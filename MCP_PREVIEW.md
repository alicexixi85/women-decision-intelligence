# WDI six-constraint MCP preview — free limited demo

This repository was **already the public WDI showcase**. Its complete bilingual decision intelligence product is a separate **$35 one-time purchase** at [Gumroad](https://dejunchen770231.gumroad.com/l/wdi-womens-decision-intelligence). This demo is **not** that paid Skill or the 75-file commercial package, and no commercial source is included.

The new `wdi_mcp_preview.py` is a small, working **Python 3.11+ MCP stdio server**, with no external dependencies, network traffic or data retention. It returns a deterministic checklist for six constraints: cash, time, care, safety, control and institutions. Evidence is graded using `KNOWN`, `ASSUMED`, `UNKNOWN`, `SYNTHETIC` (missing = `UNKNOWN`). It does **not** generate case retrieval, jurisdiction-dependent advice, scores, predictions or individualized legal/medical/financial advice.

## Install and run

```bash
python --version   # Python 3.11+
python wdi_mcp_preview.py
```

Use your MCP client's **stdio** configuration with the absolute Python executable path as `command`, the absolute path to `wdi_mcp_preview.py` as the single argument, and this repository as the working directory. **No `node dist/index.js` and no paid downloads are required for the free demo.**

Tool: `review_six_constraints`; parameters:

```json
{
  "decision": "Whether to change careers",
  "constraints": {
    "cash": "KNOWN",
    "time": "UNKNOWN",
    "care": "ASSUMED",
    "safety": "UNKNOWN",
    "control": "KNOWN",
    "institutions": "UNKNOWN"
  }
}
```

This is a local, read-only preview. It sends no data to a server and stores no responses. See the [existing six-constraint free worksheet](FREE-DECISION-CHECKLIST.md) for the source of the six dimensions and the current repository [LICENSE](LICENSE) for rights restrictions; the repository is **not generally open source**.

## Test, evidence and limits

Run the local offline test suite: `python -m unittest test_wdi_mcp_preview -v`.

The demo implements the **2025-06-18 legacy MCP stdio initialization and tool calls**. Newer stateless/discovery-only MCP clients may require a more recent protocol implementation. Tool output is a structured restatement of user-provided labels and reference questions, not an analysis of confidential personal information. This public preview is not a substitute for the paid product, specialist advice or safety support.
