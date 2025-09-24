// const { Builder, By, Key, until } = require('selenium-webdriver');

const { Builder, By, Key } = require('selenium-webdriver');



(async function example() {

    let driver = await new Builder().forBrowser('chrome').build();

    try {

        await driver.get('https://www.bbc.co.uk');
        await new Promise(resolve => setTimeout(resolve, 2000));

        let reject_button = driver.findElement(By.className("ssrcss-zrxd9q-Button eoocusk1"));
        reject_button.click();
        await new Promise(resolve => setTimeout(resolve, 2000));
        let sport = driver.findElement(By.className("ssrcss-uvrl0v-NavItemHoverState eki2hvo16"));
        sport.click();
        await new Promise(resolve => setTimeout(resolve, 3000));
        let tennis = driver.findElement(By.linkText("Tennis"));
        tennis.click();
        await new Promise(resolve => setTimeout(resolve, 6000));
        await driver.get('https://www.bbc.co.uk/search?d=SPORT_PS');
        let search_text = driver.findElement(By.id("searchInput"));
        search_text.sendKeys("christmas films");
        let search_button = driver.findElement(By.id("searchButton"));
        search_button.click();

        await new Promise(resolve => setTimeout(resolve, 10000));

    } finally {

        await driver.quit();

    }

})();