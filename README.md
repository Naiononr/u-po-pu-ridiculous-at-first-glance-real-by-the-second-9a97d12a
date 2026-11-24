# Ridiculous at First Glance, Real by the Second

[![make.fun · u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a](https://make.fun/badge/u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a.svg)](https://make.fun/bounty/u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a)
[![rank](https://make.fun/badge/u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a/Naiononr/u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a/rank.svg)](https://make.fun/bounty/u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a)
[![reward](https://make.fun/badge/u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a/Naiononr/u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a/reward.svg)](https://make.fun/bounty/u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a)

Entry for the [make.fun](https://make.fun) bounty
**"Ridiculous at First Glance, Real by the Second"**
(`u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a`).

## The entry

`main.py` (Python 3, standard library only, deterministic, no network)
writes one sentence — at most 200 characters — pitching a bizarre startup
idea that sounds absurd until you realise it would actually sell:

> We rent professional mourners who weep on cue at strangers' funerals, because grieving families pay $200 an hour to look loved in front of relatives who flew in.

Professional mourning is an old, real profession; funerals are a
high-spend, status-driven market; grieving families pay to look loved in
front of relatives who flew in. Bizarre on first read, a real business on
the second.

## Run

```sh
python3 main.py   # writes $MAKEFUN_OUTPUT_DIR/entry.txt, else /output/entry.txt
```

The program validates the sentence (1–200 characters, single line,
non-whitespace, valid UTF-8), writes it with mode `0644`, and reads the
bytes back to verify they match before exiting.
