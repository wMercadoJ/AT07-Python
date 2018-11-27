Feature: table

  @my_tags
  Scenario: verify that is possible .
    Given these Users:
      | name            | date of birth   |
      | Michael Jackson | August 29, 1958 |
      | Elvis           | January 8, 1935 |
      | John Lennon     | October 9, 1940 |

  @regression
  Scenario: verify that is possible to .
    Given these Users:
      | name            | date of birth   |
      | Michael Jackson | August 29, 1958 |
      | Elvis           | January 8, 1935 |
      | John Lennon     | October 9, 1940 |
