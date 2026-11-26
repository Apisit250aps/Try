"""Check the bundled handoff example's metadata, never audio quality or sync.

Run from any directory with Python's standard library. --source optionally
compares the snapshot to the exact neighboring packet inspected at authoring.
This is an example check, not a validator for arbitrary sound-packet contracts.
"""
import argparse
import copy
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import unittest


EXAMPLE = Path(__file__).resolve().parents[1] / "examples/windup-sound-packet.json"


def check(packet):
    def require(condition, message):
        if not condition:
            raise ValueError(message)

    timeline = packet["timeline"]
    rate = Fraction(timeline["fps"]["numerator"], timeline["fps"]["denominator"])
    require(rate > 0, "positive frame rate required")
    require(timeline["interval_convention"] == "half-open", "interval convention")
    require(timeline["timing_status"] == "estimated primary allocation", "estimated timing")
    shots = packet["input_snapshot"]
    require(len({s["id"] for s in shots}) == len(shots), "duplicate shot ID")
    previous = 0
    for shot in shots:
        start, end = shot["planned_frame_interval"]
        require(start == previous and end > start, "contiguous positive primary intervals")
        require(Fraction(end - start) / rate == Fraction(str(shot["duration_seconds"])),
                "duration/timebase mismatch")
        previous = end
    require(previous == timeline["duration_frames"], "total frames")
    require(Fraction(previous) / rate == Fraction(str(timeline["duration_seconds"])),
            "total seconds")
    by_id = {s["id"]: s for s in shots}
    cues = packet["cues"]
    require(len({c["id"] for c in cues}) == len(cues), "duplicate cue ID")
    for cue in cues:
        require(len(cue["shot_ids"]) == 1, "example maps one shot per cue")
        require(cue["shot_ids"][0] in by_id, "dangling shot ID")
        shot = by_id[cue["shot_ids"][0]]
        require(cue["scene_ids"] == [shot["scene_id"]], "scene mapping")
        for key in ("narrative_beat_ids", "script_beat_ids"):
            require(cue[key] == shot[key], "typed beat mapping")
        a, b = cue["planned_frame_window"]
        lo, hi = shot["planned_frame_interval"]
        require(lo <= a < b <= hi, "cue window outside shot")
        require(cue["anchor"]["sequence_frame"] is None, "no invented measured anchor")
        require(cue["audio_evidence"] == "absent" and not cue["asset_ids"],
                "no invented audio evidence")
    require(packet["handoff"]["receipt"] is None
            and packet["handoff"]["acceptance"] is None
            and packet["handoff"]["dispatch"] == "not-performed", "no invented handoff")


class ExampleChecks(unittest.TestCase):
    def setUp(self):
        self.packet = json.loads(EXAMPLE.read_text())

    def test_example(self):
        check(self.packet)

    def test_invalid_variants(self):
        mutations = [
            lambda p: p["cues"][0].update(shot_ids=["absent"]),
            lambda p: p["cues"][0].update(script_beat_ids=["NB01"]),
            lambda p: p["cues"][0].update(scene_ids=["S999"]),
            lambda p: p["cues"][0].update(planned_frame_window=[-1, 9999]),
            lambda p: p["cues"][1].update(id=p["cues"][0]["id"]),
            lambda p: p["input_snapshot"][0].update(duration_seconds=99),
            lambda p: p["timeline"].update(timing_status="measured"),
            lambda p: p["cues"][0]["anchor"].update(sequence_frame=1),
            lambda p: p["cues"][0].update(audio_evidence="measured"),
            lambda p: p["handoff"].update(receipt="approved by Editor"),
        ]
        for index, mutate in enumerate(mutations):
            with self.subTest(invalid_variant=index):
                packet = copy.deepcopy(self.packet)
                mutate(packet)
                with self.assertRaises(ValueError):
                    check(packet)


def compare_source(path):
    raw = path.read_bytes()
    source = json.loads(raw)
    packet = json.loads(EXAMPLE.read_text())
    if hashlib.sha256(raw).hexdigest() != packet["upstream"]["source_sha256"]:
        raise ValueError("Source changed since authoring; review adapter before updating snapshot")
    if source["locked_facts"] != packet["locked_facts"]:
        raise ValueError("Locks differ")
    if (source["project_id"] != packet["project_id"]
            or source["version"] != packet["upstream"]["version"]
            or source["contract"] != packet["upstream"]["contract"]):
        raise ValueError("Upstream identity/version differs")
    fps = packet["timeline"]["fps"]
    if Fraction(fps["numerator"], fps["denominator"]) != Fraction(str(source["format"]["fps"])):
        raise ValueError("Proposed playback rate differs")
    shots = {s["id"]: s for s in source["shots"]}
    if source["proposed_sequence"] != [s["id"] for s in packet["input_snapshot"]]:
        raise ValueError("Primary sequence differs")
    for snapshot in packet["input_snapshot"]:
        for key, value in snapshot.items():
            if key != "planned_frame_interval" and shots[snapshot["id"]][key] != value:
                raise ValueError(f"Source mapping differs: {snapshot['id']} {key}")
    print("Exact source hash, primary sequence, locks and typed shot fields match")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path)
    args = parser.parse_args()
    result = unittest.TextTestRunner().run(unittest.defaultTestLoader.loadTestsFromTestCase(ExampleChecks))
    if not result.wasSuccessful():
        raise SystemExit(1)
    if args.source:
        compare_source(args.source)
