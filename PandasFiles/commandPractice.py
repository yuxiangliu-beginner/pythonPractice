
import pandas
# pass in list object
df1 = pandas.DataFrame([[2,4,6],[10,20,30]])

print(df1)

df1.columns=["A","B","C"]
df1.index=["first","second"]

print(df1)

# pass in dictionary object
df2 = pandas.DataFrame([{"name":"John","age":"18"},{"name":"jack"}])
print(df2)

#get average of row
print("get mean of df")
print(df1.mean())
print("get mean of mean of df")
print(df1.mean().mean())
print("get mean for column A")
print(df1["A"].mean())
print("get Maximum value ")
print(df1.max())
print("get mean of each row, axis = 0(for column) , axis=1(for row)")
print(df1.mean(axis=1))