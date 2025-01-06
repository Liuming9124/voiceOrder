import pandas as pd

# 定義食物資料
data = [
    {"name": "檸檬塔", "description": "一款以檸檬為主的甜點，酸甜可口。", "taste": "酸", "price": 120, "weather": "晴天", "type": "甜點"},
    {"name": "紅燒牛肉麵", "description": "湯頭濃郁，牛肉軟嫩的經典主食。", "taste": "辣", "price": 200, "weather": "陰天", "type": "主食"},
    {"name": "炸雞塊", "description": "外酥內嫩的炸雞，適合當小吃或配餐。", "taste": "鹹", "price": 80, "weather": "雨天", "type": "小吃"},
    {"name": "珍珠奶茶", "description": "加入珍珠的奶茶，甜度可調，深受歡迎的飲料。", "taste": "甜", "price": 50, "weather": "晴天", "type": "飲料"},
    {"name": "巧克力慕斯蛋糕", "description": "滑順濃郁的巧克力慕斯，適合作為甜點享用。", "taste": "甜", "price": 150, "weather": "陰天", "type": "甜點"},
    {"name": "麻辣火鍋", "description": "辛香麻辣的火鍋，適合多人共享。", "taste": "辣", "price": 300, "weather": "雨天", "type": "主食"},
    {"name": "水果沙拉", "description": "清爽健康的水果沙拉，適合夏日享用。", "taste": "甜", "price": 100, "weather": "晴天", "type": "甜點"},
    {"name": "炒米粉", "description": "經典台式小吃，加入各種配料的炒米粉。", "taste": "鹹", "price": 60, "weather": "陰天", "type": "小吃"},
    {"name": "抹茶拿鐵", "description": "濃郁抹茶風味，搭配奶香。", "taste": "苦", "price": 70, "weather": "晴天", "type": "飲料"},
    {"name": "炸蝦天婦羅", "description": "酥脆的炸蝦，搭配特製醬料。", "taste": "鹹", "price": 120, "weather": "晴天", "type": "小吃"},
    {"name": "咖哩飯", "description": "濃郁咖哩搭配白飯，是經典主食之一。", "taste": "辣", "price": 150, "weather": "雨天", "type": "主食"},
    {"name": "布丁", "description": "細緻滑嫩的布丁，適合甜點愛好者。", "taste": "甜", "price": 40, "weather": "陰天", "type": "甜點"},
    {"name": "鹽酥雞", "description": "台灣夜市必吃小吃，炸得香酥可口。", "taste": "鹹", "price": 90, "weather": "晴天", "type": "小吃"},
    {"name": "手工啤酒", "description": "多種口味可選的精釀啤酒，適合小酌。", "taste": "苦", "price": 150, "weather": "晴天", "type": "飲料"},
    {"name": "日式拉麵", "description": "濃厚湯頭搭配彈牙麵條的日式經典。", "taste": "鹹", "price": 180, "weather": "陰天", "type": "主食"},
    {"name": "抹茶冰淇淋", "description": "帶有微苦甘甜的抹茶冰淇淋。", "taste": "苦", "price": 80, "weather": "晴天", "type": "甜點"},
    {"name": "番茄炒蛋", "description": "酸甜開胃的家常料理。", "taste": "酸", "price": 70, "weather": "陰天", "type": "主食"},
    {"name": "芒果冰沙", "description": "清涼消暑的芒果冰沙，夏日必備。", "taste": "甜", "price": 60, "weather": "晴天", "type": "飲料"},
    {"name": "芝士焗飯", "description": "濃郁芝士與米飯的完美結合。", "taste": "鹹", "price": 180, "weather": "雨天", "type": "主食"},
    {"name": "熱巧克力", "description": "暖心濃郁的熱巧克力飲品，適合寒冷天氣。", "taste": "甜", "price": 90, "weather": "陰天", "type": "飲料"}
]

# 創建 DataFrame
df = pd.DataFrame(data)

# 匯出為 Excel 檔案
file_path = "./food.xlsx"
df.to_excel(file_path, index=False)

file_path
