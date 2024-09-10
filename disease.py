import pandas as pd

all_df = pd.read_excel('data/1_Alldata.xlsx', sheet_name='Alldata')
site_data = pd.read_excel("data/1_Alldata.xlsx", sheet_name="Plotdata")
location_df = pd.read_excel('data/1_Alldata.xlsx', sheet_name='Lacation')


location_df.rename(columns={'Site': 'Site2'}, inplace=True)


pre_data = pd.merge(site_data, location_df, left_on="Site", right_on="Site2")

# total_df = pd.merge(
#     pre_data, 
#     all_df, 
#     left_on=['Site', 'Route', 'Plot', 'Region'], 
#     right_on=['Site', 'Route', 'Plot', 'Region']
# )

total_df = pd.merge(
    all_df,pre_data, 
    left_on=['Site', 'Route', 'Plot', 'Region'], 
    right_on=['site', 'Route', 'Plot', 'Region']
)
# 将合并后的 DataFrame 保存为 CSV 文件
csv_file_path = 'data/merged_data.csv'  # 指定保存路径和文件名
total_df.to_csv(csv_file_path, index=False)
print(total_df)
print(f"Data has been saved to {csv_file_path}")