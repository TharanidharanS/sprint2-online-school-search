Feature: To search for school details in eduvidya application

  Scenario:to search for CBSE  school in Pune
    Given user in eduvidya website
    When user click on school
    When user search for school board and location and click on search
    Then user get the school details and user verifies it
    When user take 3 screenshots of the available schools
    When user close the driver

