Feature: create a new gmail account

  Scenario Outline: Verify that is possible create a new account
    Given I go to gmail page
    When I fill field <first_name>,<last_name>,<user_name>,<password>,<confirm_password>,<month>,<day>,<year>,<gender>,<phone>, <email>
    Examples:
      | first_name | last_name | user_name | password | confirm_password | month | day | year | gender | phone    | email          |
      | erik       | vargas    | erik123   | 123456   | 123456           | april | 8   | 1992 | male   | 69627086 | erik@gmail.com |
      | beto       | estrada   | beto      | beto     | beto             | may   | 3   | 1992 | male   | 69627086 | erik@gmail.com |
    Then should be displayed information "<first_name>,<last_name>,<user_name>,<password>,<confirm_password>,<month>,<day>,<year>,<gender>,<phone>, <email>"
