
import numpy as np
import pandas as pd


'''
BASIC SERIES AND DATAFRAME CREATION
'''

ser_no_index = pd.Series([9,0,7,8,3])

index = ['a','b','c','d']
vals = ['100','3.14','2.71','32']

ser = pd.Series(vals, index)

kvp = {'a':'adam', 'b':'bob', 'c':'chris', 'd':'dan', 'e':'evan'}

ser_from_dict = pd.Series(kvp)

new_idx = [i for i in range(1,101,2)]

np_arr_2d = [[11,12,13,14],
            [25,26,27,28]]

df_2d = pd.DataFrame(np_arr_2d)

transposed = np.transpose(np_arr_2d)

df_transposed = pd.DataFrame(transposed)

#convert df back into numpy array
df_to_arr = dr_2d.values



'''
INDEX AND COLUMN ORDER/LABEL MANIPULATION
'''

#use a column as the index
def first_col_as_index(df, index):
    col = index[0]
    df.set_index(col)
    df.index.name = None #removes name (original column heading)
    return df

def use_original_index(df):
    df.reset_index() 
    #df.reset_index(drop=True) #drop/delete the column that was serving as index

def change_to_new_index(df, vals):
    df_reindex = df.reindex(vals) #cannot reindex inplace
    return df_reindex

def rename_columns(df, name_dict): #use a dictionary {'old_col': 'new_col'}
    df.rename(columns=name_dict, inplace=True)
    return df

    #single column
    #df.rename(columns={'original':'new'}, inplace=True) 

def rename_cols_with_lambda(df):
    df.rename(columns=lambda x: x.strip(), inplace=True) #remove padding
    return df

def change_column_headings(df, headings):
    df.columns = headings #list method; key:val is better practice



def change_column_order(df, ordered_columns):
    df_ordered_cols = df.reindex(columns=ordered_columns)
    return df_ordered_cols


'''
DATAFRAME OPERATIONS
'''

seed = np.random.randint(0,100,16)

eight_two = seed.reshape(8,2)  #pd.series cannot be reshaped
two_eight = seed.reshape(2,8)
four_four = pd.DataFrame(seed.reshape(4,4))

df4 = four_four

disciplines = ['Math', 'History', 'English', 'Science']
students = ['A', 'B', 'C', 'D']

df4['Students'] = students
df4.set_index('Students', inplace=True)
df4.columns = disciplines

#retrieve row
iloc_0 = df4.iloc[0] #integer index, returns row 
loc_0 = df4.loc['A'] #named index returns row

#retrieve column
col_0 = df4['Math']

#store a copy to do operations on it
df5 = df4.copy()

#append column
df5['E'] = np.random.randint(0,100,4)

#append row
df5.loc['E'] = np.random.randint(0,100,5)

#rename column
df5.rename(columns={'E':'Music'}, inplace=True)

#sort by column
df5.sort_values('Music', axis=0, ascending=False)

#append row using append method
append_df1 = pd.DataFrame([[1,2],[13,14]],columns=['Alpha','Beta'])
append_df2 = pd.DataFrame([[35,36],[47,48]],columns=['Alpha','Beta'])

def append_dataframes(df1, df2):
    df1 = df1.append(df2)
    #df1.append(df2, ignore_index=True) #ignore second df's index
    return df1

#mean and standard dev
df['Student Overall'] = df.mean(axis=1)
subject_means = df.mean(axis=0)

#dealing with null data
df.isnull() #booleans
df.isnull().sum() #nulls by column
df.isnull().sum()sum() #nulls in the entire df

df['row'] = df['row'].fillna(0) #replace NaN with zero
df = df.dropna(axis=0) #remove all rows with NaN



#classify data into bins
bins = [0,25,50,75,100]
names = ['Fourth quartile', 'Third quartile', 'Second quartile','First quartile']

def create_bins(df, bins, labels):
    binned_df = pd.cut(df, bins, labels=names)
    return binned_df

#select row with max/min in column
def get_col_max(df, column):
    return df.loc[df[column].idxmax()]

def get_col_min(df, column):
    return df.loc[df[column].idxmin()]


'''
RESTRUCTURING DATAFRAMES
'''



#append dataframe one row at a time using one concat
'''append creates a new copy of dataframe every time, so for performance reasons it is bettr to prepare a list of lists or list of dicts beforehand to seed the dataframe'''
def concat_dataframe(df1, new_data):
    cols = new_data[0]
    df_new = []

    for row in new_data[1:]:
        
        next_dict = {}
        for i in len(row):
            next_dict.update({cols[i] = row[i]})

        df_new.append(next_dict)

    return df1.concat(pd.DataFrame(df_new, ignore_index=True))



def get_head(mx, n): #series and df only; np array invalid
    return mx.head(n)


def melt_columns():
    pass


def pivot_table():
    pass



if __name__ == "__main__":
    print("Kung fu pandas")

    #print('Series head: \n', ser_from_dict.head(2))

    print('Seed:\n', seed)