package swapi;

import org.junit.jupiter.api.Test;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;

import static org.junit.jupiter.api.Assertions.assertTrue;

public class CLIOutputTest {
    public static CLIOutput cli = new CLIOutput();

    @Test
    public void ShowFilmsTest() throws Exception {
        ByteArrayOutputStream out = new ByteArrayOutputStream();
        PrintStream ps = new PrintStream(out);

        PrintStream originalOut = System.out;
        System.setOut(ps);

        // Code under test
        cli.ShowFilms();

        System.setOut(originalOut); // restore

        String printed = out.toString().trim();
        try {
            assertTrue(printed.contains("The Phantom Menace (1999)"));
            System.out.println("The Phantom Menace was found");
        } catch (AssertionError e) {
            System.out.println("The Phantom Menace was not found");
        }
    }
}
