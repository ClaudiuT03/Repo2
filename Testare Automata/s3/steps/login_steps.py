from behave import *


@given('I am on the saucedemo login page')
def step_impl(context):
    """
    CONTEXT este in primul rand un parametru pe care
    toate functiile/implementarile de pasi (scenario steps)
    il vor avea.

    El reprezinta o cutiuta in care pot sa stochez informatii
    precum: informatii despre browser, alte pagini etc definite/adaugate
    din fisierul environment.py
    """
    context.login_page_object.navigate_to_login_page()


@when('I insert correct username and correct password')
def step_impl(context):
    context.login_page_object.insert_correct_username()
    context.login_page_object.insert_correct_password()

@when('I insert correct username and incorrect password')
def step_impl(context):
    context.login_page_object.insert_correct_username()
    context.login_page_object.insert_incorrect_password()


@when('I click on login button')
def step_impl(context):
    context.login_page_object.click_login_btn()


@when('I insert incorrect username and correct password')
def step_impl(context):
    context.login_page_object.insert_incorrect_username()
    context.login_page_object.insert_correct_password()


@when('I insert incorrect username and incorrect password')
def step_impl(context):
    context.login_page_object.insert_incorrect_username()
    context.login_page_object.insert_incorrect_password()


@when('I insert correct username and no password')
def step_impl(context):
    context.login_page_object.insert_correct_username()


@when('I insert incorrect username and no password')
def step_impl(context):
    context.login_page_object.insert_incorrect_username()


@when('I insert no username and correct password')
def step_impl(context):
    context.login_page_object.insert_correct_password()


@when('I insert no username and incorrect password')
def step_impl(context):
    context.login_page_object.insert_incorrect_password()


@when('I insert locked username and incorrect password')
def step_impl(context):
    context.login_page_object.insert_locked_username()
    context.login_page_object.insert_incorrect_password()


@when('I insert no username and no password')
def step_impl(context):
    pass

@when('I insert locked username and correct password')
def step_impl(context):
    context.login_page_object.insert_locked_username()
    context.login_page_object.insert_correct_password()


@then('I can login into the application and see the list of products')
def step_impl(context):
    context.inventory_page_object.check_current_url()


@then('I cannot login into the application and I receive the error Epic sadface: Username and password do not match any user in this service')
def step_impl(context):
    expected_err_msg = 'Epic sadface: Username and password do not match any user in this service'
    context.login_page_object.check_error_message(expected_err_msg)


@then('I cannot login into the application and I receive the error Epic sadface: Password is required')
def step_impl(context):
    expected_err_msg = 'Epic sadface: Password is required'
    context.login_page_object.check_error_message(expected_err_msg)


@then('I cannot login into the application and I receive the error Epic sadface: Sorry, this user has been locked out.')
def step_impl(context):
    expected_err_msg = 'Epic sadface: Sorry, this user has been locked out.'
    context.login_page_object.check_error_message(expected_err_msg)


@then('I cannot login into the application and I receive the error Epic sadface: Username is required')
def step_impl(context):
    expected_err_msg = 'Epic sadface: Username is required'
    context.login_page_object.check_error_message(expected_err_msg)
