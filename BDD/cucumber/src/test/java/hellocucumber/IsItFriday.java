package hellocucumber;

import io.cucumber.java.en.Given;
import io.cucumber.java.en.When;
import io.cucumber.java.en.Then;
import static org.assertj.core.api.Assertions.assertThat;

class IsItFriday {
    static String isItFriday(String today) {
        if ("Friday".equals(today)) {
            return "Hell Yeah!";
        } else {
            return "Nope";
        }
    }
}