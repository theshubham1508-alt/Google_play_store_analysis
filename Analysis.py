import pandas as pd
df = pd.read_csv("google play store.csv")
print(df.shape)
print(df.head)

#dataset overview
import pandas as pd
df = pd.read_csv("google play store.csv")
print("shape:",df.shape)
print("\ncolomns:")
print(df.columns)
print("\nInfo:")
print(df.info())

#missing values
import pandas as pd
df = pd.read_csv("google play store.csv")
print(df.isnull().sum())

#Duplicate rows
import pandas as pd
df = pd.read_csv("google play store.csv")
print(df.duplicated().sum())

# Top 5 categories
import pandas as pd
df = pd.read_csv("google play store.csv")
print(df["Category"].value_counts().head())


#handle a missing value
import pandas as pd
df = pd.read_csv("google play store.csv")

df["Rating"] = df["Rating"].fillna(df["Rating"].mean())

df["Type"] = df["Type"].fillna(df["Type"].mode()[0])

df["Content Rating"] = df["Content Rating"].fillna(
    df["Content Rating"].mode()[0]
)
df["Current Ver"] = df["Current Ver"].fillna("Unknown")

df["Android Ver"] = df["Android Ver"].fillna("Unknown")

print(df.isnull().sum())

# Handle a duplicat value
import pandas as pd
df = pd.read_csv("google play store.csv")
df = df.drop_duplicates()
print(df.duplicated().sum())


#check database size 
import pandas as pd
df = pd.read_csv("google play store.csv")
print(df.shape)

#top 5 Category
import pandas as pd
df = pd.read_csv("google play store.csv")
print(df["Category"].value_counts().head())


# Average rating
import pandas as pd
df = pd.read_csv("google play store.csv")
print(df["Rating"].mean())

#Top Rated App 
import pandas as pd
df = pd.read_csv("google play store.csv")
print(df.sort_values("Rating",ascending = False) [["App","Rating"]].head())
print(df["Rating"].max())

# Free  Vs Paid App
import pandas as pd
df = pd.read_csv("google play store.csv")
print(df["Type"].value_counts())

#rating describe
import pandas as pd
df = pd.read_csv("google play store.csv")
print(df["Rating"].describe())


#graph for rating distribution
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("google play store.csv")
df["Rating"].hist()
plt.title("Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Count")
plt.show()

#graph for to 5 categories (Bar Chart)
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("google play store.csv")
df["Category"].value_counts().head().plot(kind = "bar")
plt.title("Top 5 Category")
plt.xlabel("Categoty")
plt.ylabel("Count")
plt.show()

# Which category has the most app
import pandas as pd
df = pd.read_csv("google play store.csv")
print(df["Category"].value_counts().head(10))

#graph
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("google play store.csv")
print(df["Category"].value_counts().head(10).plot(kind = "bar"))
plt.title("Top 10 Categories")
plt.show()


#Category wise Average Rating
import pandas as pd
df = pd.read_csv("google play store.csv")
print(
    df.groupby("Category")["Rating"].mean().sort_values(ascending = False).head(10)
)

# graph
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("google play store.csv")

df.groupby("Category")["Rating"]\
.mean()\
.sort_values(ascending=False)\
.head(10)\
.plot(kind="bar")

plt.title("Top 10 Categories by Average Rating")
plt.xlabel("Category")
plt.ylabel("Average Rating")
plt.show()


import pandas as pd
df = pd.read_csv("google play store.csv")
df = df[df["Rating"] <=5]
print(df["Rating"].max())

# Invalid rating remove
import pandas as pd

df = pd.read_csv("google play store.csv")
df = df[df["Rating"] <= 5]

print(
    df.groupby("Category")["Rating"]
      .mean()
      .sort_values(ascending=False)
      .head(10)
)