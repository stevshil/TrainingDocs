const express = require('express');
// const helmet = require('helmet');
const app = express();

// Use helmet middleware
// app.use(helmet());
app.use((req, res, next) => {
  console.log('Time:', Date.now())
  next()
})


app.get('/', (req, res) => {
  res.send('Hello, world!');
});

app.listen(3000, () => {
  console.log('Server is running on port 3000');
});