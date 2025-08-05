# Steps to creating a Spring Boot Java application

Intellij and Eclipse provide the ability to create a spring boot application within the IDE.  For this guide, we will create it externally using the **[Spring Initializr](https://start.spring.io/)**

## Creating the project structure

1. Point your web browser at https://start.spring.io/
2. Select the packaging system you prefer.  For this example we will be using **Maven**.
3. Select the programming language, in this case **Java**.
4. Select the version of Sprint Boot you wish to code with.  At the time of writing this guide - 3.5.4 was the stable version.
5. The project meta data should contain information about your project.  For example the group would normally be the DNS name of your organisation backward.
    * The **Artifact** is the name you want to give the the executable **jar** file.
    * The **package name** will be automatically completed.
    * For this example we will use
        * Group: **com.tps**
        * Artifact: **myapp**
        * Name: **myapp** - this will be filled out from Artifact
        * Leave **Description** as is
        * Leave **Package name** as generated
6. Leave **Packaging** as **Jar**
7. Select the Java version you will be developing in.  21 will be used for this example.
8. Now we need to add our dependencies.
    * Click the **ADD DEPENDENCIES** button
    * Add the following dependencies;
        * Lombok
        * Spring Configuration Processor
        * Spring Web
        * Spring Data JPA
9. Finally click the **GENERATE** button to download the zip file of your project.

The [**myapp.zip**](./myapp.zip) file was created using the above selection.

## Getting ready to code

Now we have our zip file we need to extract it so that we can open it in our chosen IDE.

1. Unzip the file.
2. The zip file will create the **myapp** directory containing the requirements for your project and the directory layout.
3. Open the **myapp** directory in your IDE.

## Next

Now go to the **[part_2](../part_2)** folder to continue.