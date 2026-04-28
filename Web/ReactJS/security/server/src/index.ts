import express from "express";
import bodyParser from "body-parser";
import cors from "cors";
import { login, authenticateJWT } from "./auth";
import { users } from "./users";

const app = express();

// Allow frontend at http://localhost:5173
app.use(cors({
  origin: "http://localhost:5173",
  methods: ["GET", "POST"],
  allowedHeaders: ["Content-Type", "Authorization"]
}));

app.use(bodyParser.json());

app.post("/login", login);
app.get("/users", authenticateJWT, (req, res) => {
  res.json(users);
});

app.listen(3000, () => {
  console.log("Server running on http://localhost:3000");
});
