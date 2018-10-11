Feature: create a new gmail account

  Scenario Outline: Verify that  it is possible create an account in gmail
    Given I go page page gmail
    And I go click new account
    When I fill the field data with "<first_name>", "<last_name>", "<user_name>", "<create_password>", "<confirm_password>", "<birthday>", "<Gender>", "<email>", "<phone>"
    Examples:

      | first_name | last_name | user_name | create_password | confirm_password | birthday  | Gender | email            | phone    |
      | Karina     | Vargas    | Karina01  | 123456          | 123456           | 2/05/2015 | M      | karina@gmail.com | 72768163 |
    Then I should be displayed on new account
