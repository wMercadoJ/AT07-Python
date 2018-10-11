# Created by yerel-estalin at 10/11/2018
Feature: Google Gmail form
  test form of Google Gmail to test a new account

  Scenario: create a new account of Gmail
    Given I go to page create Google account
    When I fill my Name "Estalin"
      And I fill my last name "Hurtado"
      And I fill my new username for new Gmail account "yerelEstalin123"
      And I fill my new password for my new account "&estalinyerel123&"
      And I fill my password for confirm "&estalinyerel123&"
      And I select my month Birthday "july"
      And I fill my day of Birthday "12"
      And I fill my year of Birthday "1960"
      And I select my gender "M"
      And I select my code "+591" with my number "6789123"
      And I fill my current email address "Yerel.Hurtado@fundacion-jala.org"
    Then I should see my new account of Gmail
