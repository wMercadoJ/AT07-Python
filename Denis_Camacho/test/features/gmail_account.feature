Feature: create a new email account

  Scenario Outline: verify that is possible create an account.
    Given I go to the gmail page
    And I click in new account
    When I fill the fields with "<first_name>","<last_name>","<choose_email>","<create_pass>","<confirm_pass>","<month>","<day>","<year>","<gender>","<mobile_phone>","<current_email>"
    Then should be created account
    Examples:
      | first_name | last_name | choose_email    | create_pass | confirm_pass | month  | day | year | gender | mobile_phone | current_email        |
      | Denis      | Camacho   | denis_cc1720ero | QWqw12/*    | QWqw12/*     | August | 29  | 1989 | male   | 69489750     | denissined@gmail.com |