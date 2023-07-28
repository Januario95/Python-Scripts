import os
import json
import pandas as pd


class ExtractValue:
    def __init__(self, df):
        self.df = df

    def get_value(self, key):
        value = None
        for row in self.df1.itertuples():
            if row.Index == key:
                value = row.Value
        return value

class ClientesSociedadePrenchido(ExtractValue):
    def __init__(self, filename='Ficheiro para o Robot Abertura de contas.xlsx'):
        self.xls = pd.ExcelFile(filename)
        self.df1 = pd.read_excel(self.xls, sheet_name='Clientes Sociedade Prenchido')
        self.df1 = self.df1[['__________________Informacoes dos Documentos de Identificacao_________________',
            'Unnamed: 1', 'Unnamed: 2']]
        self.df1 = self.df1.iloc[1:94, :]
        self.df1 = self.df1.rename(columns={
        '__________________Informacoes dos Documentos de Identificacao_________________': 'Name',
        'Unnamed: 1': 'Value', 'Unnamed: 2': 'Meaning'
        })
        self.df1.set_index('Name', inplace=True)

    
class ContasSociedadeConstituidaPr(ExtractValue):
    def __init__(self, filename='Ficheiro para o Robot Abertura de contas.xlsx'):
        self.xls = pd.ExcelFile(filename)
        df1 = pd.read_excel(self.xls, sheet_name='Contas Sociedade Constituida Pr')
        last_col = df1.columns[-1]
        new_row = {
            'Name': df1.columns[0],
            'Value': df1.columns[-1]
        }
        df1 = df1.rename(columns={
            'No. do Cliente': 'Name',
            last_col: 'Value'
        })
        df1 = df1.iloc[1:21, :]
        df1.append(new_row, ignore_index=True)
        self.df1 = df1
        self.df1.set_index('Name', inplace=True)


# df = ClientesSociedadePrenchido()
# # print(df.extract_value())
# # print(df.get_value('GB # Nome:'))

df = ContasSociedadeConstituidaPr()
# print(df.extract_value())
print(df.get_value('GB # Nome:'))

filename = 'Ficheiro para o Robot Abertura de contas.xlsx'

xls = pd.ExcelFile(filename)
df1 = pd.read_excel(xls, 'Cliente Em Nome Individual Pren')
# print(df1)


# df3 = pd.read_excel(xls, 'Contas Sociedade Constituida Pr')
# last_col = df3.columns[-1]
# new_row = {
#     'Name': df3.columns[0],
#     'Value': df3.columns[-1]
# }
# df3 = df3.rename(columns={
#     'No. do Cliente': 'Name',
#     last_col: 'Value'
# })
# df3 = df3.iloc[1:21, :]
# # print(df3.columns.values)
# # print(df3.head())

# df3 = df3.append(new_row, ignore_index=True)
print(df3)
# print(row1_col1)
# row1 = df3.iloc[:1, :]
# print(row1.loc[:1, 'No. do Cliente'])
# print(df3.columns)