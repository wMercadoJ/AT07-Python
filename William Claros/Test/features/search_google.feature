# Make a feature that verifies that you can perform any search for information on Google.

Feature: Perform a search using the Google search engine.

  Scenario: Perform the search for information through the Google search engine.
    Given I enter the URL "www.google.com" in any browser
    When I enter "Wikipedia" in the input text box
      And I pressed the Google Search button
    Then I verify that the information in the text box of the search results page matches the information I entered in the initial search engine