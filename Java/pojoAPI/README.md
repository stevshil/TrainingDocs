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

# Building with Gradle CLI

Building a Pradle project from the command line will require Gradle to be installed on your system.  Don't panic though, as most projects created through IntelliJ or via SpringInitialzr will create a wrapper that can be used called **gradlew**.  This downloads the appropriate gradle for your project.

## Building the Jar file - method 1

Using the **fatjar** method - see the **build.gradle-fatjar** for configuration.

The main piece in the file that tells gradle to create the jar is;

```groovy
jar {
    manifest {
        attributes 'Main-Class': 'swapi.Server'
    }
    from {
        configurations.runtimeClasspath.collect { it.isDirectory() ? it : zipTree(it) }
    }
    duplicatesStrategy = DuplicatesStrategy.EXCLUDE
}
```

### To build

```sh
gradle clean build
```

Once complete successfully it will create your file in;

**build/libs**

## Building the Jar file - method 2

The alternative method is to use the **shadowJar** plugin, as shown in the **build.gradle-shadow**.

This requires 2 sections to be modified.

1. **plugins**
   - In this section you need to add;
      ```groovy
      id 'com.github.johnrengelman.shadow' version '8.1.1
      ```
2. Next you need to add the **shadowJar** section;
   ```groovy
   shadowJar {
      manifest {
         attributes 'Main-Class': 'swapi.Server'
      }
   }
   ```

### To build

```sh
gradle shadowJar
```

If building for a Docker container you need to use;

```sh
gradle shadowJar --no-daemon
```