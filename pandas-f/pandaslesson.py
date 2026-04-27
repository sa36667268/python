import pandas as pd
# # s=pd.Series([9, 3,32 , 4, 5])
# # # print(s)
# # print(s[0])
# # print(s[1:4])
# # s.index=['a','b','c','d','e']
# # print(s['e'])

# # df = pd.read_csv(r'C:\Users\sarav\OneDrive\Desktop\GUVI-Files\repos\python\california_housing_train.csv')
# # print(df)
# #df.dropna()
# # df.fillna({'housing_median_age': 99},inplace=True)
# # print(df.isnull().sum())
# # print(df.duplicated())
# # print(df.head(12))
# # df.info()
# # df.sample()
# # df_csv = pd.read_csv(r'C:\Users\sarav\OneDrive\Desktop\GUVI-Files\repos\python\california_housing_train.csv')
# # # df_json =pd.read_json(r'C:\Users\sarav\OneDrive\Desktop\GUVI-Files\repos\python\california_housing_train.json')
# # # df_parq= pd.read_parquet(r'C:\Users\sarav\OneDrive\Desktop\GUVI-Files\repos\python\california_housing_train.parquet')
# # # df_merge_read = pd.read_parquet(r'C:\Users\sarav\OneDrive\Desktop\GUVI-Files\repos\python\california_housing_train_merged.parquet')
# # # df_merge= pd.concat([df_csv,df_json,df_parq])
# # # print(df_merge)
# # # df_merge.to_parquet(r'C:\Users\sarav\OneDrive\Desktop\GUVI-Files\repos\python\california_housing_train_merged.parquet')
# # # print(df_merge_read)
# # # print(df_merge.duplicated().sum())
# # # df_merge.drop_duplicates(inplace=True)
# # # print(df_merge.duplicated().sum())
# # print(df_csv.head())
# # print(df_csv.groupby('latitude')['total_rooms'].sum())
# # print(df_csv.groupby(['latitude','longitude'])['total_rooms'].max())
# # df=pd.DataFrame({'date':['3/10/2026','4/10/2026','5/10/2026'],'value':[1,2,3]})
# # print(df.info())

# # print(df['date'].dtype)
# # df['date'] = pd.to_datetime(df['date'],format='%m/%d/%Y')
# # df = pd.DataFrame({'date': ['2016-6-10 20:30:0',
# #                             '2016-7-1 19:45:30',
# #                             '2013-10-12 4:5:1'],
# #                    'value': [2, 3, 4]})
# # df['date'] = pd.to_datetime(df['date'], format="%Y-%d-%m %H:%M:%S")
# # df['year'] = df['date'].dt.year
# # df['month'] = df['date'].dt.month
# # df['day'] = df['date'].dt.day
# # print(df)
# df = pd.DataFrame({'year': [2015, 2016],
#                    'month': [2, 3],
#                    'day': [4, 5]})
# print(df)
df = pd.DataFrame({'name': ['Tom', 'Andy', 'Lucas'],
                 'DoB': ['08-05-1997', '04-28-1996', '12-16-1995']})
df['DoB'] = pd.to_datetime(df['DoB'])
print(df['DoB'])
dw_mapping={
    0: 'Monday',
    1: 'Tuesday',
    2: 'Wednesday',
    3: 'Thursday',
    4: 'Friday',
    5: 'Saturday',
    6: 'Sunday'
}
df['day_of_week_name']=df['DoB'].dt.weekday.map(dw_mapping)
print(df)