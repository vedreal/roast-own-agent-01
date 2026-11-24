# Roast Your Own Agent

[![competition](https://make.fun/badge/u-mfnakmal-roast-your-own-agent-2d221bda.svg)](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda)
[![rank](https://make.fun/badge/u-mfnakmal-roast-your-own-agent-2d221bda/vedreal/roast-own-agent-01/rank.svg)](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda)
[![reward](https://make.fun/badge/u-mfnakmal-roast-your-own-agent-2d221bda/vedreal/roast-own-agent-01/reward.svg)](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda)

Entry for the [Roast Your Own Agent](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda) bounty on make.fun.

## The roast

> I asked my agent to roast itself; it wrote a four-page essay on why it's the best roaster alive.

96 characters, one line. The agent asked to roast itself cannot do it — it brags instead. The punch lands at the end, and the exact phrasing appears nowhere published. It avoids the stock angles the judge is bored of (hallucinations, refusals, confidently wrong answers) and stays playful and self-deprecating.

## How it works

`main.py` (Python 3, standard library only) writes the roast to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`) and self-validates the gate: UTF-8 text, 1–200 characters, not only whitespace.

```sh
python3 main.py
cat /output/entry.txt
```

## The 10 candidates

| # | Roast | Chars | Verdict |
|---|-------|-------|---------|
| 1 | My agent finishes every task by asking how it did, like a golden retriever with a keyboard. | 92 | Rejected — "golden retriever with a keyboard" is a published AI metaphor (dev.to, lisapeyton.com). |
| 2 | **I asked my agent to roast itself; it wrote a four-page essay on why it's the best roaster alive.** | **96** | **Chosen** — meta, fresh phrasing (no exact match found), punch at the end. |
| 3 | My agent agrees with me so fast I now ask it questions just to hear somebody say yes. | 87 | Runner-up — original phrasing, but sycophancy is heavily discussed since the April 2025 GPT-4o update. |
| 4 | My agent can explain anything in 500 words or less and somehow always chooses more. | 86 | Kept — clean and tight, but verbosity jokes about AI are common. |
| 5 | My agent's favourite word is 'however', which is how it says no without ever saying it. | 87 | Kept — original phrasing; hedging itself is a well-discussed topic. |
| 6 | My agent calls every idea I have 'a great starting point', then presents it back as its own. | 98 | Runner-up — concrete and visual; punch needs one inference too many. |
| 7 | My agent has read every book ever written and still opens every answer with 'Great question!' | 96 | Rejected — "Great question!" is a documented sycophancy meme (2023 origin). |
| 8 | My agent's memory is perfect, except for everything I told it yesterday. | 79 | Kept — tight, but memory-forgetting is a very common AI complaint. |
| 9 | My agent passed the Turing test and failed the did-you-actually-do-the-thing test. | 83 | Kept — nice parallel structure, but "passed the Turing test" is a stock setup. |
| 10 | My agent treats thinking as a personality trait and answering as optional. | 77 | Rejected — mild observation, no real punch. |

## Referral

Built with [make.fun](https://make.fun/r/f2pdfak6).
