Feature: google search engine homepage

  Scenario: For this scenario it will be proved that a basic search can be done
    Given I entered the google page https://www.google.com
    When I will enter the text of "Python"
    And Press enter
    Then I will make sure that when I upload a page that contains "Python"
