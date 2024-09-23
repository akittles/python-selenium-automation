Feature: Sign In page opens

  Scenario: User enters valid email and password combination
    Given Open target main page
    When Click on sign in
    When Click on side window sign in
    Then Verify user on sign_in page
    When User inputs valid email address and password
    And Click on sign in with password
    Then Verify user is logged in

  Scenario: User enters invalid email or phone number
    Given Open target main page
    When Click on sign in
    When Click on side window sign in
    When User inputs invalid email
    And Click on sign in with password
    Then Verify user sees Please enter a valid email or phone number

  Scenario: User enters invalid password
    Given Open target main page
    When Click on sign in
    When Click on side window sign in
    When User inputs invalid password
    And Click on sign in with password
#    Then Verify user sees Please enter a valid password