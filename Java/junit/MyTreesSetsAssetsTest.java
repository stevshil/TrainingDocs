// filepath: /home/steve/Documents/projects/TrainingDocs/Java/junit/TestMyTreesSets.java

import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class MyTreesSetsAssetsTest {

    @Test
    public void testMultiply() {
        assertEquals(50, 10*5, "10 x 5 must be 50");
    }

    private Person nick;
    private Person steve;
    private People folks;

    @BeforeEach // This will create the object each time
    public void setUp() {
        nick = new Person("Nick",21);
        steve = new Person("Steve", 28);
        folks = new People();
        folks.addPeople(nick);
        folks.addPeople(steve);
    }

    @AfterEach
    public void tearDown() {
        nick = null;
        steve = null;
        folks = null;
    }

    @Test
    public void testPerson() {
        assertTrue(nick instanceof Person);
    }

    @Test
    public void testPersonNameAssigned() {
        assertTrue(steve.getName() == "Steve");
    }

    @Test
    public void testBeginsWithN() {
        assertTrue(folks.getNameBeginningWithN(nick));
    }

    @Test
    public void testDoesNotBeginWithN() {
        assertFalse(folks.getNameBeginningWithN(steve));
    }

}