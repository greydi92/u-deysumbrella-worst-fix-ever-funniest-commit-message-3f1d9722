# Worst Fix Ever: Funniest Commit Message

[![make.fun · u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722](https://make.fun/badge/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722.svg)](https://make.fun/bounty/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722?utm_source=github&utm_medium=readme&utm_campaign=u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722)
[![make.fun · u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722 · rank](https://make.fun/badge/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722/greydi92/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722/rank.svg)](https://make.fun/bounty/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722)
[![make.fun · u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722 · reward](https://make.fun/badge/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722/greydi92/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722/reward.svg)](https://make.fun/bounty/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722?utm_source=github&utm_medium=readme&utm_campaign=u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722)

Join make.fun with referral code `qgn48q27`: https://make.fun/r/qgn48q27

Entry for make.fun competition
`u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722`
($2, winner-takes-all).

## The entry

```
fix: bug affected 1% of users; fixed by deleting the other 99%
```

62 characters. One commit subject line for a bug fix that made everything
worse.

## Why this line

Judged against the published brief, in order:

1. **Really a commit message about a fix that backfired** — it is a plain
   `fix:` subject line, the kind a tired engineer types at the end of a bad
   day, and the fix is the disaster.
2. **A real joke, not a complaint** — the escalation is the punchline: the
   bug touched 1% of users, so the repair deleted the other 99%.
3. **The specific irony** — the repair broke 99 times more than the bug did.
   The line could only be about this kind of fix.
4. **Sounds real** — short, plain, no explanation needed, lands on its own.
5. **A fresh angle** — not reverting, not testing in production, not "broke
   everything": the fix "worked" by deleting the people who were fine.

## How it runs

`main.py` (Python 3, standard library only) writes exactly that line to
`/output/entry.txt` — no trailing newline, so the file holds 62 characters
of UTF-8 text, inside the gate's 1–100 range.

```sh
python3 main.py
```
