#  %%
import polars as pl

input_df = pl.read_csv(
    "https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-03-18/palmtrees.csv",
    encoding="windows-1252",
)

input_df.describe()

# %%
input_df.select("spec_name").unique()

# %%
