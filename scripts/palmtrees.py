import polars as pl
import altair as alt
import seaborn as sns

input_df = pl.read_csv(
    "https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-03-18/palmtrees.csv",
    encoding="windows-1252",
)

input_df.describe()

# Columns imported as strings, converting NA to null.
input_df = input_df.with_columns(pl.col(pl.String).replace("NA", None))

# Converting all numeric columns.
schema = {
    "max_stem_height_m": pl.Float32,
    "max_stem_dia_cm": pl.Float32,
    "max_leaf_number": pl.Int32,
    "max__blade__length_m": pl.Float32,
    "max__rachis__length_m": pl.Float32,
    "max__petiole_length_m": pl.Float32,
    "average_fruit_length_cm": pl.Float32,
    "min_fruit_length_cm": pl.Float32,
    "max_fruit_length_cm": pl.Float32,
    "average_fruit_width_cm": pl.Float32,
    "min_fruit_width_cm": pl.Float32,
    "max_fruit_width_cm": pl.Float32,
}

input_df = input_df.cast(schema)

alt.Chart(input_df).mark_point().encode(
    x="max_stem_dia_cm", y="max_fruit_length_cm", color="spec_name"
).interactive()


# sns.pairplot(input_df.to_pandas(), hue="spec_name")

alt.Chart(input_df).mark_bar().encode(
    alt.X("palm_tribe").title("palm_tribe"),
    alt.Y("mean(max_stem_dia_cm)").title("Mean Stem Diameter"),
)

#  text = bar.mark_text(
#     #align="left",
#     baseline="middle",
#     dx=3
# ).encode(text="mean(max_stem_dia_cm)")

# bar+text

alt.Chart(input_df).mark_bar().encode(
    alt.X("fruit_shape").title("palm_tribe"),
    alt.Y("mean(max_fruit_length_cm)").title("Stem Diameter"),
)

input_df.filter(pl.col("max_fruit_length_cm").is_null())
