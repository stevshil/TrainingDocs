const express = require('express');
const mysql = require('mysql');
const bcrypt = require('bcryptjs');
const http = require('http');
// Below deals with hardcoded values
require('dotenv').config()
// Info exposure prevention
// const helmet = require("helmet");
const app = express();

// Using SSL certs
// const https = require('https');
// const fs = require('fs');
// const options = {
//   key: fs.readFileSync("/app/api/certs/localhost.key"),
//   cert: fs.readFileSync("/app/api/certs/localhost.cert"),
// };


// Remove for CSRF fix
app.use(express.json())

// Fix for CSRF
// const cookieSession = require('cookie-session')
// const csurf = require("csurf");
// app.use(require("body-parser").json())
// app.use(
//   require("cookie-session")({
//       secret: "secret123",
//       maxAge: 24 * 60 * 60 * 1000
//   })
// );

// app.use(csurf());

// app.use(function(req, res, next) {
//   res.cookie("mytoken", req.csrfToken());
//   next();
// });

// Create a MySQL connection
const db = mysql.createConnection({
  host: 'database',
  database: 'user_accounts',
  user: 'root',
  password: 'secret123',
  // user: process.env.DBUSER,
  // password: process.env.DBPASS,
  // host: 'localhost',
  // port: '1306',
});

// Connect to the database
db.connect((err) => {
  if (err) throw err;
  console.log('Connected to MySQL database');
});

// Route to list users
app.get('/users', (req, res) => {
  const query = 'SELECT * FROM users'; // Adjust the query as needed
  db.query(query, (err, results) => {
    if (err) throw err;
    res.json(results); // Send user data as JSON
  });
});

// Route to list specifi users
app.get('/users/:username', (req, res) => {
  const username = req.params.username;
  const query = 'SELECT * FROM users WHERE username LIKE "%'+username+'%"'; // Dangerous SQL
  // console.log(query);
  // The above allows for http://localhost:1080/users/steve%22%20OR%201=1;%20--%20''
  // Or better written as http://localhost:1080/users/steve" OR 1=1; -- ''
  // This displays all results
  // const query = 'SELECT * FROM users WHERE username LIKE ?'; // SAFE SQL
  // db.query(query, "%"+username+"%", (err, results) => { // Safe SQL Query
  db.query(query, (err, results) => {
    if (err) throw err;
    res.json(results); // Send user data as JSON
  });
});

// Route to handle adding a user
app.post('/users/add', (req, res) => {
  const { username, email, password } = req.body;
  try {
    const salt = bcrypt.genSaltSync(10);
    const hashedPassword = bcrypt.hashSync(password, salt);
    console.log(req.body)
    const query = 'INSERT INTO users (username, email, password) VALUES (?, ?, ?)';
    db.query(query, [username, email, hashedPassword], (err, result) => {
      if (err) throw err;
      res.status(201).json({ message: 'User registered successfully' });
    });
  } catch (error) {
    res.status(500).json({ error: 'Internal server error' });
  }
});

app.put('/users/:id', (req, res) => {
  const userId = req.params.id; // User ID from the route parameter
  const { username, email, password } = req.body; // Updated data from the request body
  var updateQuery;
  var updateData;
  var hashedPassword;
  const salt = bcrypt.genSaltSync(10);

  // Validate request data (you can add more validation as needed)
  if (!username || !email) {
      return res.status(400).json({ message: 'Username and email are required.' });
  }

  // Update user data in the database
  if (!password) {
    updateQuery = 'UPDATE users SET username = ?, email = ? WHERE id = ?';
    updateData = [username, email, userId]
  } else {
    hashedPassword = bcrypt.hashSync(password, salt);
    updateQuery = 'UPDATE users SET username = ?, email = ?, password = ? WHERE id = ?';
    updateData = [username, email, hashedPassword, userId]
  }
  db.query(updateQuery, updateData, (err, result) => {
      if (err) {
          console.error('Error updating user data:', err);
          return res.status(500).json({ message: 'Internal server error.' });
      }
      if (result.affectedRows === 0) {
          return res.status(404).json({ message: 'User not found.' });
      }
      res.json({ message: 'User data updated successfully.' });
  });
});

// Start the server
const PORT = process.env.PORT || 80;
// app.listen(PORT, () => {
//   console.log(`Server running on port ${PORT}`);
// });

// With HTTPS
var httpServer = http.createServer(app);
// var httpsServer = https.createServer(options, app);

httpServer.listen(PORT);
// httpsServer.listen(443);
