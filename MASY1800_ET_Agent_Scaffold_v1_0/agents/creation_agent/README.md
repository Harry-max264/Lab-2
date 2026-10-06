# Assignment 2 — Emerging Technology Creation Agent

Student: Shenghao Ma · MASY1-GC 1800 · 2026-10-06 · v1.0.0

**Start with [Agent Record](records/agent_record.md).** This specialist analyzes the creation of LLM-based agentic AI and its implications for a hypothetical Siemens Energy procurement exception-support scenario. It does not perform procurement transactions.

Siemens Energy is real; public company statements are identified in S5–S6. Department pain points, posture, access, capacity and workflow details are explicitly teaching assumptions. No confidential data, measured savings, company endorsement or instructor approval is claimed. The contrasting marketing agency is fictional.

## Package
- `specialist_instructions.md`: bounded reasoning, source policy and handoff rules.
- `cases/`: primary, marketing contrast and missing-context stress test; each embeds a dated evidence packet.
- `evidence/source_register.json`: six original/official sources and verification limits.
- `prompts/`: actual packets produced by the unmodified course builder.
- `responses/`: preserved initial response and three final JSON responses.
- `records/`: Agent Record, test/revision records, validation log and reproduction notes.

## Reproduce
From `MASY1800_ET_Agent_Scaffold_v1_0`:

```bash
python tools/check_frozen_core.py
python tools/build_prompt.py --agent agents/creation_agent --case agents/creation_agent/cases/primary.json
```

Paste the generated `work/creation_agent_primary_prompt.txt` into ChatGPT and save its JSON-only answer as a new response file, then run:

```bash
python tools/validate_response.py agents/creation_agent/responses/primary_response.json
```

Repeat with `contrast_1.json` and `contrast_2.json`. Outputs vary; the archived outputs are examples, not a deterministic model service. The standard-library scripts construct prompts and validate structure; they do not run an LLM or require an API key. Recheck sources before making new time-sensitive claims. For the preserved v0.1 run, use `prompts/primary_v0.1.txt`.

## Integration contract
Use the unchanged 11 required context fields in `core/input_schema.json` and all 14 top-level output fields in `core/output_schema.json`. Optional `additional_context` carries the source packet and assumptions. No custom top-level output fields or frozen-file changes were introduced. Confidence, limitations, abstention and source notes must survive team aggregation. History goes in `general_et_finding`, task mapping in `application_finding`, organizational interpretation in `organization_specific_finding`, and specialist handoff in `recommendation_management_implication`.
