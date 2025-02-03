# Jane-Street-Real-Time-Market-Data-Forecasting
Entry for Jane Street- Market Data Forecasting. The data consists of multiple features required for market data prediction. The competition dataset comprises a set of timeseries with 79 features and 9 responders.


Operation	Pandas	Polars
Get column as Series	df["grp"]	df["grp"]
Cell indexing by location	df.iloc[1, 1]	df[1, 1]
Row slicing by location	df.iloc[1:3]	df[1:3]
Column slicing by location	df.iloc[:, 1:]	df[:, 1:]
Row indexing by label	df.loc['c']	df.filter(pl.col("index") == "c")
Column indexing by label	df.loc[:, 'x']	df[:, "x"]
 	 	df.select("x")
Column indexing by labels	df.loc[:, ['x', 'z']]	df[:, ['x', 'z']]
 	 	df.select(['x', 'z'])
Column slicing by label	df.loc[:, 'x':'z']	df[:, "x":"z"]
Mixed indexing	df.loc['c'][1]	df.filter(pl.col("index") == "c")[0, 1]
Note: when a query in Pandas returns a single row then that row is returned as a Series. If the row contains both floats and integers then Pandas casts the integers to floats in the Series. Polars returns a DataFrame with one row keeping the original dtypes.

Duplicates and missing values
Operation	Pandas	Polars
Keep unique rows	df.drop_duplicates()	df.unique() [1]
…based a subset of columns	df.drop_duplicates(subset=["ref"])	df.unique(subset=["ref"])
Drop rows with missing values	df.dropna()	df.drop_nulls()
[1] Be aware that in Polars the order of the output from df.unique() is not in general the same as the order of the input. In addition, the default choice of which of each duplicated row to keep is any rather first as in Pandas. I looked at the reasons for this behaviour and how you can control it in this post.

The missing value in Pandas depends on dtype of the column whereas in Polars a missing value is null for all dtypes.

Grouping data and aggregation
Polars has a group_by function to group rows. The following table illustrates some common grouping and aggregation usages. The code snippets are long so scroll horizontally to see Polars.

Operation	Pandas	Polars
Agg by groups	df.groupby('grp')['x'].mean()	df.group_by('grp').agg(pl.col("x").mean()
Agg multiple columns	df.agg({'x': 'max', 'y': 'min'})	df.select([pl.col("x").max(),pl.col("y").min()])
 	df[['x', 'y']].mean()	df.select(["x","y"]).mean()
 	df.filter(regex=("^x")).mean()	df.select(pl.col("^x$").mean()
 	 	df.select(cs.starts_with("x").mean()
Rename column after aggregation	df.groupby('grp')['x'].mean().rename("x_mean")	df.group_by("grp").agg(pl.col("x").mean().name.suffix("_mean"))
Add aggregated data as column	df.assign(x_mean=df.groupby("grp")["x"].transform("mean"))	df.with_column(pl.col("x").mean().over("grp").name.suffix("_mean"))
The output of aggregations in Pandas can be a Series whereas in Polars it is always a DataFrame. Where the output is a Series in Pandas there is a risk of the dtype being changed such as ints to floats.

As noted for unique above be aware that the order of the rows in the output of groupby in Polars is random by default.

Pivoting and unpivoting/melting
Pivoting converts a DataFrame from long to wide format. To go the other way from wide to long format is called unpivoting or melting. | Operation | Pandas | Polars | |————————-|—————————————————————|——————————————–| | Pivot | df.pivot(index="grp", columns="x", values="y") | df.pivot(index="grp", on="x", values="y")| | Unpivot | df_pivot.melt(id_vars="grp", value_name="y") | df_polars_pivot.unpivot(index="grp")|

Polars has moved away from Pandas syntax (e.g. melt becomes unpivot) to have a syntax that is more consistent between pivot and unpivot. In both cases we use the on argument to specify the column to pivot/unpivot on.

The order of the columns in a Polars pivot is random. We can fix this order by passing the sort_columns argument to pivot.

In Pandas the presence of missing values causes the integer values to be cast to float.

Check out the many other posts I’ve written on Polars!

Learn more
Want to know more about Polars for high performance data science and ML? Then you can:

join my Polars course on Udemy
follow me on bluesky
follow me on twitter
connect with me at linkedin
check out my youtube videos
or let me know if you would like a Polars workshop for your organisation.

Operation	Pandas	Polars
Get column as Series	df["grp"]	df["grp"]
Cell indexing by location	df.iloc[1, 1]	df[1, 1]
Row slicing by location	df.iloc[1:3]	df[1:3]
Column slicing by location	df.iloc[:, 1:]	df[:, 1:]
Row indexing by label	df.loc['c']	df.filter(pl.col("index") == "c")
Column indexing by label	df.loc[:, 'x']	df[:, "x"]
 	 	df.select("x")
Column indexing by labels	df.loc[:, ['x', 'z']]	df[:, ['x', 'z']]
 	 	df.select(['x', 'z'])
Column slicing by label	df.loc[:, 'x':'z']	df[:, "x":"z"]
Mixed indexing	df.loc['c'][1]	df.filter(pl.col("index") == "c")[0, 1]
Note: when a query in Pandas returns a single row then that row is returned as a Series. If the row contains both floats and integers then Pandas casts the integers to floats in the Series. Polars returns a DataFrame with one row keeping the original dtypes.

Duplicates and missing values
Operation	Pandas	Polars
Keep unique rows	df.drop_duplicates()	df.unique() [1]
…based a subset of columns	df.drop_duplicates(subset=["ref"])	df.unique(subset=["ref"])
Drop rows with missing values	df.dropna()	df.drop_nulls()
[1] Be aware that in Polars the order of the output from df.unique() is not in general the same as the order of the input. In addition, the default choice of which of each duplicated row to keep is any rather first as in Pandas. I looked at the reasons for this behaviour and how you can control it in this post.

The missing value in Pandas depends on dtype of the column whereas in Polars a missing value is null for all dtypes.

Grouping data and aggregation
Polars has a group_by function to group rows. The following table illustrates some common grouping and aggregation usages. The code snippets are long so scroll horizontally to see Polars.

Operation	Pandas	Polars
Agg by groups	df.groupby('grp')['x'].mean()	df.group_by('grp').agg(pl.col("x").mean()
Agg multiple columns	df.agg({'x': 'max', 'y': 'min'})	df.select([pl.col("x").max(),pl.col("y").min()])
 	df[['x', 'y']].mean()	df.select(["x","y"]).mean()
 	df.filter(regex=("^x")).mean()	df.select(pl.col("^x$").mean()
 	 	df.select(cs.starts_with("x").mean()
Rename column after aggregation	df.groupby('grp')['x'].mean().rename("x_mean")	df.group_by("grp").agg(pl.col("x").mean().name.suffix("_mean"))
Add aggregated data as column	df.assign(x_mean=df.groupby("grp")["x"].transform("mean"))	df.with_column(pl.col("x").mean().over("grp").name.suffix("_mean"))
The output of aggregations in Pandas can be a Series whereas in Polars it is always a DataFrame. Where the output is a Series in Pandas there is a risk of the dtype being changed such as ints to floats.

As noted for unique above be aware that the order of the rows in the output of groupby in Polars is random by default.

Pivoting and unpivoting/melting
Pivoting converts a DataFrame from long to wide format. To go the other way from wide to long format is called unpivoting or melting. | Operation | Pandas | Polars | |————————-|—————————————————————|——————————————–| | Pivot | df.pivot(index="grp", columns="x", values="y") | df.pivot(index="grp", on="x", values="y")| | Unpivot | df_pivot.melt(id_vars="grp", value_name="y") | df_polars_pivot.unpivot(index="grp")|

Polars has moved away from Pandas syntax (e.g. melt becomes unpivot) to have a syntax that is more consistent between pivot and unpivot. In both cases we use the on argument to specify the column to pivot/unpivot on.

The order of the columns in a Polars pivot is random. We can fix this order by passing the sort_columns argument to pivot.

In Pandas the presence of missing values causes the integer values to be cast to float.

Check out the many other posts I’ve written on Polars!

Learn more
Want to know more about Polars for high performance data science and ML? Then you can:

join my Polars course on Udemy
follow me on bluesky
follow me on twitter
connect with me at linkedin
check out my youtube videos
or let me know if you would like a Polars workshop for your organisation.