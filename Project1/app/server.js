const express = require("express");
const mysql = require("mysql2");

const app = express();

const db = mysql.createConnection({
  host: "db",
  user: "root",
  password: "root",
  database: "testdb"
});

app.get("/", (req, res) => {
  db.query("SELECT 'Docker Compose Working!' AS message", (err, result) => {
    if (err) {
      return res.send("Database connection failed");
    }
    res.send(result[0].message);
  });
});

app.listen(3000, () => {
  console.log("App running on port 3000");
});

