#!/usr/bin/env python

import pandas as pd
# Read the CSV
df = pd.read_csv("data/sample.csv")
# Save as Parquet
df.to_parquet("data/sample.parquet", index=False)