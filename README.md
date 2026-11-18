# GreekNumbers

Converts arbitrarily large integers into **Greek numerals** written in the
classical myriad system, and renders them as LaTeX-style math so they can be
displayed in Markdown.

## Background

Greek numerals use 27 letters: units (α–θ, with ϛ for 6), tens (ι–ϙ) and
hundreds (ρ–ϡ). Thousands reuse the unit letters with a lower-left mark (`͵`,
written here as a backtick). Numbers past 9,999 are grouped into **myriads**
(10,000s), written with an M and the multiplier above it. This program extends
that idea recursively: myriads of myriads are tracked as numbered *periods*,
and very large numbers move up to higher *orders*, so any integer Python can
hold can be written out.

## Usage

```bash
python greekNum.py
```

The script converts a few example numbers and writes each result as a `.MD`
file containing a `$...$` math expression:

| File | Number |
|---|---|
| `computeTime.MD` | 200,000,000 |
| `handprime.MD` | 20,988,936,657,440,586,486,151,264,256,610,222,593,863,921 (Ferrier's prime, the largest prime found without a computer) |
| `largeFactor.MD` | 340,282,366,939,463,463,374,607,431,768,211,457 |

To convert your own number, add a line at the bottom of `greekNum.py`:

```python
write(convert(123456789), "example")   # writes example.MD
```

The Mersenne prime 2^136,279,841 − 1 is included as a commented-out example;
it works but is very slow.

Progress is printed for long inputs, since numbers with millions of digits
take a long time.
