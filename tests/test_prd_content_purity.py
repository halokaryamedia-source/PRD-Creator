from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = ROOT / "kits" / "project-document-generator" / "validator" / "validate.py"


def load_validator_module():
    spec = importlib.util.spec_from_file_location("prd_validate_content_purity", VALIDATOR)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


class ProjectDocumentContentPurity(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.validator = load_validator_module()

    def test_rejects_observed_document_process_leakage(self) -> None:
        data = {
            "overview": {
                "main_systems": [
                    {"title": "Global Rule 1", "description": "Golden HTML structure remains unchanged."},
                ]
            },
            "global_development": [
                {
                    "overview": "Every stage uses the same three-page contract.",
                    "notes": [
                        "Every objective has one Gameplay Overview page and one Developer page.",
                    ],
                }
            ],
            "packages": [],
        }
        errors = self.validator.content_purity_errors(data)
        joined = "\n".join(errors)
        self.assertIn("Golden HTML/reference language", joined)
        self.assertIn("document-contract narration", joined)
        self.assertIn("visible page-role narration", joined)
        self.assertIn("generic", joined)
        self.assertIn("plain note strings render as generic Important Note cards", joined)

    def test_accepts_project_facing_content_and_semantic_note_titles(self) -> None:
        data = {
            "overview": {
                "main_systems": [
                    {
                        "title": "Always Recoverable",
                        "description": "Mistakes cost time or position but never create an unwinnable state.",
                    },
                ]
            },
            "global_development": [
                {
                    "overview": "Shared runtime owns session start, transitions, interruption, and reset.",
                    "notes": [
                        {
                            "title": "Lane Isolation",
                            "description": "Visual, audio, entity, and gameplay state stay inside the assigned lane.",
                        }
                    ],
                }
            ],
            "packages": [
                {
                    "level_design": {
                        "notes": [
                            {
                                "title": "Readable Trap Tells",
                                "description": "Every trap communicates warning, active, and safe states.",
                            }
                        ]
                    },
                    "developer": {
                        "notes": [
                            {
                                "title": "No State Carryover",
                                "description": "Temporary objective state is cleared before lane reuse.",
                            }
                        ]
                    },
                }
            ],
        }
        self.assertEqual(self.validator.content_purity_errors(data), [])


if __name__ == "__main__":
    unittest.main()
