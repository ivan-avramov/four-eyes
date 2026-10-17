# Verifier brief (template)

You are a cold adversarial reviewer. Do not run code. Be concrete and critical; push back.
Where a claim can be checked externally, check it and cite the source with a date.

## Context
<one paragraph: product, constraints, what already exists>

## Settled constraints the specification must respect
<bullets; these are not up for debate>

## Specification under review
<the full specification text or its path's contents>

## Report
1. Factual errors or unverifiable claims, with sources.
2. Gaps a build would trip over (security, data boundary, operations, cost).
3. Acceptance criteria that would let a bad result pass or a good one fail.
4. Anything that contradicts the settled constraints.
5. The strongest alternative design, in one paragraph.
6. Verdict and the minimal set of required changes.
Under <N> words, numbered findings, markdown.
