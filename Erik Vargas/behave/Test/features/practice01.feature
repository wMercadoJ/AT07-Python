Feature: displaye information of a country

Scenario: Verify that it is possible display information of a country
	Given I go to page 
	When I write information
	Then shold be displayed whit zipcode "123455"
	Then display country "inglaterra"
	Then display number of habitants "4.294.967.295"