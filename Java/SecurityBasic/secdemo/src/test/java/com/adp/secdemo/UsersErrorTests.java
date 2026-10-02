package com.adp.secdemo;

import com.adp.secdemo.controller.Restricted;
import com.adp.secdemo.controller.UsersExceptionHandler;
import com.adp.secdemo.repository.UsersRepository;
import org.junit.jupiter.api.Test;
import org.springframework.dao.DataAccessResourceFailureException;
import org.springframework.http.MediaType;
import org.springframework.test.web.servlet.MockMvc;
import org.springframework.test.web.servlet.setup.MockMvcBuilders;

import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.when;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.content;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;

class UsersErrorTests {

    @Test
    void returnsJsonErrorWithoutExposingDatabaseDetails() throws Exception {
        UsersRepository repository = mock(UsersRepository.class);
        when(repository.findAll())
                .thenThrow(new DataAccessResourceFailureException("Internal database connection details"));
        MockMvc mockMvc = MockMvcBuilders.standaloneSetup(new Restricted(repository))
                .setControllerAdvice(new UsersExceptionHandler())
                .build();

        mockMvc.perform(get("/users"))
                .andExpect(status().isInternalServerError())
                .andExpect(content().contentTypeCompatibleWith(MediaType.APPLICATION_JSON))
                .andExpect(content().json("{\"code\":500,\"message\":\"Unable to retrieve users\"}"));
    }
}
