# CHANGE TITLE TO LOG IN
Feature: Sign In page opens
  # Enter feature description here

  Scenario: User can open sign in page
    Given Open target main page
    When Click on sign in
    When Click on side window sign in
    Then Verify user on sign_in page
    When User inputs email address and password
    And Click on sign in with password
    Then Verify user is logged in

