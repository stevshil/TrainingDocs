# Making History

Git is all about keeping track of changes.  The following commands and examples show you how and when to store your history.

## The commands

In this section you will use the following commands;

- **add**
  - Adds specified files to the staging area, ready to be added to history
  - Akin to placing in a shopping cart, but you're not ready to checkout yet as you might change your mind
- **commit**
  - This is the command that makes history
  - Once you commit a change, Git creates the snapshot of the files
  - At this point you can look back at the different changes
  - Akin to paying for you goods at the checkout - creating a purchase history
- **status**
  - Tells us where we are, and whether anything has changed
- **stash**
  - Store changes that you do not yet want to commit to history

## Adding

When coding or writing config files, or other files and directories that need to be recorded in Git, you would use your favourite (or your company recommended) text editor or IDE to create the files and directories as normal.  There is no difference here or even when you further edit the files.  We just treat them like normal files.

Before we can create history we have to tell Git which files we wish to be part of the history.  The reason for this is that you can select only those files that you want to be added to the history, as others might not be ready.

> **ANALOGY:** Imagine that you are shopping in your favourite food store.  You have your shopping cart and you take things of the shelf that you like and place them in the cart.  This is **git add**, known as **staging** changes. You then decide that there was a nicer coffee on the shelf, so you need to **un-stage** the change and remove the coffee from your basket to put the new one in.  Un-staging is done using **git rm --cached**.  So now you add the new one in with **git add**.

Let's do this.

1. In the last section you created a new Git repository and directory called **learning_git**.
2. Change into the **learning_git** directory.
3. Create a file called **hello.py** and add the following text;

    ```python
    #!/usr/bin/env python

    print("Hello World")
    ```

4. Now that we have some working code, we want to store it as a back up, just in case we continue to work on the file and then break it.  If we break it and have it stored in Git history we can then come back to this point in time.  So first we need to tell Git which files we want to add to the history;

    ```sh
    git add hello.py
    ```

    In this example we have specified the exact filename.

    Later we will introduce you to storing multiple files and all files.

5. The **add** has only made Git aware that we want to record this as history.  Git uses hashes to identify changes in history.  We now want to save this change as a historical snapshot;

    ```sh
    git commit -m "My first python file in git"
    ```

    The **commit** command requires a comment, which normally tells us what the change relates to.  Some organisations use the ticket and a short description, others may ask you to write the answer to "What did the change fix or do?".

6. You have now created history.  To check type;

    ```sh
    git log
    ```

    This will output a long has reference or which the first 5 or so characters should match with the output of your **git commit** command.

Let's now make a further change and we will look at the different states, using the **git status** command at each stage.

1. Open the **hello.py** file again and add the following line at the end of the file;

    ```python
    print("End of program")
    ```

2. Run the command;

    ```sh
    git status
    ```

    The output will tell you;
    - Which branch you are on
    - It will state which changes have not been staged, and provides example commands for storing or restoring.
    - Example output;

      ```sh
      On branch main
      Changes not staged for commit:
          (use "git add <file>..." to update what will be committed)
          (use "git restore <file>..." to discard changes in working directory)
          modified:   hello.py

        no changes added to commit (use "git add" and/or "git commit -a")
      ```
3. Now we can add.  This time we will add everything using the **-a** option.

    ```sh
    git add -A
    ```

4. Check the state;

    ```sh
    git status
    ```

    > NOTE: The change in the output.  If you have a colour capable terminal the file name has changed from red to green.  You are also told that **Changes to be committed**

5. Add the change to the history;

    ```sh
    git commit -m "Added the end of program"
    ```

    You will now see the new history commit hash.

6. Checking status at this point will show;

    ```sh
    On branch main
nothing to commit, working tree clean
    ```

Using **git status** is very usefull to remember where you are in the process of adding files to your Git history.

## Adding multiple files

We saw in the last example the use of;

```sh
git add -A
```

Which added all files.  This is a special option that will add all files in the Git repository regardless of where you are in the tree structure.

This would be equivalent to changing directory to the top of the Git repository, that is where you will find the **.git** directory, and then performing;

```sh
git add .
```

The **.** in this instance means current directory recursively down.  This can miss files if you are too far down in the directory structure.

---

  [⬅ Back](README.md)<span style="float: right;">
  [Next ➡](03.md)</span>