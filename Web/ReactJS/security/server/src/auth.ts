import { Request, Response, NextFunction } from "express";
import jwt from "jsonwebtoken";
import { users } from "./users";

const SECRET = "MY_SUPER_SECRET_KEY"; // Replace with env variable in real apps

export const login = (req: Request, res: Response) => {
  const { username, password } = req.body;

  const user = users.find(
    (u) => u.username === username && u.password === password
  );

  if (!user) {
    return res.status(401).json({ message: "Invalid credentials" });
  }

  const token = jwt.sign({ username: user.username }, SECRET, {
    expiresIn: "1h"
  });

  res.json({ token });
};

export const authenticateJWT = (
  req: Request,
  res: Response,
  next: NextFunction
) => {
  const authHeader = req.headers.authorization;

  if (!authHeader) {
    return res.status(403).json({ message: "Missing token" });
  }

  const token = authHeader.split(" ")[1];

  jwt.verify(token, SECRET, (err, user) => {
    if (err) return res.status(403).json({ message: "Invalid token" });

    (req as any).user = user;
    next();
  });
};
