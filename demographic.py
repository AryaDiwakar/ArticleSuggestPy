import pandas as pd 
import munpy as np 
df=pd.read_csv("articles.csv")
df=df.sort_values(["total_events"])
output = df[['url', 'title', 'lang', 'total_events']].head(20).values.tolist()
