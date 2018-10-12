# Create 1 feature file with 1 scenario :
# Add validation steps for :
#	 ZipCode (only digits)
#    Country (only letters and underscore)
#    Number of Habitants  (number with thousand separator)

Feature: Validate that the fields entered are valid

  Scenario Outline: Validate that the value entered in the zipcode, country and number of habitants fields are valid
    Given I opened the form to enter the data
    When I enter values "<ZipCode>", "<Country>", "<NumberHabitants>" the following fields
    Then The information entered must respect the formats established for each one
    Examples:
      | ZipCode | Country | NumberHabitants |
      | 72046   | England | 60.776.238      |