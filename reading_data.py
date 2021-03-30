import pandas as pd

df_open_trans = pd.read_excel('datasets.xlsx', sheet_name='open_transactions')
df_meter_values = pd.read_excel('datasets.xlsx', sheet_name='open_metervalues')


def data_open_trans():
    return df_open_trans


def data_meter_values():
    return df_meter_values
