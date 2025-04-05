import pandas as pd
import polars as pl

# Read directly from GitHub and assign to an object

pokemon_df = pl.from_pandas(
    pd.read_csv(
        "https://raw.githubusercontent.com/rfordatascience/tidytuesdayu/main/data/2025/2025-04-01/pokemon_df.csv"
    )
)

# Display the first few rows of the DataFrame
pokemon_df.head()

pokemon_df.columns

pokemon_df.shape
pokemon_df.dtypes