from py2neo import Graph

# 連接至 Neo4j 資料庫
graph = Graph("bolt://server.lmteck.uk:7687", auth=("neo4j", "R6jCH8EiOAQji18"))

def delete_all_nodes():
    # 執行 Cypher 查詢刪除所有節點及其關係
    graph.run("MATCH (n) DETACH DELETE n")
    print("All nodes and relationships have been deleted.")

if __name__ == "__main__":
    delete_all_nodes()
