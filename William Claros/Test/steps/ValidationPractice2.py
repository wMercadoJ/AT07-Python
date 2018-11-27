from behave import *
from compare import *


@given("I opened the form to enter the data")
def step_impl(context):
    pass


@when('I enter values "{ZipCode}", "{Country}", "{NumberHabitants}" the following fields')
def step_impl(context, ZipCode, Country, NumberHabitants):
    context.zipcode = ZipCode
    context.country = Country
    context.number_habitants = NumberHabitants


@then("The information entered must respect the formats established for each one")
def step_impl(context):
    expect(context.zipcode).to_equals("72046")
    expect(context.country).to_equals("England")
    expect(context.number_habitants).to_equals("60,776,238")


