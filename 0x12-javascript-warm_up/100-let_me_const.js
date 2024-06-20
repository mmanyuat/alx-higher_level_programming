#!/usr/bin/node
require('./100-main.js');
global.myVar = 333;
module.exports = myVar;
