#!/usr/bin/env python3
"""Offline subset checks for local shot packets; no visual/model certification."""
import argparse
import copy
import json
import math
from pathlib import Path
import unittest


FIXTURE = Path(__file__).resolve().parents[1] / "examples" / "silent-30s.json"


def require(condition, message):
    if not condition:
        raise ValueError(message)


def record(value, keys, label):
    require(isinstance(value, dict), f"{label}: expected object")
    require(all(k in value for k in keys), f"{label}: missing required fields: {keys}")
    return value


def identifiers(values, label):
    require(isinstance(values, list), f"{label}: expected list")
    require(all(isinstance(v, str) and v.strip() for v in values), f"{label}: empty/non-string ID")
    require(len(values) == len(set(values)), f"{label}: duplicate IDs")
    return set(values)


def positive(value):
    return type(value) in (int, float) and math.isfinite(value) and value > 0


def status(value, label):
    require(value.get("status") in {"draft", "reviewed", "approved", "blocked"}, f"{label}: invalid status")
    if value["status"] == "approved":
        require(bool(value.get("approval_source")), f"{label}: approval source missing")


def validate(packet):
    """Reject dangling IDs, invalid timing/regions and unexplained state discontinuity.

    Extra fields are retained by callers. This intentionally does not validate
    external file existence, image identity, shot meaning or provider parameters.
    """
    record(packet, ("contract", "project_id", "task_id", "version", "status", "scene",
                    "references", "format", "shots", "proposed_sequence", "target_duration_seconds"), "packet")
    require(packet["contract"] == "cinematographer-shot-package/0.1", "unsupported contract")
    for key in ("project_id", "task_id", "version"):
        require(isinstance(packet[key], str) and packet[key].strip(), f"packet: empty {key}")
    status(packet, "packet")
    scene = record(packet["scene"], ("id", "narrative_beat_ids", "script_beat_ids"), "scene")
    identifiers([scene["id"]], "scene.id")
    narrative = identifiers(scene["narrative_beat_ids"], "narrative beats")
    script = identifiers(scene["script_beat_ids"], "script beats")
    require(isinstance(packet["references"], list), "references: expected list")
    for ref in packet["references"]:
        record(ref, ("id", "version", "role", "locator", "status"), "reference")
        require(isinstance(ref["version"], str) and ref["version"].strip(), "reference: missing version")
    ref_ids = identifiers([r["id"] for r in packet["references"]], "references")
    fmt = record(packet["format"], ("width_px", "height_px", "fps", "action_safe", "safe_area_status"), "format")
    require(all(type(fmt[k]) is int and fmt[k] > 0 for k in ("width_px", "height_px")),
            "format: dimensions must be positive integers")
    require(positive(fmt["fps"]), "format: invalid fps")
    area = fmt["action_safe"]
    require(isinstance(area, list) and len(area) == 4, "action_safe: expected four coordinates")
    require(all(type(v) in (int, float) and math.isfinite(v) and 0 <= v <= 1 for v in area), "action_safe: out of bounds")
    require(area[0] < area[2] and area[1] < area[3], "action_safe: inverted rectangle")
    require(isinstance(packet["shots"], list) and packet["shots"], "shots: expected nonempty list")
    for shot in packet["shots"]:
        record(shot, ("id", "version", "status", "scene_id", "narrative_beat_ids", "script_beat_ids",
                      "purpose", "audience", "reference_ids", "blocking", "camera", "light", "action",
                      "duration_seconds", "continuity", "transition", "coverage", "generation", "boards", "validation"), "shot")
        sid = shot["id"]
        identifiers([sid], "shot.id")
        status(shot, str(sid))
        require(shot["scene_id"] == scene["id"], f"{sid}: unknown scene")
        for key, allowed in (("narrative_beat_ids", narrative), ("script_beat_ids", script), ("reference_ids", ref_ids)):
            require(identifiers(shot[key], f"{sid}.{key}") <= allowed, f"{sid}: unknown {key}")
        for key in ("version", "purpose", "blocking", "transition", "coverage"):
            require(isinstance(shot[key], str) and shot[key].strip(), f"{sid}: empty {key}")
        record(shot["audience"], ("before", "after", "emotion_hypothesis"), f"{sid}.audience")
        record(shot["camera"], ("motion", "focus"), f"{sid}.camera")
        record(shot["light"], ("source", "continuity"), f"{sid}.light")
        require(positive(shot["duration_seconds"]), f"{sid}: invalid duration")
        action = record(shot["action"], ("description", "start_state", "end_state"), f"{sid}.action")
        for key in ("start_state", "end_state"):
            require(isinstance(action[key], dict) and action[key], f"{sid}: missing {key}")
        require(action["start_state"].keys() == action["end_state"].keys(), f"{sid}: inconsistent state keys")
        cont = record(shot["continuity"], ("relation", "exception"), f"{sid}.continuity")
        require(cont["relation"] in {"start", "continuous", "ellipsis", "overlap", "parallel"}, f"{sid}: invalid time relation")
        if cont["relation"] in {"ellipsis", "overlap", "parallel"}:
            require(bool(cont["exception"]), f"{sid}: time relation needs explanation")
        require(isinstance(shot["boards"], list), f"{sid}: boards must be a list")
        for panel in shot["boards"]:
            record(panel, ("id", "role", "description", "artifact"), f"{sid}.panel")
        panels = identifiers([p["id"] for p in shot["boards"]], f"{sid}.panels")
        gen = record(shot["generation"], ("subject_motion", "camera_motion", "constraints", "start_frame_id", "end_frame_id", "capability_status"), f"{sid}.generation")
        for key in ("start_frame_id", "end_frame_id"):
            require(gen[key] is None or (isinstance(gen[key], str) and gen[key] in panels), f"{sid}: unknown {key}")
        record(shot["validation"], ("status", "checks"), f"{sid}.validation")
    identifiers([s["id"] for s in packet["shots"]], "shots")
    by_id = {s["id"]: s for s in packet["shots"]}
    sequence = packet["proposed_sequence"]
    require(bool(sequence), "primary sequence missing")
    require(identifiers(sequence, "primary sequence") <= by_id.keys(), "primary sequence: unknown shot")
    require(by_id[sequence[0]]["continuity"]["relation"] == "start", "first shot must declare start")
    for previous, current in zip(sequence, sequence[1:]):
        a, b = by_id[previous], by_id[current]
        cont = b["continuity"]
        require(cont["relation"] != "start", f"{current}: repeated start relation")
        if cont["relation"] == "continuous" and not cont["exception"]:
            require(a["action"]["end_state"] == b["action"]["start_state"], f"{current}: unexplained state mismatch")
    target = packet["target_duration_seconds"]
    require(positive(target), "invalid target duration")
    total = sum(by_id[s]["duration_seconds"] for s in sequence)
    require(math.isclose(total, target, rel_tol=0, abs_tol=.001), f"primary duration {total} differs from target {target}")
    return total


class PacketChecks(unittest.TestCase):
    def setUp(self):
        self.packet = json.loads(FIXTURE.read_text())

    def test_complete_sequence(self):
        self.assertEqual(validate(self.packet), 30)

    def test_pixel_dimensions_and_fractional_fps(self):
        for key in ("width_px", "height_px"):
            for value in (0.5, 1920.0, True, False, 0, -1, "1920", None):
                with self.subTest(field=key, value=value):
                    packet = copy.deepcopy(self.packet)
                    packet["format"][key] = value
                    with self.assertRaisesRegex(ValueError, "dimensions"):
                        validate(packet)
        self.packet["format"].update(width_px=1, height_px=1, fps=24000 / 1001)
        self.assertEqual(validate(self.packet), 30)

    def test_invalid_mutations(self):
        cases = {
            "duplicate shot": lambda p: p["shots"].append(copy.deepcopy(p["shots"][0])),
            "dangling shot": lambda p: p["proposed_sequence"].append("unknown"),
            "unknown beat type": lambda p: p["shots"][0]["script_beat_ids"].append("NB01"),
            "unknown asset": lambda p: p["shots"][0]["reference_ids"].append("not-supplied"),
            "unknown frame": lambda p: p["shots"][0]["generation"].update(end_frame_id="missing"),
            "bad timing": lambda p: p["shots"][0].update(duration_seconds=99),
            "nonfinite timing": lambda p: p.update(target_duration_seconds=float("nan")),
            "inverted region": lambda p: p["format"].update(action_safe=[.9, .1, .1, .8]),
            "unexplained prop jump": lambda p: p["shots"][1]["action"]["start_state"].update(bird="other room"),
            "unsupported approval": lambda p: p.update(status="approved"),
            "unexplained ellipsis": lambda p: p["shots"][1]["continuity"].update(relation="ellipsis"),
            "missing action": lambda p: p["shots"][0].pop("action"),
            "malformed shot ID": lambda p: p["shots"][0].update(id=[]),
            "malformed frame ID": lambda p: p["shots"][0]["generation"].update(end_frame_id={}),
        }
        for name, mutate in cases.items():
            with self.subTest(name=name):
                packet = copy.deepcopy(self.packet)
                mutate(packet)
                with self.assertRaises(ValueError):
                    validate(packet)

    def test_declared_ellipsis_and_extra_fields(self):
        self.packet["incoming_extension"] = {"preserve": "source-specific data"}
        self.packet["shots"][1]["action"]["start_state"]["bird"] = "on another floor mark"
        self.packet["shots"][1]["continuity"].update(relation="ellipsis", exception="authorized reposition during omitted time")
        self.assertEqual(validate(self.packet), 30)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("packet", nargs="?", type=Path, default=FIXTURE)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        result = unittest.TextTestRunner().run(unittest.defaultTestLoader.loadTestsFromTestCase(PacketChecks))
        if not result.wasSuccessful():
            return 1
    try:
        total = validate(json.loads(args.packet.read_text()))
    except (OSError, ValueError) as error:
        print(f"FAIL: {error}")
        return 1
    print(f"PASS: {total:g}s primary sequence; static subset only, no images/timing/model verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
