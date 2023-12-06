import json

# 讀取檔案
file_path = 'C:/Users/user/Documents/研究所/vis2023f-main/hw03/src/json/AerobicData.json'

with open(file_path, 'r') as file:
    data = file.readlines()

# 將每一行的 JSON 物件加上逗號並合併成一個字串
json_data = '[' + ','.join(data) + ']'

# 將修改後的資料寫回檔案
with open(file_path, 'w') as file:
    file.write(json_data)

print("程式執行完成。")