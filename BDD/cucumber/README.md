This example is taken from https://cucumber.io/docs/guides/10-minute-tutorial/

To have HTML reports;

See the src/test/resources/junit-platform.properties and pom.xml for allure

Run the command

```
npm install -g allure-commandline --save-dev
```

To generate the report

```
allure generate allure-results --clean -o target/allure-report
allure open target/allure-report
```