# Created by Owner at 10/31/2024
Feature: Reelly sign-in page
  # Enter feature description here

  Scenario: User can go to sign in page
    Given Open Reelly main page
    When Click on open in browser button
    Then Verify user on signin page


  Scenario: Check UI on sign in page
    Given Open Reelly sign-in page
    Then Verify signin page UI