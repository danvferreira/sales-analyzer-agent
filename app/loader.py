import pandas as pd

def load_sales_data(filepath = './dataset/sales.csv'):
    return pd.read_csv(filepath, sep=";", dtype={'product_id': str, 'local': str, 'date': str, 'promotion_type': str })