#Suppose you are going to test the form to create a new gmail account :
# Add the feature file and the scenarios for your testing, in your steps verify that arguments received for each field are specific
#(e.g. Birthday Year only numbers, etc, etc)

Feature: Create a new account in Gmail

  Scenario Outline: Verify that it is possible to create a new account in Gmail.
    Given I enter the URL address "https://accounts.google.com/signup/v2/webcreateaccount?flowName=GlifWebSignIn&flowEntry=SignUp" in any browser
    When I fill in the form basics fields "<FirstName>", "<LastName>", "<Username>", "<Password>", "<ConfirmPassword>", "<MobilePhone>", "<CurrentEmailAddress>" with the following information
      Examples:
      | FirstName | LastName | Username          | Password      | ConfirmPassword | MobilePhone | CurrentEmailAddress |
      | William   | Claros   | will.especialista | William#12345 | William#12345   | 79742992    | will@hotmail.com    |

      And  I fill in the form fields "<Month>", "<Day>", "<Year>", "<Gender>" with the following information
      Examples:
      | Month | Day | Year | Gender |
      | May   | 16  | 1990 | Male   |
    Then I verify that all the fields have been correctly filled in the form