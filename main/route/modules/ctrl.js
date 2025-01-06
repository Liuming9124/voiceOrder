const express = require('express')
const router = express.Router()

const ctrlCtl = {
    ctrlPage: async (req, res) => {
        console.log('ctrl in')
        res.send("ctrl");
    }
}

router.get('/', ctrlCtl.ctrlPage)

module.exports = router