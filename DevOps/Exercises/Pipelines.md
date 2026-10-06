# Pipelines

For these exercises you need to have developed a small application(s) already.  Ideally a frontend and a backend application, or have one that you can use, there are plenty in this repository to use, and Exercises to build an application;

- [Spring and Spring Boot](../../Java/Spring/Exercise/)
- [NodeJS/TypeScript](../../NodeJS/TypeScript/)
- [ReactJS](../../Web/ReactJS/)

## Objective

This lab is about DevOps and automating the testing, building and deployment of your application.

The lab is open for interpretation so that you can choose;
- Pipeline system
    - Bitbucket pipelines
    - GitHub Actions
    - Jenkins
    - TeamCity
    - Bamboo
    - etc

## Developing

You should choose a suitable branching strategy that protects the **main** branch, which is **production/live**.

All developers should work on a **feature/hotfix/bugfix** branching method, and related to a task.

Tasks could be real from Jira or Trello, or other Kanban methods, or made up.

You should consider that you are in a release process where every 2 weeks you will be merging the **release** branch into **main** in a controlled manner.  This could also be automated through a manual button click in your Git server.

## Building

### 1. Testing

The first thing we must do is ensure that your code isn't going to break the build, so we must run the unit tests as part of the pull request.

Doing this makes it easier for the reviewer of the pull request, and allowing them to review the code only.

**AI extra:** If you are working with an AI enabled pipeline, such as GitHub then you can also automate the review using Copilot.
- If Copilot spots issues or recommendations then it can complete an Issue or comment, or you could have it modify the code and a new P.R.

**EXTRA:** Could you automate the process of the merge, rather than manually clicking the button if all of the tests pass and Copilot has OK'd the review of the code?

### 2. Delivery

Once the initial unit tests have passed your **feature** branch should be merged into the **release** branch.

This ideally be an automated and controlled process, but you can simply have the developer click the **Merge** button in the Git server.

Once merged the **release** branch should have the following actions performed;
- A final run of all unit tests
- Integration tests to ensure that the project branch is stable before merging
- Build the final deployable package, which could be any of the following;
    - Docker image (recommended as easier to deploy)
        - Only requires Docker to be installed on the server
    - Jar file
        - Requires the right version of Java to be deployed to the servers
    - Zip file for React
        - Requires a web server software to be installed, e.g. NGINX or Apache
- The package should be made available for the deployment service
    - Either use;
        - Docker hub or AWS ECR for containers
        - JFrog Artifactory for other images
        - Research for the type of file you are creating

### 3. Deployment

This pipeline will deploy your application to a production ready environment.

We are by-passing a QA or staging environment, which would normally be used to check that our code is good to deploy.  Instead we will use your release branch to make these checks in the CI/CD pipeline.

You should deploy your built artifact to AWS, either;
- Already running AWS EC2 instance (ideally running docker as it makes it easier to control and deploy)
- Lambda function, either as a
    - Node, Java, Python application direct
    - Docker container
