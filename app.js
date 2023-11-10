const dotenv = require("dotenv");
dotenv.config({path:"config.env"});
const express = require("express");
const app = express();

const port = process.env.PORT || 80;

app.use(express.static('public'));

app.listen(port,()=>{
  console.log(`Application is listening on PORT:${port}`)
});