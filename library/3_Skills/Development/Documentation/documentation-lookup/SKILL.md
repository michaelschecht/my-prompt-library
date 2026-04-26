---
title: "Documentation Lookup"
tags: ["documentation", "context7", "api-reference", "frameworks", "current-docs"]
category: "Skills"
subcategory: "Development"
source: "https://skillsmp.com/skills/affaan-m-everything-claude-code-agents-skills-documentation-lookup-skill-md"
source_author: "affaan-m"
source_repository: "affaan-m/everything-claude-code"
source_stars: 160286
source_updated: "2026-03-16"
---

# Documentation Lookup

## Overview
Use current library, framework, and API documentation before answering implementation questions. This skill is especially useful with Context7 or another documentation retrieval tool, but the workflow also applies to official docs, SDK references, and release notes.

## When to Use
- The user asks about setup, configuration, or API usage for a named tool.
- Code depends on current framework behavior or version-specific APIs.
- The answer could be wrong if based on stale model knowledge.
- The user mentions products such as React, Next.js, Prisma, Supabase, Tailwind, Express, Vue, or similar libraries.

## Lookup Workflow
1. Identify the library, framework, product, and version from the request.
2. Resolve the official documentation source or a trusted documentation index entry.
3. Query with the user's actual task, not just the library name.
4. Prefer official sources and high-reputation package docs over community forks.
5. Use the fetched documentation to answer, including version notes when they matter.
6. If documentation is ambiguous after a small number of lookups, state the uncertainty instead of guessing.

## Context7 Pattern
```text
1. resolve-library-id
   - libraryName: "Next.js"
   - query: "How do I configure middleware in Next.js 15?"

2. Select the closest official or highest-quality library ID.

3. query-docs
   - libraryId: "/vercel/next.js"
   - query: "middleware configuration Next.js 15"
```

## Answering Rules
- Cite the library or version when it materially changes behavior.
- Show a minimal code example only after checking the docs.
- Redact secrets before sending queries to external documentation tools.
- Limit repeated lookups; if three targeted queries do not resolve the issue, explain what remains unknown.

## Best Practices
- Use the full user question as part of the query for better relevance.
- Prefer version-specific docs when the user names a version.
- Confirm package names and official org names before relying on examples.
- Treat framework migrations and beta APIs as high-risk for stale information.

## Source Notes
Adapted from the SkillsMP `documentation-lookup` skill, selected for high popularity and broad value in avoiding stale API and framework answers.
