import os
from pytest_bdd import scenarios, given, when, then
from tests.mobile.steps.common_steps import *
scenarios("../features/login.feature")

#temp credentials for testing
USERNAME = os.getenv("TEST_USERNAME")
PASSWORD = os.getenv("TEST_PASSWORD")

@when("I login with valid credentials")
def enter_valid_credentials(pages):
    pages.login.login(USERNAME, PASSWORD)

@when("I go to the Log In page")
def go_to_login_page(pages):
    pages.navigation.go_to_login_page()

@then("I should see the Logout button in the navigation menu")
def should_see_logout_button(pages):
    pages.navigation.open_menu()
    assert pages.navigation.is_logout_button_visible(), "Logout button should be visible in the navigation menu"  