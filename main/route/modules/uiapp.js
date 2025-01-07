const express = require('express')
const router = express.Router()

const uiappCtl = {
    uiappPage: async (req, res) => {
        return res.send("uiapp");
    }
}

router.get('/', uiappCtl.uiappPage)
router.post('/vtocmsg', async (req, res) => {
    data = req.body;
    console.log(data);
    msg = data[0].msg;
    returnmsg = "receive " + msg;
    response = [{"msg":returnmsg}];
    res.send(response);
})


router.post('/vtocvoice', async (req, res) => {
    data = req.body;
    console.log(data);
    msg = data[0].msg;
    returnmsg = "receive " + msg;
    response = [{"msg":returnmsg}];
    res.send(response);
})


module.exports = router