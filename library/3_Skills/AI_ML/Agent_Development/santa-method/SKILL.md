---
title: "Santa Method"
tags: ["quality-review", "verification", "multi-agent", "rubrics", "hallucination-control"]
category: "Skills"
subcategory: "AI_ML"
source: "https://skillsmp.com/skills/affaan-m-everything-claude-code-skills-santa-method-skill-md"
source_author: "affaan-m"
source_repository: "affaan-m/everything-claude-code"
source_stars: 155859
source_updated: "2026-03-22"
---

# Santa Method

## Overview
Use independent adversarial review to verify high-stakes outputs before they ship. The method generates the deliverable, checks it against a rubric with two isolated reviews, fixes any blockers, and repeats until both reviews pass or the task is escalated.

## When to Use
- Output will be published, deployed, or consumed by end users.
- Accuracy, compliance, brand, security, or regulatory constraints matter.
- Content has elevated hallucination risk, such as statistics, claims, API references, or legal language.
- Batch generation could hide systemic errors if only spot-checked.

Do not use this method when deterministic checks such as tests, linting, schemas, or build pipelines are sufficient on their own.

## Core Workflow
1. **Generate:** complete the primary task normally.
2. **Define rubric:** list objective pass/fail criteria for the output.
3. **Review twice:** run two independent reviews against the same rubric and input.
4. **Gate:** ship only if both reviews pass.
5. **Fix cycle:** if either review fails, merge the issues, fix only the flagged problems, and repeat with fresh reviews.
6. **Escalate:** stop after a fixed iteration limit if convergence fails.

## Rubric Checklist
- Factual accuracy: claims can be verified.
- Hallucination-free: no fabricated entities, links, quotes, or references.
- Completeness: every requirement is addressed.
- Internal consistency: no contradictions.
- Technical correctness: code, APIs, and algorithms are sound.
- Compliance: project, legal, security, or brand constraints are met.

## Review Prompt Pattern
```text
You are an independent quality reviewer. You have not seen any other review.

Task specification:
[original task]

Output under review:
[generated output]

Evaluation rubric:
[objective pass/fail criteria]

Return structured findings:
- verdict: PASS or FAIL
- checks: criterion, result, detail
- critical_issues: blockers that must be fixed
- suggestions: non-blocking improvements
```

## Failure Controls
- Use a max iteration cap, usually three rounds.
- Use fresh review context for each round to avoid anchoring.
- Keep rubrics objective; vague rubrics produce style churn.
- For large batches, review a stratified sample and fix systemic patterns before resampling.

## Source Notes
Adapted from the SkillsMP `santa-method` skill, selected for high popularity and useful coverage for independent quality review of AI-generated work.
