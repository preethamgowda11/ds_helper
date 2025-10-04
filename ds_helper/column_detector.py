import pandas as pd
def typeofcolumn(df, num_len=20):
    column_types = {
        "numerical": [],
        "categorical": [],
        "text": []
    }
    for col in df.columns:
        col_type = df[col].dtype
        if col_type == "int64" or col_type == "float64":
            unique_vals = df[col].nunique()
            if unique_vals <= num_len:
                column_types["categorical"].append(col)
            else:
                column_types["numerical"].append(col)
        elif col_type == "object":
            avg_len = df[col].astype(str).str.len().mean()
            if avg_len > 30:
                column_types["text"].append(col)
            else:
                column_types["categorical"].append(col)
        else:
            column_types["categorical"].append(col)
    return column_types