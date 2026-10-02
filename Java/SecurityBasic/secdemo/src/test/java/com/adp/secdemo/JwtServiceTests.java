package com.adp.secdemo;

import com.adp.secdemo.Config.Security;
import com.adp.secdemo.service.JwtService;
import org.junit.jupiter.api.Test;
import org.springframework.security.oauth2.jwt.JwtException;
import org.springframework.test.util.ReflectionTestUtils;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;

class JwtServiceTests {

    private static final String TEST_SECRET =
            "test-only-signing-string-not-for-production";

    private Security configuration(String mode, String secret) {
        Security security = new Security();
        ReflectionTestUtils.setField(security, "jwtSigningKeyType", mode);
        ReflectionTestUtils.setField(security, "jwtSecret", secret);
        return security;
    }

    @Test
    void tokenCanBeDecodedWithSameStringInNewConfiguration() {
        Security original = configuration("static", TEST_SECRET);
        JwtService service = new JwtService(
                original.jwtEncoder(original.jwtSigningKey()));
        String token = (String) service.createLoginResponse("admin").get("token");

        Security restarted = configuration("static", TEST_SECRET);
        var jwt = restarted.jwtDecoder(restarted.jwtSigningKey()).decode(token);

        assertEquals("admin", jwt.getSubject());
        assertEquals("HS256", jwt.getHeaders().get("alg"));
    }

    @Test
    void rejectsTokenSignedWithDifferentKey() {
        Security original = configuration("static", TEST_SECRET);
        JwtService service = new JwtService(
                original.jwtEncoder(original.jwtSigningKey()));
        String token = (String) service.createLoginResponse("admin").get("token");

        Security other = configuration(
                "static", "different-test-only-string-not-for-production");
        var decoder = other.jwtDecoder(other.jwtSigningKey());

        assertThrows(JwtException.class, () -> decoder.decode(token));
    }

    @Test
    void rejectsShortAndBlankKeys() {
        Security shortKey = configuration("static", "short");
        Security blankKey = configuration("static", " ".repeat(32));

        assertThrows(IllegalArgumentException.class, shortKey::jwtSigningKey);
        assertThrows(IllegalArgumentException.class, blankKey::jwtSigningKey);
    }

    @Test
    void dynamicKeySignsAndVerifiesHs256Tokens() {
        Security security = configuration("dynamic", "");
        var key = security.jwtSigningKey();

        assertEquals("HmacSHA256", key.getAlgorithm());
        assertEquals(32, key.getEncoded().length);

        JwtService service = new JwtService(security.jwtEncoder(key));
        String token = (String) service.createLoginResponse("admin").get("token");
        var jwt = security.jwtDecoder(key).decode(token);

        assertEquals("HS256", jwt.getHeaders().get("alg"));
        assertEquals("admin", jwt.getSubject());
    }
}