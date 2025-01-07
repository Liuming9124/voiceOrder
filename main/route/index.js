const ctrl = require('./modules/ctrl.js')
const uiapp = require('./modules/uiapp')
const llm   = require('./modules/llm')
const dbctl = require('./modules/dbctl')

module.exports = app => {
  app.use('/ctrl',  ctrl)
  app.use('/uiapp',  uiapp)
  app.use('/llm',    llm)
  app.use('/dbctl',  dbctl)
  app.post('/vtocvoice', async (req, res) => {
    console.log('vtocvoice in')
    res.send("vtocvoice");
  })
}
