@Regress @Frontend @Functional @Send_email
Feature: Seznam Email - Send Email

  Scenario: Sending an email with an attachment [AUT-FE]
    Given the user is logged into the application
    When the user sends an email with an attachment
    Then the email should be sent successfully
    And the recipient should receive the email
