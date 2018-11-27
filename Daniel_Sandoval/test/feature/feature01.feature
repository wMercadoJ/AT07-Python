Feature: practice 01

  Scenario: validate date
    Given I add validation steps
    When I enter zip code "110221"
      And I enter country "Indonesia"
      And I enter number of population "4842352147"
    Then verify than the date enter validate