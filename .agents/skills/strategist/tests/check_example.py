#!/usr/bin/env python3
"""Validate retained synthetic evidence and claim references, without accounts/network.

This is a fixture checker, not a platform metric parser or audience evaluator.
"""
from copy import deepcopy
from pathlib import Path
import json
import math
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]


def referenced_ids(text):
    found = set()
    for prefix, first, second_prefix, last in re.findall(
        r"\b([SP])(\d{2})(?:[–-]([SP])?(\d{2}))?\b", text
    ):
        if last and second_prefix and second_prefix != prefix:
            raise ValueError("mixed ID range")
        found.update(f"{prefix}{i:02d}" for i in range(int(first), int(last or first) + 1))
    return found


def require(condition, message):
    if not condition:
        raise ValueError(message)


def check_packet(packet):
    require(packet["contract"] == "strategist-packet/0.1", "wrong local contract")
    require(packet["fixture"] is True and packet["evidence_state"] == "synthetic",
            "synthetic data presented as actual evidence")
    require(packet["window"]["start"] is None and packet["window"]["end"] is None,
            "fictional publication window presented as observed")
    require(packet["measured_result"] is None, "invented measured result")
    require(packet["raw_view_ranking"] is None and packet["unique_audience_sum"] is None,
            "unsupported cross-platform ranking or audience sum")
    require(packet["experiment"]["state"] == "planned"
            and packet["experiment"]["result"] is None
            and packet["experiment"]["causal_claim"] is None, "fictional experiment result")
    require(all(packet["handoff"][key] is None
                for key in ("receipt", "implementation", "release_authorization")),
            "fictional handoff or release authority")
    observations = packet["observations"]
    require(len({row["id"] for row in observations}) == len(observations), "duplicate IDs")
    sources = set(re.findall(r"^### (S\d{2})$", (ROOT / "research/sources.md").read_text(), re.M))
    for row in observations:
        require(set(row["definition_sources"]) <= sources, "unregistered source")
        require(row["data_source"] == "synthetic-brief", "fabricated data provenance")
        require(row["post_age_days"] == 7, "incomparable post-age window")
        for value in (row["numerator"], row["denominator"]):
            require(value is None or (type(value) in (int, float)
                                     and math.isfinite(value) and value >= 0), "invalid count")
        if row["definition_state"] == "unresolved" or not row["denominator"]:
            require(row["derived_value"] is None, "rate without known positive base")
            continue
        require(row["platform"] == "youtube-shorts"
                and row["denominator_name"] == "engaged views", "wrong AVD base")
        require(math.isclose(row["derived_value"], row["numerator"] / row["denominator"]),
                "wrong AVD calculation")
        require(math.isclose(row["derived_apv_percent"],
                            row["derived_value"] / row["duration_seconds"] * 100),
                "wrong fixed-duration derived APV")


class Checks(unittest.TestCase):
    def setUp(self):
        self.packet = json.loads((ROOT / "examples/metric-packet.json").read_text())

    def test_retained_packet(self):
        check_packet(self.packet)

    def test_invalid_evidence_variants(self):
        mutations = [
            lambda p: p.update(evidence_state="measured"),
            lambda p: p.update(measured_result={"lift": 0.1}),
            lambda p: p.update(raw_view_ranking=["tiktok", "instagram", "youtube"]),
            lambda p: p.update(unique_audience_sum=4500),
            lambda p: p["window"].update(start="2026-11-01"),
            lambda p: p["experiment"].update(state="completed", result="winner"),
            lambda p: p["experiment"].update(causal_claim="hook caused lift"),
            lambda p: p["handoff"].update(receipt="Editor accepted"),
            lambda p: p["handoff"].update(release_authorization="approved"),
            lambda p: p["observations"][1].update(id="STR-M01"),
            lambda p: p["observations"][0].update(definition_sources=["S99"]),
            lambda p: p["observations"][0].update(denominator_name="public views"),
            lambda p: p["observations"][0].update(derived_value=10),
            lambda p: p["observations"][0].update(denominator=0),
            lambda p: p["observations"][1].update(derived_value=0.015),
            lambda p: p["observations"][2].update(denominator=1500, derived_value=10),
            lambda p: p["observations"][0].update(numerator=-1),
            lambda p: p["observations"][0].update(numerator=float("nan")),
        ]
        for index, mutate in enumerate(mutations):
            with self.subTest(invalid_variant=index + 1):
                bad = deepcopy(self.packet)
                mutate(bad)
                with self.assertRaises(ValueError):
                    check_packet(bad)

    def test_claim_traceability(self):
        registry = (ROOT / "research/sources.md").read_text()
        notes = (ROOT / "research/notes.md").read_text()
        sources = set(re.findall(r"^### (S\d{2})$", registry, re.M))
        claims = set(re.findall(r"^\| (P\d{2}) \|", notes, re.M))
        self.assertEqual(len(sources), 30)
        self.assertEqual(len(claims), 12)
        self.assertEqual(referenced_ids(notes) - claims, sources)
        for path in ROOT.rglob("*.md"):
            with self.subTest(path=str(path.relative_to(ROOT))):
                self.assertFalse(referenced_ids(path.read_text()) - sources - claims)

    def test_id_ranges_and_diagnostic_arithmetic(self):
        self.assertEqual(referenced_ids("S01–S03 P10–P12"),
                         {"S01", "S02", "S03", "P10", "P11", "P12"})
        self.assertAlmostEqual(400 / 10000 * 100, 4)
        self.assertAlmostEqual((16 / 40 - 30 / 100) * 100, 10)
        self.assertNotEqual(700 / 10000 * 100, 4)


if __name__ == "__main__":
    unittest.main(verbosity=2)
