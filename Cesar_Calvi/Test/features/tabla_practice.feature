Feature: validation table

  @practice @before_all @before_feature
  Scenario: Validation data of table
    Given these Users:
      | name            | date of birth   |
      | Michael Jackson | August 29, 1958 |
      | Elvis           | January 8, 1935 |
      | John Lennon     | October 9, 1940 |
