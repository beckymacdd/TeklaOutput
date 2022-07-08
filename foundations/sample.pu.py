
import pandas as pd

# %% [markdown]
# ```I am formatting osome code for a tutorial```

# %% [markdown]
# <!-- hello  -->

# %% [markdown]
# 

# %%
df = pd.read_csv("Calcs.csv")

# %%
df.head(10)

# %%

df1 = pd.read_csv("Strength.csv",header = 6, 
usecols=[0,6,7,8,9,10,11],
na_values="-"
)
df1.rename(columns={"Unnamed: 0": "Support", "Fvert\n[kN]":"Fv", "Fmajor\n[kN]":"Fy","Fminor\n[kN]":"Fx","Mmajor\n[kNm]":"My","Mminor\n[kNm]":"Mx","Mtor\n[kNm]":"Mtor"}, inplace=True)
df1.Support = df1.Support.fillna(0)


df1

# %%
# Everytime row in "Support" = NaN, row = [i-1,'Support'] -> if 

# df1.Support = NaN, df1 = df1[i-1,'Support']
for i in range (1,len(df1)):
    if df1.loc[i, 'Support'] == 0:
        df1.loc[i, 'Support'] = df1.loc[i-1, 'Support'] 

df1.set_index('Support', inplace=True)
df1.head()

# Finding maximum value for each column, make new table with the values and show what support is associated with it 
max_index = df1.Fv.idxmax()
print(max_index)
index_list = []
for column in df1.columns:
    print(column)
    if column == 'Fv':
        index_list.append((column,df1[column].idxmin(),df1[column].min()))
    else:
        index_list.append((column,df1[column].abs().idxmax(),df1[column].abs().max()))
    
    

df1.columns
index_list

# %%
summary_df = pd.DataFrame()
for entry in index_list:
    tempdf = df1.loc[entry[1]]
    summary_df = summary_df.append(tempdf)
# summary_df.append(tempdf)
summary_df

# %%
# Finding maximum service load combinations for foundation design 
# df3=pd.read_csv("Service.csv", encoding ='latin1',header = 6, 
# usecols=[0,4,5,6,7,8,9,10],
# na_values="-"
# )
# df3.rename(columns={"Unnamed: 0": "Support","Unnamed: 4": "Loadcase", "Fvert\n[kN]":"Fv", "Fmajor\n[kN]":"Fy","Fminor\n[kN]":"Fx","Mmajor\n[kNm]":"My","Mminor\n[kNm]":"Mx","Mtor\n[kNm]":"Mtor"}, inplace=True)
df3=pd.read_csv("Service.csv", encoding ='latin1',header = 6, 
usecols=[0,5,6,7,8,9,10],
na_values="-"
)
df3.rename(columns={"Unnamed: 0": "Support", "Fvert\n[kN]":"Fv", "Fmajor\n[kN]":"Fy","Fminor\n[kN]":"Fx","Mmajor\n[kNm]":"My","Mminor\n[kNm]":"Mx","Mtor\n[kNm]":"Mtor"}, inplace=True)

# Creating support names for all loadcases
df3.Support = df3.Support.fillna(0)
for i in range (1,len(df3)):
    if df3.loc[i, 'Support'] == 0:
        df3.loc[i, 'Support'] = df3.loc[i-1, 'Support'] 

df3.set_index('Support', inplace=True)

# Finding maximum value for each column, make new table with the values and show what support is associated with it 
max_index = df3.Fv.idxmax()
print(max_index)
index_list = []
for column in df3.columns:
    print(column)
    if column == 'Fv':
        index_list.append((column,df3[column].idxmin(),df3[column].min()))
    # if column == 'Fy','Fx','My','Mx','Mtor':
    else:
        index_list.append((column,df3[column].abs().idxmax(),df3[column].abs().max()))
    
    


summary_df3 = pd.DataFrame()
for entry in index_list:
    tempdf = df3.loc[entry[1]]
    summary_df3 = summary_df3.append(tempdf)
# summary_df.append(tempdf)
summary_df3.head(30)


# %%



