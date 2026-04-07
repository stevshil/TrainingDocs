# Creating a New Repository

To create a repository in git do the following;

1. Create a new directory

    ```sh
    mkdir my_new_project
    ```

2. Change into the new directory

    ```sh
    cd my_new_project
    ```

3. Initialise a git repository

    ```
    git init
    ```

4. Git will respond with something similar to;

    ```
    Initialised empty Git repository in /home/steve/my_new_project/.git/
    ```

The last command is the key.  This creates the magical **.git** directory ready for your **git** actions that you perform.

If you list the directory you should see the **.git** directory.

```sh
$ ls -la
total 12
drwxrwxr-x  3 steve steve 4096 Apr  7 00:22 .
drwxr-xr-x 10 steve steve 4096 Apr  7 00:21 ..
drwxrwxr-x  7 steve steve 4096 Apr  7 00:22 .git
```

If you're using Windows then use a program such as **GitBash** available from [https://git-scm.com/install/windows](https://git-scm.com/install/windows).

Every time you wish to create a new project that is going to be version controlled by Git you will need the **git init** command.  But you must be the creator**.
**

> **IMPORTANT:**  If you are using a Git repository or it already exists do not use this command!.

## Your turn

1. Go back to your HOME directory.
    Just **cd** on it's own will do this if you're using a Linux command line, such as GitBASH.

2. Create a new project directory called **learning_git**

3. Initialise that directory as a Git repository.

4. Create another directory from your HOME directory called **more_git** and make that a Git repository.

---

[⬅ Back](README.md)<span style="float: right;">
[Next ➡](02-Make_History.md)</span>