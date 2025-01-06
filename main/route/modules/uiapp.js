const express = require('express')
const router = express.Router()

const uiappCtl = {
    uiappPage: async (req, res) => {
        return res.send("uiapp");
    }
}

router.get('/', uiappCtl.uiappPage)

module.exports = router