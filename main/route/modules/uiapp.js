const express = require('express')
const router = express.Router()

const uiappCtl = {
    uiappPage: async (req, res) => {
        return res.send("uiapp");
    }
}

router.get('/', uiappCtl.uiappPage)
router.post('/vtocmsg', async (req, res) => {
    data = req.body
    console.log(data)
    
    res.send("vtocMsg success");
})


router.post('/vtocvoice', async (req, res) => {
    data = req.body
    console.log(data)
    
    res.send("vtocvoice success");
})


module.exports = router