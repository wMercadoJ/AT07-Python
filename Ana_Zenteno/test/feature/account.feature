# Created by Admin at 10/11/2018
Feature: create account
  # Enter feature description here

  Scenario: Verify that it can create a account in gmail
    Given I go to gmail page
      And I go to create account
    When I fill name with "lluvia"
      And I fill last with "Zenteno"
      And I fill username "lluvia@gmail.com"
      And I fill create password with "1234asd"
      And I fill confirm password with "1234asd"
      And I select month with "March" day with 2 year with 2018
      And I select gender with "female"
      And I fill phone with 34524856
      And I fill email address "lluvia2827@gmail.com"
    Then the data should be saved correctly