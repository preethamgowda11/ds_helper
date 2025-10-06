# ds_helper
A Python library with tools for column type detection, data visualization, and text cleaning.

## Features
- Detects column types in a DataFrame (numerical, categorical, text)
- Automatically visualizes data based on column type
- Cleans text data by removing punctuation, filler words, and stopwords

## Installation
Clone the repository and install locally:

```sh
git clone https://github.com/preethamgowda11/ds_helper.git
cd ds_helper
pip install .
```

## Usage
```python
import pandas as pd
from ds_helper import typeofcolumn, visualize, TextCleaner

# Example DataFrame
df = pd.read_csv("your_data.csv")

# Detect column types
print(typeofcolumn(df))

# Visualize data
visualize(df)

# Clean text
cleaner = TextCleaner()
cleaned_text = cleaner.clean("Um, I think this is, like, a sample sentence!")
print(cleaned_text)
```

## Requirements
- pandas
- matplotlib
- seaborn
- wordcloud
- nltk
