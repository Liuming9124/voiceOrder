const express = require('express')
const router = express.Router()
const fs = require('fs');


const config = JSON.parse(fs.readFileSync('config.env', 'utf8'));

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
    input = {
        "detail": [
            {
                "input": {
                    "msg": msg
                }
            }
        ]
    }

    fastapi = config.fastapi + '/asklm';
    console.log(fastapi);

    // 發 post request 
    await fetch( fastapi, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(input),
    })
    .then(res => res.json())
    .then(data => {
        console.log('Success:', data);
        res.send([data]);
    })
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