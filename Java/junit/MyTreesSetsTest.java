// filepath: /home/steve/Documents/projects/TrainingDocs/Java/junit/TestMyTreesSets.java
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

class MyTreesSetsTest {

    @Test
    public void testMultiply() {
        assertEquals(50, 10*5, "10 x 5 must be 50");
    }

    @Test
    public void testPerson() {
        Person me = new Person();
        assertTrue(me instanceof Person);
    }

    @Test
    public void testPersonNameAssigned() {
        Person me = new Person();
        me.setName("Steve");
        assertTrue(me.getName() == "Steve");
    }

    @Test
    public void testBeginsWithN() {
        Person me = new Person("Nick", 24);
        People folks = new People();
        folks.addPeople(me);
        assertTrue(folks.getNameBeginningWithN(me));
    }

    @Test
    public void testDoesNotBeginWithN() {
        Person me = new Person("Steve",28);
        People folks = new People();
        folks.addPeople(me);
        assertFalse(folks.getNameBeginningWithN(me));
    }

}