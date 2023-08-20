Feature: Check the functionality of the login page

#  Scenario: Scenariu description
##    Given in what conditions we are working in
##    When actions that we are doing on the page
##    And when2
##    And when3
##    Then checks

  # Scenariu 1: username corect + parola corecta
  ## Scenariu 2: username corect + parola incorecta
  ## Scenariu 3: username incorect + parola corecta
  # Scenariu 4: username incorect + parola incorecta
  ## Scenariu 5: username corect + parola None
  # Scenariu 6: username None + parola corecta
  # Scenariu 7: username None + parola None
  # Scenariu 8: username incorect + parola None
  # Scenariu 9: username None + parola incorecta
  ## Scenariu 10: username blocat (locked_out_user) + parola corecta
  # Scenariu 11: username blocat (locked_out_user) + parola incorecta

  # Scenariu 1
  Scenario: Check that you can login into the application when providing correct credentials
    Given I am on the saucedemo login page
    When I insert correct username and correct password
    And I click on login button
    Then I can login into the application and see the list of products

  # Scenariu 2
  Scenario: Check that you can not login into the application when providing incorrect password
    Given I am on the saucedemo login page
    When I insert correct username and incorrect password
    And I click on login button
    Then I cannot login into the application and I receive the error Epic sadface: Username and password do not match any user in this service

  # Scenariu 3
  Scenario: Check that you can not login into the application when providing incorrect username
    Given I am on the saucedemo login page
    When I insert incorrect username and correct password
    And I click on login button
    Then I cannot login into the application and I receive the error Epic sadface: Username and password do not match any user in this service


   # Scenariu 4
  Scenario: Check that you can not login into the application when providing incorrect username and incorrect password
    Given I am on the saucedemo login page
    When I insert incorrect username and incorrect password
    And I click on login button
    Then I cannot login into the application and I receive the error Epic sadface: Username and password do not match any user in this service

  # Scenariu 5
  Scenario: Check that you can not login into the application whithout providing password
    Given I am on the saucedemo login page
    When I insert correct username and no password
    And I click on login button
    Then I cannot login into the application and I receive the error Epic sadface: Password is required


  # Scenariu 6
  Scenario: Check that you can not login into the application when providing no username and correct password
    Given I am on the saucedemo login page
    When I insert no username and correct password
    And I click on login button
    Then I cannot login into the application and I receive the error Epic sadface: Username is required


  # Scenariu 7
  Scenario: Check that you can not login into the application when providing no username and no password
    Given I am on the saucedemo login page
    When I insert no username and no password
    And I click on login button
    Then I cannot login into the application and I receive the error Epic sadface: Username is required

  # Scenariu 8
  Scenario: Check that you can not login into the application when providing incorrect username and no password
    Given I am on the saucedemo login page
    When I insert incorrect username and no password
    And I click on login button
    Then I cannot login into the application and I receive the error Epic sadface: Password is required

  # Scenariu 9
  Scenario: Check that you can not login into the application when providing no username and incorrect password
    Given I am on the saucedemo login page
    When I insert no username and incorrect password
    And I click on login button
    Then I cannot login into the application and I receive the error Epic sadface: Username is required

  # Scenariu 10
  Scenario: Check that you can not login into the application when providing locked username
    Given I am on the saucedemo login page
    When I insert locked username and correct password
    And I click on login button
    Then I cannot login into the application and I receive the error Epic sadface: Sorry, this user has been locked out.


     # Scenariu 11
  Scenario: Check that you can not login into the application when providing locked username and incorrect password
    Given I am on the saucedemo login page
    When I insert locked username and incorrect password
    And I click on login button
    Then I cannot login into the application and I receive the error Epic sadface: Username and password do not match any user in this service