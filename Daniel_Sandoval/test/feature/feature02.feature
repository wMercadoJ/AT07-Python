Feature: Create new account

  Scenario Outline: I have crete a new account
    Given fill in the required fields
    When I fill the fields "<first_name>","<last_name>", "<email>", "<password>", "<confirm_password>"
    Then account created
    Examples:
      | first_name | last_name | email         | password | confirm_password |
      | Manuel     | Caseres   | uno@gmail.com | 123456   | 123456           |

  Scenario Outline: I have not create account
    Given I fill the fields with information invalidate
    When I enter "<password>", "<confirm_password>"
    Then I can not create account "<message_error>"
    Examples:
      | password | confirm_password | message_error |
      | probando | qwaszx           | date invalid  |