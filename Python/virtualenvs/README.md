# Working with Virtual Environments

Virtual environments allow you the developer to start with a completely fresh version of a Python environment for developing your application.

Using a Python virtual environment will ignore all other Python settings and modules that have been installed on your computer system.  From this fresh environment you can identify which modules you have installed and are required by your application.  This in turn allows you to create a dependency file so that other developers or people deploying and running your application can ensure that they have all the correct requirements for running your script.

## Creating a new virtual environment

To create a virtual environment for your project, you need to have a command line that is in your project directory.

In that command line you will then run;

```
python -m venv .venv
```

**.venv** is the naming convention used for the virtual environment, but you could call it what you like, especially if you are developing on different operating systems, as some modules will vary depending on whether you're using Linux, Mac or Windows.

Once the command has completed you will have a local copy of Python and libraries in your folder.

If you are using **git** then you should ensure that the **.venv** folder is added to your **.gitignore** file as follows;

```
**/.venv
```

If you are using VS Code then it will prompt you with a pop-up message asking if you wish to associate the virtual environment with the project.  Click **Yes**.  That way when you click the **play** button it will use the virtual environment and not the system wide Python.

## Activating your virtual environment

To activate a virtual environment from the command line;

* Windows

    ```sh
    .\.venv\Scripts\activate
    ```

* Linux/Mac

    ```sh
    source ./.venv/bin/activate
    ```

    or

    ```sh
    . ./.venv/bin/activate
    ```

This command updates the current command line setting up Python to only use your local .venv directory to run Python and store modules.

Once activated your prompt will change showing the name of the virtual environment directory in brackets/paranethises ( ) at the beginning of your prompt.  E.g.;

```sh
(.venv) C:\Users\Steve> 
```

## Using your virtual environment

Now your virtual environment is active you can start to code and install modules and run your code knowing that you have a fresh Python system.

Let's say that you have the following Python code in a file called **moduleplay.py**;

```python
import requests

response = requests.get("https://swapi.info/api/films")

print(response.status_code)
if ( response.status_code == 200 ):
    print(response.json())
else:
    print(f"Error: {response.status} - a problem occurred")
```

By default the **requests** module is not installed and not part of the Python standard library.

If we tried to run the program it would fail;

```sh
(.venv) C:\Users\Steve> python moduleplay.py
Traceback (most recent call last):
  File "C:\Users\Administrator\Documents\PythonWeb\modulesplay.py", line 1, in <module>
    import requests
ModuleNotFoundError: No module named 'requests'
```

With our prompt showing the virtual environment as being active we can do the following;

```sh
(.venv) C:\Users\Steve> pip install requests
```

This will download and install the **requests** module into the **.venv** folder in the relevant modules sub-directory.

Now when we run our program it will work and return the data from the web API.

## Storing our installed modules

As we continue to develop our application so we will install more modules.  We need to keep track of the modules we have installed so that other developers and users can simply set up and run our program.

To do this we need to store a list of the modules, and their versions.

In Python we do this with a command called **pip freeze** as follows;

```sh
pip freeze >requirements.txt
```

The **>requirements.txt** captures the output of the command and stores it into the file called **requirements.txt**.  This is the name by convention used to store module requirements for your program.

## Using requirements

If you are going to work with a Python project that has had external modules installed you will want to use the **requirements.txt** file to be able to install all the required modules and packages.

As long as the developer has provided the requirements.txt file in their git repository, which they should do if they are a proper Python developer, then you can install all the required dependencies as follows;

```sh
pip install -r requirements.txt
```

Ideally you would have activated your virtual environment if you're developing first, but if you're installing as an application on a system for general use, you will run without the virtual environment.

The change to our command is that we use the **-r** option and give it the file containing the list of modules and packages to install.  If the file only contains the names of the modules then it will install the newest.  If it has versions with the modules it will install the versions.

**References**

* https://pip.pypa.io/en/stable/reference/requirement-specifiers/

## Removing modules

To remove a module simply run;

```sh
pip uninstall requests
```

Where requests is the name of the module to remove.

**REMEMBER**

Update your **requirements.txt** file so that you keep the module requirements up to date;

```sh
pip freeze >requirements.txt
```