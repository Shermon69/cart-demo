# Shopping Cart — demo project

A deliberately small Python module used to demonstrate the R26-SE-038
automated testing system.

Four functions in `src/cart.py`. Two of them have problems planted in them,
so the pipeline has something real to find.

## What is wrong with it, and who should catch it

**`apply_discount` is broken.** It treats the percentage as a fraction:

```python
return total - (total * percent)      # 20% off 100 gives -1900
```

It should divide by 100. Note the history — this function has been "fixed"
twice already, and is still wrong. That is why the risk model ranks it first,
citing `bug_history`.

**`refund` promises something it never does.** Its docstring says it raises
`ValueError` when the refund exceeds the payment. The code has no such check.

Which component should find each:

| Problem | Found by | How |
|---|---|---|
| `refund`'s unkept promise | Component 1 | Compares the docstring to the code, no execution needed |
| `apply_discount` ranked riskiest | Component 2 | Two bug-fix commits touch it |
| Both, described in prose | Component 3 | LLM code review |
| `apply_discount` proven broken | Components 3 + 4 | A generated test fails: `assert -1900 == 80.0` |

## Running the demo

Open a pull request that changes something in `src/cart.py`. The workflow in
`.github/workflows/ai-test-review.yml` runs the analysis and posts its report
as a comment.

It needs one secret: `GROQ_API_KEY`, under
**Settings → Secrets and variables → Actions**.

## Two settings that matter

`fetch-depth: 0` on the checkout. The risk model reads git history, and the
default shallow clone has none — every function would look brand new and score
LOW.

`min-risk-level: LOW`. Small repositories score low across the board. On a
mature library only 1 function in 266 reached MEDIUM, so the default would
select nothing here and the run would finish having done no work.
