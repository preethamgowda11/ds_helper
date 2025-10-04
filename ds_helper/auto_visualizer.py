import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from .column_detector import typeofcolumn 

def visualize(df, num_len=20):
    column_types = typeofcolumn(df, num_len)
    for col, col_type in column_types.items():
        print(f"\nColumn: {col} → {col_type}")

        if col_type == "numerical":
            plt.hist(df[col].dropna(), bins=10, color="skyblue", edgecolor="black")
            plt.title(f"Histogram of {col}")
            plt.xlabel(col)
            plt.ylabel("Frequency")
            plt.show()
            plt.scatter(df.index, df[col], color="green")
            plt.title(f"Scatter Plot of {col} vs Index")
            plt.xlabel("Index")
            plt.ylabel(col)
            plt.show()
            plt.boxplot(df[col].dropna())
            plt.title(f"Boxplot of {col}")
            plt.ylabel(col)
            plt.show()
        elif col_type == "categorical":
            counts = df[col].value_counts()
            counts.plot(kind="bar", color="orange")
            plt.title(f"Bar Chart of {col}")
            plt.xlabel(col)
            plt.ylabel("Count")
            plt.show()
            counts.plot(kind="barh", color="purple")
            plt.title(f"Count Plot of {col}")
            plt.xlabel("Count")
            plt.ylabel(col)
            plt.show()
        elif col_type == "text":
            text_data = " ".join(df[col].dropna().astype(str))
            if text_data.strip():
                wordcloud = WordCloud(width=600, height=400, background_color="white").generate(text_data)
                plt.imshow(wordcloud, interpolation="bilinear")
                plt.axis("off")
                plt.title(f"Word Cloud for {col}")
                plt.show()
            words = text_data.split()
            freq = {}
            for word in words:
                freq[word] = freq.get(word, 0) + 1
            top_words = dict(sorted(freq.items(), key=lambda x: x[1], reverse=True)[:10])
            plt.bar(top_words.keys(), top_words.values(), color="red")
            plt.title(f"Top 10 Word Frequencies in {col}")
            plt.xticks(rotation=45)
            plt.show()
        else:
            print(f"Skipping {col} (unsupported type).")
