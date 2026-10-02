package com.adp.secdemo;

import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.webmvc.test.autoconfigure.AutoConfigureMockMvc;
import org.springframework.http.MediaType;
import org.springframework.security.oauth2.jwt.Jwt;
import org.springframework.security.oauth2.jwt.JwtDecoder;
import org.springframework.test.web.servlet.MockMvc;
import tools.jackson.databind.ObjectMapper;

import java.time.Duration;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.post;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.jsonPath;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;

@SpringBootTest(properties = {
        "spring.datasource.url=jdbc:sqlite::memory:",
        "spring.datasource.hikari.maximum-pool-size=1",
        "spring.jpa.hibernate.ddl-auto=create-drop"
})
@AutoConfigureMockMvc
class LoginTests {

    @Autowired
    private MockMvc mockMvc;

    @Autowired
    private ObjectMapper objectMapper;

    @Autowired
    private JwtDecoder jwtDecoder;

    @Test
    void returnsSignedJwtForValidCredentials() throws Exception {
        String response = mockMvc.perform(post("/login")
                        .contentType(MediaType.APPLICATION_JSON)
                        .content("{\"username\":\"admin\",\"password\":\"admin\"}"))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.tokenType").value("Bearer"))
                .andExpect(jsonPath("$.expiresIn").value(3600))
                .andReturn().getResponse().getContentAsString();

        Jwt jwt = jwtDecoder.decode(objectMapper.readTree(response).get("token").asText());
        assertEquals("admin", jwt.getSubject());
        assertEquals("secdemo", jwt.getClaimAsString("iss"));
        assertEquals(Duration.ofHours(1), Duration.between(jwt.getIssuedAt(), jwt.getExpiresAt()));
        assertFalse(jwt.getClaims().containsKey("password"));
    }

    @Test
    void rejectsInvalidCredentials() throws Exception {
        for (String credentials : new String[] {
                "{\"username\":\"admin\",\"password\":\"wrong\"}",
                "{\"username\":\"missing\",\"password\":\"admin\"}"
        }) {
            mockMvc.perform(post("/login").contentType(MediaType.APPLICATION_JSON).content(credentials))
                    .andExpect(status().isUnauthorized());
        }
    }

    @Test
    void rejectsMissingBlankAndMalformedCredentials() throws Exception {
        for (String credentials : new String[] {
                "{}", "{\"username\":\"admin\"}",
                "{\"username\":\" \",\"password\":\"admin\"}",
                "{\"username\":\"admin\",\"password\":\"\"}", "{"
        }) {
            mockMvc.perform(post("/login").contentType(MediaType.APPLICATION_JSON).content(credentials))
                    .andExpect(status().isBadRequest());
        }
    }

    @Test
    void loginRequiresPostAndRootRemainsPublic() throws Exception {
        mockMvc.perform(get("/login")).andExpect(status().isMethodNotAllowed());
        mockMvc.perform(get("/")).andExpect(status().isOk());
    }
}
