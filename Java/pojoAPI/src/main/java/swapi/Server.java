package swapi;

import java.io.IOException;

public class Server {

    public static void main(String[] args) {
        APIOutput server = new APIOutput();
        try {
            server.RunServer();
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
}
