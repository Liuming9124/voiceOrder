from py2neo import Graph, Node
import pandas as pd

# 連接至 Neo4j 資料庫
graph = Graph("bolt://server.lmteck.uk:7687", auth=("neo4j", "R6jCH8EiOAQji18"))

# 從 Excel 讀取資料
file_path = "./food.xlsx"  # 替換成您的 Excel 路徑
df = pd.read_excel(file_path)

# 新增每個 node 至 Neo4j
for _, row in df.iterrows():
    node = Node(
        "Food",
        name=row["name"],
        description=row["description"],
        taste=row["taste"],
        price=row["price"],
        weather=row["weather"],
        type=row["type"]
    )
    graph.create(node)
print("Nodes added successfully.")
