package com.adp.secdemo.Config;

import java.nio.charset.StandardCharsets;
import java.security.NoSuchAlgorithmException;
import javax.crypto.KeyGenerator;
import javax.crypto.SecretKey;
import javax.crypto.spec.SecretKeySpec;

import com.nimbusds.jose.jwk.JWKSet;
import com.nimbusds.jose.jwk.OctetSequenceKey;
import com.nimbusds.jose.jwk.source.ImmutableJWKSet;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.oauth2.jwt.JwtDecoder;
import org.springframework.security.oauth2.jwt.JwtEncoder;
import org.springframework.security.oauth2.jwt.NimbusJwtDecoder;
import org.springframework.security.oauth2.jwt.NimbusJwtEncoder;
import org.springframework.security.oauth2.jose.jws.MacAlgorithm;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

@Configuration
public class Security {

    @Value("${jwt.signingkey}")
    private String jwtSigningKeyType;

    @Value("${jwt.secret:}")
    private String jwtSecret;

    private static final Logger logger = LoggerFactory.getLogger(Security.class);

    @Bean
    public SecretKey jwtSigningKey() {
        if ( jwtSigningKeyType.equals("static")) {
            byte[] keyBytes = jwtSecret.getBytes(StandardCharsets.UTF_8);
            if (jwtSecret.isBlank() || keyBytes.length < 32) {
                throw new IllegalArgumentException("jwt.secret must contain at least 32 UTF-8 bytes and must not be blank");
            }
            logger.info("Using static jwt.secret for signing JWTs");
            return new SecretKeySpec(keyBytes, "HmacSHA256");
        } else if (jwtSigningKeyType.equals("dynamic")) {
            try {
                KeyGenerator generator = KeyGenerator.getInstance("HmacSHA256");
                generator.init(256);
                logger.info("Using dynamic HmacSHA256 key for signing JWTs");
                return generator.generateKey();
            } catch (NoSuchAlgorithmException e) {
                throw new IllegalStateException("Failed to generate HmacSHA256 key", e);
            }
        }
        throw new IllegalArgumentException("Invalid jwt.signingkey value: " + jwtSigningKeyType);
    }

    @Bean
    public JwtEncoder jwtEncoder(@Qualifier("jwtSigningKey") SecretKey jwtSigningKey) {
        OctetSequenceKey key = new OctetSequenceKey.Builder(jwtSigningKey).build();
        return new NimbusJwtEncoder(new ImmutableJWKSet<>(new JWKSet(key)));
    }

    @Bean
    public JwtDecoder jwtDecoder(@Qualifier("jwtSigningKey") SecretKey jwtSigningKey) {
        return NimbusJwtDecoder.withSecretKey(jwtSigningKey).macAlgorithm(MacAlgorithm.HS256).build();
    }
}
