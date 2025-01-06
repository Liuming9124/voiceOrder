const express = require('express')
const neo4j = require('neo4j-driver');
const router = express.Router()
const db = neo4j.driver(
    'bolt://server.lmteck.uk:7687',
    neo4j.auth.basic('neo4j', 'R6jCH8EiOAQji18')
);


const dbCtl = {
    dbMenu: async (req, res) => {
        const session = db.session(); // 創建 session
        try {
            const result = await session.run('MATCH (n) RETURN n'); // 執行查詢
            const nodes = result.records.map(record => record.get('n').properties); // 獲取節點屬性
            return res.json(nodes); // 返回 JSON 格式的節點資料
        } catch (error) {
            console.error('Error fetching data from Neo4j:', error);
            return res.status(500).send('Internal Server Error');
        } finally {
            session.close();
        }
        return res.send('test');
    }
}

router.get('/', dbCtl.dbMenu)

module.exports = router