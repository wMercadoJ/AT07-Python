Feature: Create a Gmail account


  @email
  Scenario Outline: Create an account with valid data
    Given I enter the google page to create an account
    When I submit the data to the form "<first_name>", "<last_name>", "<choose_email>", "<password>", "<confirm_pass>"
    Then The data that is entered should not change and should be saved correctly
    Examples:
      | first_name | last_name | choose_email | password   | confirm_pass |
      | Cesar      | Calvi     | cesar1414    | cessss1414 | cessss1414   |


  @email
  Scenario Outline:Create account with valid data.
    Given I enter the google page to create an account https://accounts.google.com/signup/v2/webcreateaccount?hl=es-419&flowName=GlifWebSignIn&flowEntry=SignUp
    When I submit the data the form "<monday>", "<day>", "<year>", "<gener>", "<mobile_phone>", "<current_email>"
    Then The data that is entered should not change and should be saved correctly.
    Examples:
      | monday   | day    | year | gener | mobile_phone | current_email         |
      | december | friday | 1994 | male  | 67681749     | ccalvilujan@gmail.com |