from pytest_bdd import given, when, then

@given("the app is launched")
def app_is_launched(pages):
    assert pages.navigation.is_app_logo_and_name_visible(), "App logo and name should be visible"

@when("I open the navigation menu")
def open_menu(pages):
    pages.navigation.open_menu()

@then("I should see the Catalog page")
def should_see_catalog_page(pages):
    assert pages.catalog.is_catalog_page_title_visible(), "Catalog page title should be visible"