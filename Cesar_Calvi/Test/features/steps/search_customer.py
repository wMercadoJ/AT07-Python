from behave import *
from  compare import *


@given('I entered the google page https://www.google.com')
def step_impl(contex):
    pass


@when('I will enter the text of "{Python}"')
def step_when(contex,Python):
    print "d----------", Python
    pass


@when('Press enter')
def steep_press(contex):
    pass


@then('I will make sure that when I upload a page that contains "{Python}"')
def step_compare(context, Python):
    expect(Python).to_equal("Python")