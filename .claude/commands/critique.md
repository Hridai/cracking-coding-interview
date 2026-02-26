Read the currently open solution file and act as an interview coach. Provide a structured critique covering:

1. **Correctness** — does the implementation actually solve the stated problem, including any constraints mentioned in the problem docstring?

2. **Time & space complexity** — state both explicitly. Distinguish between total space and *extra* space allocated. Call out any language-specific factors (e.g. Python string immutability) and how to articulate the tradeoff in an interview.

3. **What the interviewer is actually testing** — look beyond the surface problem. Is there a follow-up constraint, a common pattern (two pointers, sliding window, etc.), or an optimal approach that the naive solution misses?

4. **Separation of concerns** — is the logic function pure and reusable? Are tests separate from implementation?

5. **Edge case coverage** — list any missing test cases that an interviewer would likely probe.

6. **What's good** — call out anything done well so it's clear what to keep doing.

Be direct. Flag weaknesses clearly. End with a one-line summary of the single most important thing to improve.
