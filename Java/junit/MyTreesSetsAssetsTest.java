// filepath: /home/steve/Documents/projects/TrainingDocs/Java/junit/TestMyTreesSets.java

import org.junit.jupiter.api.*;

import static org.junit.jupiter.api.Assertions.*;

@TestMethodOrder(MethodOrderer.class)
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
    @Order(2)
    public void testPerson() {
        assertTrue(nick instanceof Person);
    }

    @Test
    @Order(1)
    public void testPersonNameAssigned() {
        assertTrue(steve.getName() == "Steve");
    }

    @Test
    @Order(4)
    public void testBeginsWithN() {
        assertTrue(folks.getNameBeginningWithN(nick));
    }

    @Test
    @Order(5)
    public void testDoesNotBeginWithN() {
        assertFalse(folks.getNameBeginningWithN(steve));
    }

}