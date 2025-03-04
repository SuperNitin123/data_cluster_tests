# Pandas Data Frame Analysis

import pandas as pd

# pandas Head and tail
data={'name':['aamir','nitin','john','Alice','Bob','Mike'],
      'Age':[32,54,64,24,34,56],
      'city':['New Delhi','Noida','Hyderabad','New York','Puna','Bombay']}

df=pd.DataFrame(data)

#display first 3 rows
print('First 3 Rows: ')
print(df.head(3))
print()
#display first 5 rows
print('First 5 Rows: ')
print(df.head())


#display last 3 rows
print('Last 3 Rows: ')
print(df.tail(3))
print()
#display last 5 rows
print('Last 5 Rows: ')
print(df.tail())


# add column and row
data={'name':['aamir','nitin','john','Alice','Bob','Mike'],
      'Age':[32,54,64,24,34,56],
      'city':['New Delhi','Noida','Hyderabad','New York','Puna','Bombay']}

df=pd.DataFrame(data)

# new list
add=['New Delhi','Noida','Hyderabad','New York','Puna','Bombay']
df['Address']=add
print(df)

#new row
df.loc[len(df.index)]=['ML Eng','Data Analys','BIT','VL']
print(df)

# delete column and row
data={'name':['aamir','nitin','john','Alice','Bob','Mike'],
      'Age':[32,54,64,24,34,56],
      'city':['New Delhi','Noida','Hyderabad','New York','Puna','Bombay']}

df=pd.DataFrame(data)

print(df)

print()

# delete 4 index
df.drop(4,inplace=True)
print(df)
print()

# delete city column
df.drop('city',axis=1,inplace=True)
print(df)
print()

# delete age
df.drop(columns='Age',inplace=True)
print(df)
print()

# delete row with index 1 and 3
df.drop([1,3],axis=0,inplace=True)
print(df)

# rename labels
data={'name':['aamir','nitin','john','Alice','Bob','Mike'],
      'Age':[32,54,64,24,34,56],
      'city':['New Delhi','Noida','Hyderabad','New York','Puna','Bombay']}

df=pd.DataFrame(data)
print(df)
print()

#rename column 'name' to 'first_name'
df.rename(columns={'name':'first_name'},inplace=True)
print(df)
print()

df.rename(mapper={'Age':'Number','city':'Town'},axis=1,inplace=True)
print(df)
print()

#rename column one index lable
df.rename(index={0:'s.no'},inplace=True)
print(df)
print()
#rename column multiple index lable
df.rename(mapper={1:100,2:200},axis=0,inplace=True)
print(df)

#.loc
data={'name':['aamir','nitin','john','Alice','Bob','Mike'],
      'Age':[32,54,64,24,34,56],
      'city':['New Delhi','Noida','Hyderabad','New York','Puna','Bombay']}

df=pd.DataFrame(data)
names=df['name']
print(names)
print()


name_city=df[['name','city']]
print(name_city)
print()

#slice
slice_rows=df.loc[1:3]
print("Sliced rows")
print(slice_rows)
print()

#boolean index with .loc
boolen_index=df.loc[df['Age']>35]
print("Boolean index")
print(boolen_index)
print()

#.iloc
data={'name':['aamir','nitin','john','Alice','Bob','Mike'],
      'Age':[32,54,64,24,34,56],
      'city':['New Delhi','Noida','Hyderabad','New York','Puna','Bombay']}

df=pd.DataFrame(data)

#single_row
single_row=df.iloc[2]
print(single_row)
print()

#multiple_row
multiple_row=df.iloc[[0,2,4]]
print(multiple_row)
print()

#specific vlaue
specific=df.iloc[1,0]
print(specific)
print()

#slice
slice_rows=df.iloc[1:3]
print("Sliced rows")
print(slice_rows)
print()

# select
data={'name':['aamir','nitin','john','Alice','Bob','Mike'],
      'Age':[32,54,64,24,34,56],
      'city':['New Delhi','Noida','Hyderabad','New York','Puna','Bombay']}

df=pd.DataFrame(data)
print(df)
print()
selected_data_loc=df.loc[df['Age']>35,'name']
print(selected_data_loc)
print()
selected_data_iloc=df.iloc[(df['Age']>35).values,0]
print(selected_data_iloc)
print()

selected_data_loc=df.loc[1:3,['name','Age']]
print(selected_data_loc.to_string(index=False))
print()

selected_rows=df[df['Age']>35]
print(selected_rows)
print()

selected_rows=df.query('Age>35')
print(selected_rows)
print()

filter_name=['aamir','nitin']
selected_rows=df[df['name'].isin(filter_name)]
print(selected_rows)
print()

#pandas multiple index

data={"Continent":["North America","Europe","Asia","North America","Europe","Asia","North America","Europe","Asia","Asia"],
      "Country":["United States","Germany","China","Canada","Japan","France","Maxico","India","United Kingdon","Nepal"],
      "Population":[331002651,837564,14345643,3777543,126543,652754,128932786,138000,671600,2987659]}
df=pd.DataFrame(data)
print(df, '\n')

#sort dataframe from dict
df.sort_values('Continent',inplace=True)

#create a multiindex
df.set_index(['Continent','Country'],inplace=True)
print(df)
print()

# access asia
asia=df.loc['Asia']

#access Canada
canada=df.loc['North America','Canada']

print('Asian\n',asia)
print('Canada\n',canada)
print()

# Mulitiple Index From Arrays

#create Array
Continent=["North America","Europe","Asia","North America","Europe","Asia","North America","Europe","Asia","Asia"]
Country=["United States","Germany","China","Canada","Japan","France","Maxico","India","United Kingdon","Nepal"]
Population=[331002651,837564,14345643,3777543,126543,652754,128932786,138000,671600,2987659]

#create array from arrays
index_arr=[Continent,Country]

#multiindex from array
multi_index=pd.MultiIndex.from_arrays(index_arr,names=['Continent','Country'])

#create dataframe from multiindex
df=pd.DataFrame({'Population':Population},index=multi_index)
print(df)


data={'Date':["2023-01-01","2023-01-01","2023-01-02","2023-01-02"],
      'City':['New York','Los Angles','New York','Los Angles'],
      'Temperature':[32,45,30,49],
      'Humidity':[80,10,89,5]}

df=pd.DataFrame(data)
print(df,'\n')

#pivot from dataframe
pivot_df=df.pivot(index='Date',columns='City',values='Temperature')
print(pivot_df,'\n')

#pivot from dataframe multindex
pivot_df=df.pivot(index='Date',columns='City')
print(pivot_df)

#pivot table
pivot_table=df.pivot_table(index='Date',columns='City')
print(pivot_table)
