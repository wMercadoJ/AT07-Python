Feature: Create a new gmail account
  Scenario: Create account
    Given I go the create gmail account page
    And I set franz silva on the name field
    And I set franz1234@gmail.com on the user field
    And I set 12franz on the password field
    And I set 12franz on the confirm password field
    And I set 11 11 2001 on the birthdate fields
    And I choose male on the genre field
    And I set 7777777 on the mobile number field
    When I click on create button
    Then The new account should be created
