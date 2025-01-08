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
    const data = req.body;

    const msg = data[0].msg;
    const input = {
        detail: [
            {
                input: {
                    msg: msg
                }
            }
        ]
    };

    const fastapi = config.fastapi;

    try {
        // 發送第一個 POST 請求到 /asklm
        const asklmResponse = await fetch(fastapi + '/translate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(input),
        });

        const asklmData = await asklmResponse.json();
        console.log('Response from /translate:', asklmData.msg);

        // 發送第二個 POST 請求到 /translate，使用 /asklm 的回應
        const vtocmsgInput = [{msg: asklmData.msg}];
        console.log(config.http + '/uiapp/vtocmsg');
        const vtocmsgResponse = await fetch( config.http + 'uiapp/vtocmsg', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(vtocmsgInput),
        });

        const vtocmsgData = await vtocmsgResponse.text();
        console.log('Response from /vtocmsg:', vtocmsgData);

        const result = [
            { input: asklmData },
            { output: vtocmsgData }
        ];
        res.send(result);
    } catch (error) {
        console.error('Error in /vtocvoice:', error);
        res.status(500).send({ error: 'Failed to process vtocvoice' });
    }
})


module.exports = router