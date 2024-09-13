# Created by Owner at 9/9/2024
Feature: Tests for Target App page


  Scenario: User is able to open Privacy Policy
    Given Open Target App page
    And Store original window
    When Click on Privacy Policy link
    And Switch to new window
    Then Verify Privacy Policy page opened
#    And Close current page
#    And Return to original page