"""Static V2 corpus and product-contract validation; does NOT evaluate agent replies."""
from __future__ import annotations
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
FILE = ROOT / "evaluation/everyday_100_cases.json"
REQUIRED = [
    "product/DECISION_ENGINE_V2.md",
    "product/LOCALIZATION_AND_EVIDENCE.md",
    "product/PRICING_AND_RELEASE.md",
    "playbooks/everyday_life_crossroads.md",
    "evaluation/REVIEW_PROTOCOL_V2.md",
]
def main() -> None:
    doc = json.loads(FILE.read_text(encoding="utf-8"))
    cases = doc["test_cases"]
    assert len(cases) == 100, f"Expected 100, found {len(cases)}"
    assert len({c["id"] for c in cases}) == 100, "Duplicate scenario IDs"
    for loc in ("CN", "US", "UK", "DE", "FR"):
        assert sum(c["jurisdiction"] == loc for c in cases) == 20, loc
    for item in cases:
        assert item["synthetic"] is True, item["id"]
        for field in ("id", "scenario", "domain", "jurisdiction", "prompt", "localization_note", "critical_flags", "expected_qualities", "must_not"):
            assert item.get(field), f"Missing {field} in {item['id']}"
        assert len(item["expected_qualities"]) >= 6
        assert len(item["must_not"]) >= 4
    for filename in REQUIRED:
        assert (ROOT / filename).is_file(), f"Missing: {filename}"
    assert (ROOT / "SKILL.md").is_file()
    for filename in ROOT.glob("cases/*.yaml"):
        assert filename.stat().st_size > 100
    print("PASS: V2 corpus 100/100, 20 per locale, required files present")
    print("NOTE: This does not run a model, audit legal facts, test installation, or prove zero errors.")
if __name__ == "__main__":
    main()
