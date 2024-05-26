# Vault documentation and Tutorials

https://developer.hashicorp.com/vault/tutorials/getting-started

## Quick commands

Listing all secrets:

```sh
vault secrets list
```

The **Type** field tells you what type of secret can be stored.

## Web UI

To access the web UI you'll need to go to the following URL:

http://localhost:8200

Select **Method** **Token** and use the **secret123** as the **Token**.

## Example CLI play

Run the docker compose command to launch the 2 containers **server** and **client**.
```sh
docker compose up -d
```

You can then connect to the client container:
```sh
docker compose exec client sh
```

From here you can run the Vault CLI commands.

To work with your Vault you will need to set up the following variables:
```sh
export VAULT_ADDR='http://server:8200'
```

## Examples

### Login to the vault server

```sh
vault login
```

You'll be prompted for the token.  For this example **secret123** is the token, which you can find in the docker-compose.yaml file.

### Add a secret to the vault

```sh
vault kv put -mount=secret hello foo=bar
```

This will create a secret called **hello** containing the key of **foo** and value of **bar**

### Show the secret

```sh
vault kv get -mount=secret hello
```

The above shows the metadata and detail of the secret.

If you just want the value, we need to change how we create the secret.
```sh
vault kv put -mount=secret hello foo=bar excited=yes
```

The **excited=yes** allows us to obtain just the value when calling get.  Handy if scripting using the vault command.

To view just the value:
```sh
vault kv get -mount=secret -field=excited hello
```

### Remove a secret from the vault

```sh
vault kv delete -mount=secret hello
```

Will delete the secret known as hello.

### Undelete a secret

```sh
vault kv undelete -mount=secret -versions=2 hello
```


## NodeJS Example

Taken from https://codersociety.com/blog/articles/hashicorp-vault-node

1. Launch the web UI for Vault
    * Open a web browser
    * In the address bar type in **http://localhost:8200**
2. Add AppRole:
    * Select **Access** from left menu
    * Click **Enable New Method**
    * Select **AppRole**
    * Leave settings as are and click **Enable Method**
3. Create policy secret access
    * Select **Policies** from left menu
    * Click **Create ACL Policy**
    * Enter the name as **readonly-kv-backend**
    * Enter the following in the Policy box;
        ```json
        path "secret/data/mysql/webapp" {
        capabilities = [ "read" ]
        }
        ```
4. Log in to the vault client and run the following commands;
   * Set up the variables
        ```sh
        export VAULT_ADDR='http://server:8200'
        export VAULT_TOKEN=secret123
        ```
    * Create an appRole
        ```
        vault write auth/approle/role/node-app-role \
        token_ttl=1h \
        token_max_ttl=4h \
        token_policies=readonly-kv-backend
        ```
    * Get the role ID
        ```sh
        vault read auth/approle/role/node-app-role/role-id
        ```
    * Fetch the secret id
        ```sh
        vault write -f auth/approle/role/node-app-role/secret-id
        ```
    * Create a secret
        ```sh
        vault kv put secret/mysql/webapp db_name="users" username="admin" password="passw0rd"
        ```
        Alternatively you can add this in the UI by selecting **secret** and using mysql/webapp as the path
5. Install node-vault module
    ```sh
    npm install node-vault
    ```
6. Set the ROLE_ID and SECRET_ID values
    ```sh
    export ROLE_ID=<role id fetched in previous section>
    export SECRET_ID=<secret id fetched in previous section>
    ```

    FOR PowerShell:

    ```powershell
    $Env:ROLE_ID = '<role id fetched in previous section>'
    $Env:SECRET_ID=<secret id fetched in previous section>
    ```
7. Run the dodata.js script
    ```sh
    node index.js
    ```