Feature: Is it Friday yet?
  Everybody wants to know when it's Friday

  Scenario: "<today>" isn't Friday
    Given today is "<today>"
    When I ask whether it's Friday yet
    Then I should be told "<result>"

Examples:
|today|result|
|Sunday|Nope|
|Tuesday|Nope|
|Friday|Hell Yeah!|