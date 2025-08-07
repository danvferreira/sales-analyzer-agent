from app.loader import load_sales_data
import pandas as pd

def test_load_sales_data():
    df = load_sales_data()
    assert isinstance(df, pd.DataFrame)
    assert not df.empty
