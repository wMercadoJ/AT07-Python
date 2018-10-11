Feature: search by google chrome

  Scenario: verify that is possible perform search by google
    Given I go to the page google
    When I into the "python in feature" in the field the page
    And  I click in the button search
    Then should be display the search in the main page