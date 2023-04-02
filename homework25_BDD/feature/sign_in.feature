@sign_in
Feature: Register new user
  We click on button Sign in after that we fill new email and see success message

  Scenario: Outline Test Registration
    Given Open page of internetshop
    When Click on SIGN IN button
    Then Check that we are in new page of registration
    When We are fill form of registration, like name, surname and other
    Then We wil see message of registration is comlete


