package hellocucumber;

import io.cucumber.java.en.*;

import static org.assertj.core.api.Assertions.assertThat;

public class StepDefinitions {
    private String today;
    private String actualAnswer;

    @Given("today is {string}")
    public void today_is_Sunday(String day) {
        today = day;
    }

    @When("I ask whether it's Friday yet")
    public void i_ask_whether_it_s_Friday_yet() {
        actualAnswer = IsItFriday.isItFriday(today);
    }

    @Then("I should be told {string}")
    public void i_should_be_told(String expectedAnswer) {
        assertThat(actualAnswer).isEqualTo(expectedAnswer);
    }
}
