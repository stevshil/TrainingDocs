# Reconstructing the project

Here are the instructions for writing this project, if you don't want to just read through the code.

## Setting up the project structure

1. Create a new project in **Intellij**
2. Expand **src/main/java**
3. Right click **java**, select **New**, **Package**
4. Set the package name to **swapi**
5. Right click **swapi** and select **New** then **Package**
6. Set the package name to **controller**
7. Repeat steps 5 and 6, changing the **package** name to
   1. entity
   2. methods

## Setting up the test folder

1. Expand **test**, **java**
2. Right click **java**, select **New** then **Package**
3. Set the package name to **swapi**

## The Class Film

This code is only concerned with the films, and the following attributes;

- id
- title
- release_date

Our API will work with this data and class.  If you create more complex systems then you would create your classes in an entity folder, or something of a similar name to denote what the folder contains.

## Creating the API client

The API client **SwapiClient** is used to pull JSON data from the https://swapi.info service.  A service for Star Wars fans, containing various data about the films.

The API client makes use of the Google Gson module.  To be able to use this and have reference to the class in your code you need to add it to your **build.gradle** file, since it cannot be resolved by Intellij.

### Adding Google Gson

1. Locate and open your **build.gradle** file.
2. In the **dependencies** section add the following;
    ```
   dependencies {
        implementation 'com.google.code.gson:gson:2.10.1'
   }
   ```