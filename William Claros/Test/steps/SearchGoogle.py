from behave import *
from compare import *


@given('I enter the URL "{url:S}" in any browser')
def step_impl(context, url):
    context.url = str(url)
    print("The URL entered is %s" % url)


@when('I enter "{information}" in the input text box')
def step_impl(context, information):
    context.information = information
    print("The information entered is %s" % information)


@step("I pressed the Google Search button")
def step_impl(context):
    pass


@then(
    "I verify that the information in the text box of the search results page matches the information I entered in the initial search engine")
def step_impl(context):
    expect(context.information).to_equals("Wikipedia")
