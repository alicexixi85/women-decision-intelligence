"""WDI free MCP preview: deterministic six-constraint evidence checklist.

Standalone Python 3.11+, JSON-RPC over newline-framed stdio. No network,
AI calls, storage, personal profiles, or paid case-library access.
The full commercial WDI decision Skill is not included.
"""
import json
import sys

VERSION = "2025-06-18"
FIELDS = ("cash", "time", "care", "safety", "control", "institutions")
GRADES = ("KNOWN", "ASSUMED", "UNKNOWN", "SYNTHETIC")
QUESTIONS = {
    "cash": "What funds remain accessible after fixed costs and debt?",
    "time": "Which deadlines and obligations cannot be moved?",
    "care": "Who relies on unpaid care, and what would replacement cost?",
    "safety": "Does any option involve threats, coercion, abuse or concealment?",
    "control": "Who can approve, transfer, spend or revoke key resources?",
    "institutions": "Which contracts, benefits, rules or permits need verification?",
}

TOOL = {
    "name": "review_six_constraints",
    "description": "Free six-constraint evidence checklist; no decisions, forecasts, or professional advice.",
    "inputSchema": {
        "type": "object",
        "properties": {
            "decision": {"type": "string", "description": "A brief decision title, not private identifiers."},
            "constraints": {
                "type": "object",
                "description": "Six evidence grades; omit unknown dimensions.",
                "properties": {field: {"type": "string", "enum": list(GRADES)} for field in FIELDS},
                "additionalProperties": False,
            },
        },
        "required": ["decision"],
        "additionalProperties": False,
    },
}


def review(arguments):
    """Return only user-supplied grades and general questions, never inferred facts."""
    if not isinstance(arguments, dict) or set(arguments) - {"decision", "constraints"}:
        raise ValueError("Arguments must contain only decision and constraints.")
    decision = arguments.get("decision")
    if not isinstance(decision, str) or not decision.strip() or len(decision) > 200:
        raise ValueError("Decision title must be 1–200 characters.")
    values = arguments.get("constraints", {})
    if not isinstance(values, dict) or set(values) - set(FIELDS):
        raise ValueError("Use only the six defined constraint keys.")
    if any(grade not in GRADES for grade in values.values()):
        raise ValueError("Use only KNOWN / ASSUMED / UNKNOWN / SYNTHETIC grades.")
    rows = [
        {"constraint": field, "grade": values.get(field, "UNKNOWN"), "check": QUESTIONS[field]}
        for field in FIELDS
    ]
    return {
        "decision": decision.strip(),
        "evidence_only": True,
        "constraints": rows,
        "needs_verification": [r["constraint"] for r in rows if r["grade"] != "KNOWN"],
        "first_reversible_step": "Verify one material unknown before making an irreversible commitment.",
        "boundary": "Educational checklist only; not legal, medical, mental-health or financial advice. If threatened or unsafe, prioritize safety and local trusted support.",
        "full_framework": "https://dejunchen770231.gumroad.com/l/wdi-womens-decision-intelligence",
    }


def process(request):
    """A minimal compatible MCP 2025-06-18 legacy initialize/tools surface."""
    if not isinstance(request, dict) or request.get("jsonrpc") != "2.0":
        return {"jsonrpc": "2.0", "id": None, "error": {"code": -32600, "message": "Invalid JSON-RPC request"}}
    if "id" not in request:  # notifications have no response
        return None
    ident = request["id"]
    method = request.get("method")
    if method == "initialize":
        result = {
            "protocolVersion": VERSION,
            "serverInfo": {"name": "wdi-six-constraint-preview", "version": "1.0.0"},
            "capabilities": {"tools": {}},
        }
    elif method == "ping":
        result = {}
    elif method == "tools/list":
        result = {"tools": [TOOL]}
    elif method == "tools/call":
        params = request.get("params")
        if not isinstance(params, dict) or params.get("name") != TOOL["name"]:
            return {"jsonrpc": "2.0", "id": ident, "error": {"code": -32602, "message": "Unknown tool"}}
        try:
            result = {"content": [{"type": "text", "text": json.dumps(review(params.get("arguments", {})), ensure_ascii=False)}], "isError": False}
        except ValueError as exc:
            result = {"content": [{"type": "text", "text": str(exc)}], "isError": True}
    else:
        return {"jsonrpc": "2.0", "id": ident, "error": {"code": -32601, "message": "Unknown method"}}
    return {"jsonrpc": "2.0", "id": ident, "result": result}


def main():
    for raw in sys.stdin:
        try:
            request = json.loads(raw)
        except json.JSONDecodeError:
            response = {"jsonrpc": "2.0", "id": None, "error": {"code": -32700, "message": "Invalid JSON"}}
        else:
            response = process(request)
        if response is not None:
            sys.stdout.write(json.dumps(response, ensure_ascii=False, separators=(",", ":")) + "\n")
            sys.stdout.flush()


if __name__ == "__main__":
    main()
