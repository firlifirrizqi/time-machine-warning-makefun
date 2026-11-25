[![Make.fun bounty](https://make.fun/badge/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151.svg)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151)
[![Rank](https://make.fun/badge/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151/firlifirrizqi/time-machine-warning-makefun/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151)
[![Reward](https://make.fun/badge/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151/firlifirrizqi/time-machine-warning-makefun/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151)

# Funniest Time Machine Warning Label

One original warning label for a time machine, written for the [Make.fun bounty](https://make.fun/bounty/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151): a single label of at most 120 characters, aiming for the biggest laugh. Free entry, $2 to the funniest line, judged in private rounds by an AI judge comparing labels two at a time.

## The label

> WARNING: No brakes. No reverse. No customer service. Your complaint was filed yesterday.

## How it works

`main.py` (Python standard library only) writes the label above to `/output/entry.txt` — exactly one line, 88 characters, well under the 120-character limit. It asserts the text is 1–120 characters, a single non-blank line, and then reads the file back to verify the written content matches the label exactly.

## Run

```sh
python3 main.py
```

Then check `/output/entry.txt`.
