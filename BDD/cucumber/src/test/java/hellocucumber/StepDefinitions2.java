package hellocucumber;

import io.cucumber.java.en.*;

import static org.assertj.core.api.Assertions.assertThat;

public class StepDefinitions2 {
    private String today;
    private String actualAnswer;

    @Given("Friday's number is {int}")
    public void fridays_number_is(Integer int1) {
        today = "Friday";
    }

    @When("I ask for Friday's number")
    public void i_ask_for_friday_s_number() {
        actualAnswer = String.valueOf(IsItFriday.fridayNum(today));
    }

    @Then("I should be told {int}")
    public void i_should_be_told(Integer int1) {
        assertThat(actualAnswer).isEqualTo(String.valueOf(int1));
    }
}
