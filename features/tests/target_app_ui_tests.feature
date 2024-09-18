# Created by Owner at 9/9/2024
Feature: Tests for Target App page



  Scenario: User is able to open Privacy Policy
    Given Open Target App page
    And Store original window
    When Click on Privacy Policy link
    And Switch to new window
    Then Verify Privacy Policy page opened
    And Close current page
    And Return to original page

    Scenario: User can open and close Terms and Conditions from sign in page
    Given Open target main page
    When Click on sign in
    When Click on side window sign in
    Given Store original window
    When Click on Target terms and conditions link
    And Switch to the newly opened window
    Then Verify Terms and Conditions page is opened
    And User can close new window and switch back to original