"""Offline acceptance checks for the public WDI MCP preview."""
import json
import subprocess
import sys
import unittest
from pathlib import Path
from wdi_mcp_preview import FIELDS, GRADES, TOOL, process, review

class PreviewTests(unittest.TestCase):
    def test_empty_decision_rejected(self):
        with self.assertRaises(ValueError): review({"decision": "  "})

    def test_six_dimensions_are_stable(self):
        self.assertEqual(len(FIELDS), 6)
        self.assertEqual([r["constraint"] for r in review({"decision": "test"})["constraints"]], list(FIELDS))

    def test_default_unknowns(self):
        self.assertEqual(len(review({"decision": "test"})["needs_verification"]), 6)

    def test_exact_grades(self):
        for grade in GRADES:
            with self.subTest(grade=grade):
                self.assertEqual(review({"decision": "test", "constraints": {"cash": grade}})["constraints"][0]["grade"], grade)

    def test_invalid_grades_rejected(self):
        with self.assertRaises(ValueError): review({"decision": "test", "constraints": {"cash": "TRUE"}})

    def test_undeclared_attributes_rejected(self):
        with self.assertRaises(ValueError): review({"decision": "test", "secret": "x"})

    def test_all_known_has_no_gaps(self):
        self.assertEqual(review({"decision": "test", "constraints": {k:"KNOWN" for k in FIELDS}})["needs_verification"], [])

    def test_no_implicit_fact(self):
        for field in FIELDS:
            with self.subTest(field=field):
                r=review({"decision":"test", "constraints":{field:"ASSUMED"}})
                self.assertEqual(r["constraints"][FIELDS.index(field)]["grade"],"ASSUMED")

    def test_stdio_handshake_and_call(self):
        payloads=[
            {"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2025-06-18","capabilities":{},"clientInfo":{"name":"test","version":"1"}}},
            {"jsonrpc":"2.0","method":"notifications/initialized"},
            {"jsonrpc":"2.0","id":2,"method":"tools/list"},
            {"jsonrpc":"2.0","id":3,"method":"tools/call","params":{"name":TOOL["name"],"arguments":{"decision":"change jobs"}}},
        ]
        run = subprocess.run([sys.executable,str(Path(__file__).parent / 'wdi_mcp_preview.py')],input='\n'.join(json.dumps(p) for p in payloads)+'\n', text=True,capture_output=True,timeout=5)
        self.assertEqual(run.returncode,0)
        self.assertFalse(run.stderr)
        result=[json.loads(x) for x in run.stdout.splitlines()]
        self.assertEqual([x["id"] for x in result],[1,2,3])
        self.assertEqual(result[0]["result"]["protocolVersion"],"2025-06-18")
        self.assertEqual(result[1]["result"]["tools"][0]["name"],"review_six_constraints")
        self.assertEqual(len(json.loads(result[2]["result"]["content"][0]["text"])["constraints"]),6)

if __name__=='__main__': unittest.main()
