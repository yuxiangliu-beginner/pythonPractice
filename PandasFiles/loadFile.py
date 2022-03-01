import os
print(os.listdir("PandasFiles/supermarkets"))


import pandas
df1 = pandas.read_csv("PandasFiles/supermarkets/supermarkets.csv")
print(df1)

df2 = pandas.read_json("PandasFiles/supermarkets/supermarkets.json")
print(df2)

df3 = pandas.read_excel("PandasFiles/supermarkets/supermarkets.xlsx",sheet_name=0)
print(df3)

df4= pandas.read_csv("PandasFiles/supermarkets/supermarkets-commas.txt")
print(df4)

df5 = pandas.read_csv("PandasFiles/supermarkets/supermarkets-semi-colons.txt",sep=";")
print(df5)

#clear header and cread new header
# df6 = pandas.read_excel("data.txt",header=None)
# df6.columns("Id","Address","City",...)

# set_Index
## only set value, did not change the index
df5.set_index("ID");

## we assign result of set_index to new dataframe, 
# and pass in a variable BOOLEAN : inplace 
##

## select with 2D range
# label base selection
## exclusive (not including end)
# df7 = df.loc[x1:x2,y1:x2];

#index base seletion
## exclusive (not including end)
# df = df.loc[startIndexX1:endIndexX2,indexX1:endIndexY1:endIndexY2]

#deleting index
#drop function not-Inplace
#dr7 = df.drop(name,1) 1 for deleting column
#df7 = df.drop(label,0) 0 fordeleting row

#df 7 = df.drop(df7.columns[0:3],1) deleting column 0 to column 3
# may be not able to delete row

#insert column
#df7.shape - > (row,columns)
# df7.shape[0] -> row
#create row * "" 
#df7.shape[0] * [“","","","",]
#df7["new column name"]=df7.shape[0] * [“","","","",]

#update column 
#df7[”newColumnName] = "some string"

#get rows,
#transpose the dataframe
#df_t = df.T
# editing the column of transpose matrix equals eding the row in original matrix
# transpose back the orignal matrix
#df = df_t。T

#get latitude and longtitude byusing packe geopy
# pip instiall geopy
#import geopy
#dir(geoy)

#pandas method
#apply(function)
#passing function to excute function with each row.
