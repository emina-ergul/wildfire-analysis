import pandas as pd
import geopandas as gpd
from pathlib import Path

data_dir = Path("data/raw")


def load_csv_data(filename="events.csv"):
    df = pd.read_csv(data_dir / filename)

    print(df.head())
    print(df.columns)
    return df


load_csv_data()
