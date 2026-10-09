import unittest
import json
import os
import sys

# Tambahkan direktori root modul ke sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from scripts.rubric_grader import grade_submission, evaluate_database_schema, evaluate_workflow_state

class TestRubricGrader(unittest.TestCase):

    def test_evaluate_database_schema_valid(self):
        schema = {
            "tables": [
                {
                    "name": "users",
                    "columns": [
                        {"name": "id", "type": "UUID", "is_pk": True},
                        {"name": "email", "type": "VARCHAR(255)", "is_pk": False}
                    ]
                },
                {
                    "name": "orders",
                    "columns": [
                        {"name": "id", "type": "UUID", "is_pk": True},
                        {"name": "user_id", "type": "UUID", "is_fk": True, "references": "users.id"}
                    ]
                }
            ]
        }
        score, findings = evaluate_database_schema(schema)
        self.assertGreaterEqual(score, 80)
        self.assertEqual(len(findings), 0)

    def test_evaluate_database_schema_missing_pk(self):
        schema = {
            "tables": [
                {
                    "name": "logs",
                    "columns": [
                        {"name": "message", "type": "TEXT", "is_pk": False}
                    ]
                }
            ]
        }
        score, findings = evaluate_database_schema(schema)
        self.assertLess(score, 70)
        self.assertTrue(any("Primary Key" in f for f in findings))

    def test_evaluate_workflow_state_valid(self):
        workflow = {
            "initial": "draft",
            "states": [
                {"name": "draft", "transitions": [{"event": "SUBMIT", "target": "review"}]},
                {"name": "review", "transitions": [{"event": "APPROVE", "target": "published"}]},
                {"name": "published", "transitions": []}
            ]
        }
        score, findings = evaluate_workflow_state(workflow)
        self.assertGreaterEqual(score, 85)
        self.assertEqual(len(findings), 0)

    def test_evaluate_workflow_state_missing_initial(self):
        workflow = {
            "states": [
                {"name": "step1", "transitions": []}
            ]
        }
        score, findings = evaluate_workflow_state(workflow)
        self.assertLess(score, 60)
        self.assertTrue(any("initial state" in f for f in findings))

    def test_grade_submission_comprehensive(self):
        payload = {
            "author": "Test Contributor",
            "project_name": "E-Commerce Escrow Blueprint",
            "database": {
                "tables": [
                    {"name": "escrow_account", "columns": [{"name": "id", "type": "BIGINT", "is_pk": True}]}
                ]
            },
            "workflow": {
                "initial": "pending",
                "states": [
                    {"name": "pending", "transitions": [{"event": "PAY", "target": "funded"}]},
                    {"name": "funded", "transitions": []}
                ]
            }
        }
        result = grade_submission(payload)
        self.assertIn("total_score", result)
        self.assertIn("grade", result)
        self.assertIn("findings", result)
        self.assertGreaterEqual(result["total_score"], 75)

if __name__ == "__main__":
    unittest.main()
