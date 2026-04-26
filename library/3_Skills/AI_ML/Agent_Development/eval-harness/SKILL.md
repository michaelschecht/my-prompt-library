---
title: "Eval Harness"
tags: ["evals", "agent-evaluation", "quality", "regression-testing", "ai-engineering"]
category: "Skills"
subcategory: "AI_ML"
source: "https://skillsmp.com/skills/affaan-m-everything-claude-code-skills-eval-harness-skill-md"
source_author: "affaan-m"
source_repository: "affaan-m/everything-claude-code"
source_stars: 160286
source_updated: "2026-03-04"
---

# Eval Harness

## Overview
Define and run evaluation-driven workflows for AI-assisted development. Use this skill when a prompt, agent, workflow, or code change needs explicit pass/fail criteria, regression checks, or reliability tracking before it is considered complete.

## When to Use
- Setting up eval-driven development for an agent or prompt workflow.
- Defining measurable success criteria before implementation.
- Measuring agent reliability with pass@k or repeated-run checks.
- Creating regression suites for prompt, model, or instruction changes.
- Comparing behavior across model versions or agent configurations.

## Evaluation Types
- **Capability evals:** prove the agent can perform a newly required behavior.
- **Regression evals:** confirm existing behavior still works after changes.
- **Code-based graders:** deterministic checks such as tests, linters, builds, schemas, or file assertions.
- **Rule-based graders:** regex, JSON schema, policy, or checklist checks.
- **Model-based graders:** rubric-scored review for open-ended outputs.
- **Human graders:** manual review for high-risk or ambiguous decisions.

## Workflow
1. Define evals before implementation: task, success criteria, expected outputs, and failure conditions.
2. Implement only against the defined behavior.
3. Run capability and regression evals, recording pass/fail results.
4. Report reliability metrics such as pass@1, pass@3, and pass^3 when repeated trials matter.
5. Store eval definitions and run history with the project so future changes can detect drift.

## Eval Template
```markdown
## EVAL DEFINITION: feature-name

### Capability Evals
1. [Behavior the agent or code must now support]
2. [Second required behavior]

### Regression Evals
1. [Existing workflow that must remain intact]
2. [Existing output contract that must not change]

### Success Metrics
- Capability evals: pass@3 >= 0.90
- Release-critical regressions: pass^3 = 1.00

### Graders
- Code grader: command or script
- Rule grader: schema, regex, or policy
- Model grader: rubric and scoring scale
```

## Reporting Template
```markdown
# Eval Report: feature-name

Capability Evals: X/Y passed
Regression Evals: X/Y passed
pass@1: N%
pass@3: N%
Status: ready | needs-fix | blocked

Failures:
- [Specific failed criterion and evidence]
```

## Best Practices
- Prefer deterministic graders when possible.
- Keep evals fast enough that they will actually run.
- Include negative and edge cases, not only happy paths.
- Track cost and latency drift alongside quality.
- Version evals with the code, prompt, or agent instructions they protect.

## Source Notes
Adapted from the SkillsMP `eval-harness` skill, selected for very high marketplace popularity and broad coverage for agent and prompt evaluation workflows.
