import pandas as pd
import numpy as np
from pathlib import Path
from difflib import SequenceMatcher
import matplotlib.pyplot as plt

# ============================

# SETTINGS

# ============================

SIM_THRESHOLD = 0.70

LINKERS = [
"GPGPG",
"EAAAK"
]

SEQ_MAP = {
1: "BZLF1",
2: "EBNA1",
3: "EBNA1_2",
4: "gB",
5: "gH",
6: "GP350",
7: "gp42",
8: "LMP1",
9: "LMP1_2",
10: "LMP2",
11: "LMP2_2"
}

# ============================

# FUNCTIONS

# ============================

def similarity(a, b):
return SequenceMatcher(
None,
str(a),
str(b)
).ratio()

def find_linkers(peptide):

```
peptide = str(peptide)

matches = []

for linker in LINKERS:

    if linker in peptide:

        matches.append(linker)

if matches:

    return ";".join(matches)

return None
```

def classify(
peptide,
intended
):

```
peptide = str(peptide)

if peptide in intended:

    return (
        "Intended",
        None
    )

for p in intended:

    if (
        similarity(
            peptide,
            p
        )
        >=
        SIM_THRESHOLD
    ):

        return (
            "Redundant Intended",
            None
        )

linker = find_linkers(
    peptide
)

if linker:

    cleaned = peptide

    for l in LINKERS:

        cleaned = cleaned.replace(
            l,
            ""
        )

    if cleaned.strip() == "":

        return (
            "Linker-only",
            linker
        )

    return (
        "Junction-derived",
        linker
    )

return (
    "Novel",
    None
)
```

def read_file(path):

```
if (
    str(path)
    .endswith(
        ".tsv"
    )
):

    return pd.read_csv(
        path,
        sep="\t"
    )

return pd.read_csv(
    path
)
```

# ============================

# LOAD FILES

# ============================

frames = []

for ext in [
"*.csv",
"*.tsv"
]:

```
for f in Path(".").glob(ext):

    name = (
        f.name
        .lower()
    )

    if (
        "mhc"
        not in name
        and
        "bcell"
        not in name
    ):

        continue

    try:

        df = read_file(
            f
        )

    except Exception as e:

        print(
            "Skipping",
            f,
            e
        )

        continue

    seq_col = None

    for c in df.columns:

        if (
            "seq"
            in
            c.lower()
        ):

            seq_col = c

            break

    if (
        seq_col
        is None
    ):

        continue

    if (
        "peptide"
        not in df.columns
    ):

        continue

    df = df.rename(
        columns={
            seq_col:
            "seq_num"
        }
    )

    df[
        "source"
    ] = f.name

    frames.append(
        df
    )
```

if (
len(
frames
)
==
0
):

```
raise Exception(
    "\nNo valid MHCI/MHCII/Bcell files found.\n"
)
```

data = pd.concat(
frames,
ignore_index=True
)

print(
"\nLoaded rows:",
len(data)
)

# ============================

# BUILD INTENDED SET

# ============================

intended = {}

for seq in sorted(
data[
"seq_num"
]
.unique()
):

```
subset = data[
    data[
        "seq_num"
    ]
    ==
    seq
]

keep = []

for peptide in subset[
    "peptide"
]:

    peptide = str(
        peptide
    )

    duplicate = False

    for x in keep:

        if (
            similarity(
                peptide,
                x
            )
            >=
            SIM_THRESHOLD
        ):

            duplicate = True

            break

    if not duplicate:

        keep.append(
            peptide
        )

intended[
    seq
] = keep
```

# ============================

# CLASSIFICATION

# ============================

rows = []

for _, r in data.iterrows():

```
seq = int(
    r[
        "seq_num"
    ]
)

peptide = str(
    r[
        "peptide"
    ]
)

cls, linker = classify(
    peptide,
    intended[
        seq
    ]
)

rows.append({

    "seq_num":
        seq,

    "protein":
        SEQ_MAP.get(
            seq,
            "Unknown"
        ),

    "peptide":
        peptide,

    "classification":
        cls,

    "linker":
        linker,

    "source_file":
        r[
            "source"
        ]

})
```

detail = pd.DataFrame(
rows
)

# ============================

# SUMMARY

# ============================

summary = (
detail
.groupby(
[
"seq_num",
"protein",
"classification"
]
)
.size()
.unstack(
fill_value=0
)
)

needed = [

```
"Intended",

"Redundant Intended",

"Junction-derived",

"Linker-only",

"Novel"
```

]

for c in needed:

```
if c not in summary:

    summary[
        c
    ] = 0
```

den = (

```
summary[
    "Intended"
]

+

summary[
    "Junction-derived"
]

+

summary[
    "Novel"
]
```

)

summary[
"junction_burden"
] = np.where(

```
den > 0,

summary[
    "Junction-derived"
]
/
den,

0
```

)

summary = (
summary
.reset_index()
)

# ============================

# EXPORT

# ============================

detail.to_csv(

```
"junction_detail.csv",

index=False
```

)

summary.to_csv(

```
"junction_summary.csv",

index=False
```

)

linkers = (

```
detail[
    detail[
        "linker"
    ]
    .notna()
]

.groupby(
    "linker"
)

.size()

.reset_index(
    name="count"
)
```

)

linkers.to_csv(

```
"linker_summary.csv",

index=False
```

)

# ============================

# PLOTS

# ============================

plot_cols = [

```
"Intended",

"Redundant Intended",

"Junction-derived",

"Linker-only",

"Novel"
```

]

summary.set_index(

```
"protein"
```

)[

```
plot_cols
```

].plot(

```
kind="bar",

stacked=True,

figsize=(12, 7)
```

)

plt.tight_layout()

plt.savefig(

```
"epitope_categories.png",

dpi=300
```

)

plt.close()

summary.plot(

```
x="protein",

y="junction_burden",

kind="bar",

figsize=(10, 6)
```

)

plt.tight_layout()

plt.savefig(

```
"junction_burden.png",

dpi=300
```

)

plt.close()

print(
"\nDONE\n"
)

print(
summary
)
