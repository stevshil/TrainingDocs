// insecure-server.js
const express = require("express");
const app = express();

// No Helmet here!

app.get("/", (req, res) => {
  res.send("Helmet is OFF — no security headers.");
});

app.get("/image", (req,res) => {
  res.send(`<img src='https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/Cat_November_2010-1a.jpg/500px-Cat_November_2010-1a.jpg'>`)
})

app.listen(3001, () => {
  console.log("Insecure server running on http://localhost:3001");
});
