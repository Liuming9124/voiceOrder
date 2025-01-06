var express = require('express');
var path    = require('path');
var app     = express();
const fs = require('fs');

// // set ejs engine
// app.set('views', './views')
// app.set('view engine', 'ejs');

app.use(express.json());
app.use(express.urlencoded({ extended: true }));


//建立 server
app.use(express.static('static')); //讀取靜態檔案
app.use('*/js'        ,express.static(path.join(__dirname, '/static/js')));

//require routes
require('./route')(app)

// read config.json
const config = JSON.parse(fs.readFileSync('config.env', 'utf8'));

app.listen(config.port,function(){ //port
  console.log(`listen on ${config.http}`)
})