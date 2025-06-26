from util import load_data, clean_data
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def eda(df):
    plt.figure(figsize=(10,5))
    sns.countplot(data=df, x='year_added', hue='type', palette='tab10')
    plt.xticks(rotation=45); plt.title("Titles Added per Year (Movie vs TV Show)")
    plt.tight_layout(); plt.show()

    genres = df.explode('listed_in')['listed_in']
    plt.figure(figsize=(8,6))
    genres.value_counts().head(10).plot(kind='bar', color='skyblue')
    plt.title("Top 10 Genres"); plt.ylabel("Count")
    plt.tight_layout(); plt.show()

    countries = df.explode('country')['country']
    plt.figure(figsize=(8,6))
    countries[countries != ''].value_counts().head(10).plot(kind='bar', color='coral')
    plt.title("Top 10 Production Countries"); plt.ylabel("Count")
    plt.tight_layout(); plt.show()

    movies = df[df['type']=='Movie']
    plt.figure(figsize=(8,6))
    sns.histplot(movies['duration_int'].dropna(), bins=30, kde=False)
    plt.title("Movie Duration Distribution"); plt.xlabel("Minutes")
    plt.tight_layout(); plt.show()

    tv = df[df['type']=='TV Show']
    plt.figure(figsize=(8,6))
    sns.histplot(tv['duration_int'].dropna(), bins=10, kde=False)
    plt.title("TV Seasons Distribution"); plt.xlabel("Number of Seasons")
    plt.tight_layout(); plt.show()

def top_directors(df):
    dirs = df.dropna(subset=['director']).director.str.split(',').explode().str.strip()
    top5 = dirs.value_counts().head(5)
    print("Top 5 Directors by Content Count:\n", top5)

def run():
    df = load_data()
    df = clean_data(df)
    eda(df)
    top_directors(df)

if __name__ == "__main__":
    run()
