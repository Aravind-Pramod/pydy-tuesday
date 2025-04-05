import polars as pl

# Option 2: Read directly from GitHub and assign to an object

pokemon_df = pl.read_csv(
    "https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-04-01/pokemon_df.csv"
)
