// Example from:
// https://codersociety.com/blog/articles/hashicorp-vault-node

const vault = require("node-vault")({
    apiVersion: "v1",
    endpoint: "http://127.0.0.1:8200",
  });
  
  const roleId = process.env.ROLE_ID;
  const secretId = process.env.SECRET_ID;
  
  const run = async () => {
    const result = await vault.approleLogin({
      role_id: roleId,
      secret_id: secretId,
    });
  
    vault.token = result.auth.client_token; // Add token to vault object for subsequent requests.
  
    const { data } = await vault.read("secret/data/mysql/webapp"); // Retrieve the secret stored in previous steps.
  
    const databaseName = data.data.db_name;
    const username = data.data.username;
    const password = data.data.password;
  
    console.log({
      databaseName,
      username,
      password,
    });
  
    console.log("Attempt to delete the secret");
  
    await vault.delete("secret/data/mysql/webapp"); // This attempt will fail as the AppRole node-app-role doesn't have delete permissions.
  };
  
  run();
  