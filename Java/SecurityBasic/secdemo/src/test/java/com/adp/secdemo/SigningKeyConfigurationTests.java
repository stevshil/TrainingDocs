package com.adp.secdemo;

import java.nio.charset.StandardCharsets;
import javax.crypto.SecretKey;

import com.adp.secdemo.Config.Security;
import com.adp.secdemo.service.JwtService;
import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.runner.ApplicationContextRunner;
import org.springframework.security.oauth2.jwt.JwtDecoder;
import org.springframework.security.oauth2.jwt.JwtEncoder;

import static org.assertj.core.api.Assertions.assertThat;

class SigningKeyConfigurationTests {

    private final ApplicationContextRunner contextRunner = new ApplicationContextRunner()
            .withUserConfiguration(Security.class);

    @Test
    void selectsStaticKey() {
        contextRunner.withPropertyValues(
                "jwt.signingkey=static",
                "jwt.secret=test-only-signing-string-not-for-production"
        ).run(context -> {
            assertThat(context).hasNotFailed().hasSingleBean(SecretKey.class);
            assertThat(context.getBean(SecretKey.class).getEncoded())
                    .isEqualTo("test-only-signing-string-not-for-production".getBytes(StandardCharsets.UTF_8));
            assertTokenRoundTrip(context.getBean(JwtEncoder.class), context.getBean(JwtDecoder.class));
        });
    }

    @Test
    void selectsDynamicKeyWithEmptySecret() {
        contextRunner.withPropertyValues("jwt.signingkey=dynamic", "jwt.secret=").run(context -> {
            assertThat(context).hasNotFailed().hasSingleBean(SecretKey.class);
            assertThat(context.getBean(SecretKey.class).getEncoded()).hasSize(32);
            assertTokenRoundTrip(context.getBean(JwtEncoder.class), context.getBean(JwtDecoder.class));
        });
    }

    @Test
    void rejectsMissingSigningMode() {
        contextRunner.withPropertyValues("jwt.secret=test-only-signing-string-not-for-production")
                .run(context -> assertThat(context).hasFailed());
    }

    @Test
    void rejectsUnsupportedMode() {
        contextRunner.withPropertyValues("jwt.signingkey=unsupported", "jwt.secret=")
                .run(context -> {
                    assertThat(context).hasFailed();
                    assertThat(context.getStartupFailure())
                            .hasRootCauseInstanceOf(IllegalArgumentException.class)
                            .hasRootCauseMessage("Invalid jwt.signingkey value: unsupported");
                });
    }

    @Test
    void rejectsStaticModeWithoutSecret() {
        contextRunner.withPropertyValues("jwt.signingkey=static")
                .run(context -> assertThat(context).hasFailed());
    }

    private void assertTokenRoundTrip(JwtEncoder encoder, JwtDecoder decoder) {
        String token = (String) new JwtService(encoder).createLoginResponse("admin").get("token");
        var jwt = decoder.decode(token);
        assertThat(jwt.getSubject()).isEqualTo("admin");
        assertThat(jwt.getHeaders().get("alg")).isEqualTo("HS256");
    }
}
