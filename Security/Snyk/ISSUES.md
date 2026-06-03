# Typical examples of what you might do if unaware.

## How code is insecure

The insecure patterns in wording:

#### 1. Hardcoded usernames and passwords

**What people do:**

- **Hardcode credentials** directly in source:
  - **Label:** Example pattern  
    - A string like `"admin"` / `"password123"` inside the code, used for login checks.
- **Commit secrets to Git**:
  - `.env` contents or API keys pushed to GitHub.

**Why it's bad:**

- Anyone with repo access (or leaked repo) gets full access.
- Rotating credentials becomes painful, so they never get rotated.

**What to do instead:**

- **Use environment variables** (`process.env.DB_USER`, `process.env.DB_PASS`).
- Use a **secrets manager** (Azure Key Vault, AWS Secrets Manager, HashiCorp Vault, etc.).
- Add `.env` to `.gitignore`.

---

#### 2. Vulnerable package versions

**What people do:**

- Pin to **old versions** of Express, body-parser, templating engines, etc.
- Ignore `npm audit` / Snyk warnings.

**Typical issues:**

- **Prototype pollution**, **ReDoS**, **path traversal**, or **XSS** in dependencies.
- Old versions of Express or middleware with known CVEs.

**What to do instead:**

- Run:
  - `npm audit`
  - Snyk scans
- Regularly update dependencies and read changelogs for breaking changes.
- Avoid random, unmaintained packages for critical functionality.

---

#### 3. HTTP header issues (XSS, clickjacking, etc.)

**What people do:**

- Don't set any security headers at all.
- Manually set headers incorrectly (e.g., `X-Frame-Options: ALLOWALL` or no CSP).

**Common missing or misconfigured headers:**

- **Content-Security-Policy (CSP):** Helps mitigate XSS by restricting script sources.
- **X-Frame-Options / frame-ancestors:** Prevents clickjacking.
- **X-Content-Type-Options: nosniff:** Stops MIME sniffing.
- **Referrer-Policy:** Controls how much referrer info is leaked.
- **Strict-Transport-Security (HSTS):** Forces HTTPS.

**What to do instead:**

- Use **`helmet`** (as in the example) to set sane defaults.
- Add a CSP tailored to your app.
- Serve everything over HTTPS in production.

---

#### 4. Insecure authentication and authorization

**What people do:**

- Use **plain-text passwords** in the database.
- Implement **homegrown crypto** or roll their own token format.
- Forget to check **ownership** of resources (e.g., any user can access any task by ID).

**Typical problems:**

- **No hashing**: storing passwords as plain text or with weak hashes (like MD5).
- **JWT misuse**: no expiration, weak signing keys, or using `none` algorithm.
- **Broken access control**: user A can fetch user B's tasks by guessing IDs.

**What to do instead:**

- Hash passwords with **bcrypt**, **argon2**, or similar.
- Use well-tested libraries for JWT or session management.
- Always check `task.userId === req.user.id` (like in the example).

---

#### 5. Input validation and injection

**What people do:**

- Directly concatenate user input into:
  - SQL queries
  - NoSQL queries
  - File paths
- Trust `req.body`, `req.params`, `req.query` without validation.

**Typical vulnerabilities:**

- **SQL injection** (classic).
- **NoSQL injection** (e.g., MongoDB operators).
- **Command injection** if user input reaches `child_process.exec`.

**What to do instead:**

- Use **parameterized queries** or ORM/Query builders.
- Validate input with libraries like **Joi**, **Zod**, or **Yup**.
- Reject unexpected fields and types.

---

#### 6. Logging and error handling

**What people do:**

- Log full stack traces and **sensitive data** (tokens, passwords, PII).
- Return raw error messages to clients.

**Risks:**

- Logs become a treasure trove for attackers.
- Detailed errors reveal internal structure, table names, file paths.

**What to do instead:**

- Log **only what you need**, and scrub sensitive fields.
- Return generic error messages to clients, detailed ones only in secure logs.
- Use centralized logging with access controls.

---

### How to turn this into a learning lab (without me giving you bad code)

If you want to learn deeply, here's a path:

1. **Start from the secure-ish example above.**
2. **Run Snyk** (or `npm audit`) against it and note the baseline.
3. **Intentionally weaken things yourself**, one at a time:
   - **Label:** Example experiments  
     - Remove `helmet` and see what headers disappear.  
     - Downgrade a dependency to an older version and re-run Snyk.  
     - Add a naive login route and *then* try to spot what's wrong with it.  
     - Remove the `userId` check on tasks and see how access control breaks.
