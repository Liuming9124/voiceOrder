const express = require('express')
const router = express.Router()

const llmCtl = {
    llmPage: async (req, res) => {
        return res.send("llm");
    }
}

router.get('/', llmCtl.llmPage)

module.exports = router