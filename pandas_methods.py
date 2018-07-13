
import numpy as np
import pandas as pd

index = ['a','b','c','d']
vals = ['100','3.14','2.71','32']

ser = pd.Series(vals, index)

ser_no_index = pd.Series([9,0,7,8,3])

df = pd.DataFrame(np.random.randn(50))

new_idx = [i for i in range(1,101,2)]

'''
Index and Column Manipulation
'''

#use a column as the index
def first_col_as_index(df, index):
    col = index[0]
    df.set_index(col)
    df.index.name = None #removes name (original column heading)
    return df

def use_original_index(df):
    df.reset_index() 
    #df.reset_index(drop=True) #deletes column

def change_to_new_index(df, vals):
    df_reindex = df.reindex(vals) #cannot reindex inplace
    return df_reindex

def rename_columns(df, name_dict): #use a dictionary {'old_col': 'new_col'}
    df.rename(columns=name_dict, inplace=True)
    return df

def rename_cols_with_lambda(df):
    df.rename(columns=lambda x: x.strip(), inplace=True) #remove padding
    return df

def change_column_headings(df, headings):
    df.columns = headings #list method; key:val is better practice


def change_column_order(df, ordered_columns):
    df_ordered_cols = df.reindex(columns=ordered_columns)
    return df_ordered_cols



if __name__ == "__main__":
    print("Kung fu pandas")