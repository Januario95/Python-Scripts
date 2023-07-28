import os
import json
import PyPDF2
import pandas as pd
import numpy as np
import datetime as dt
from datetime import datetime

filename = 'Extracto-Movimentos de Conta - 3088566881007.xlsx'
df = pd.read_excel(filename)
columns = df.iloc[1:2, :].values[0]
df.columns = columns
df = df.iloc[2:-1, :]
# print(df.head())
def format_date(time):
    return time.replace('-', '/')

def format_float(val):
    try:
        return float(val.replace('-', '').replace(',', '.'))
    except Exception as e:
        return val
    
def to_datetime(date):
    return pd.to_datetime(date, dayfirst=True)


# df['Data'] = df['Data'].apply(format_date)
df = df.replace({'NaN', 0})
df = df.replace({np.nan, 0})
df = df.fillna(0)
df['Data valor'] = df['Data valor'].apply(format_float)
df['Débito'] = df['Débito'].apply(format_float)
df['Crédito'] = df['Crédito'].apply(format_float)
df['Saldo'] = df['Saldo'].apply(format_float)
df[['Débito', 'Crédito', 'Saldo']] = df[['Débito', 'Crédito', 'Saldo']].astype(float)
# print(pd.to_datetime(df['Data'], dayfirst=True))
df['Data'] = df['Data'].apply(to_datetime)
# print(df.columns)

def extract_date(val):
    return val.date()

df['Apenas-Data'] = df['Data'].apply(extract_date)
print(df.head(50))

# for row in df.head().iterrows():
#     print(row[1].values.tolist())

# print(df.head(5))
# df['Data'] = df['Data'].astype(np.datetime64)
# head = df.head(5)
# print(head.values.tolist())
# print(head.to_dict())
# print(json.dumps(json.loads(head.to_json()), indent=4))
# print(df.dtypes)
# print(df['Descrição'].to_frame().head())

# filename = 'Extracto-Standard-operation-proof.pdf'
# file = open(filename, "rb")

# reader = PyPDF2.PdfFileReader(file)
# num_pages = reader.numPages
# page = reader.getPage(0)
# text = page.extractText()
# for row in text.split('\n'):
#     print(row.split())
    
# d = '2023-05-29'
# year, month, day = d.split('-')
# print(dt.date(int(year), int(month), int(day)))