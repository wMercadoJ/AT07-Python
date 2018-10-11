Feature: In this feature the fields of postal code, number of country, number of inhabitants are validated

  @slow
  Scenario Outline: Validation of which the data of postal code, country and room numbers follow a pattern
    When  I will enter the postal "<code>" data, "<country>", "<number>" of inhabitants
    Then The data should comply with its formats
    Examples:
      | code     | country   | number     |
      | 45458745 | Australia | 24,000,000 |
      | 45458    | Bolivia   | 12,000,000 |

