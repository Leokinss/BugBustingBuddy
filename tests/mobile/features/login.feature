Feature: Login

  Scenario: Successful login
    Given the app is launched
    When I go to the Log In page
    And I login with valid credentials
    Then I should see the Catalog page
    And I should see the Logout button in the navigation menu