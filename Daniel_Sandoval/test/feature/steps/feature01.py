from behave import *
from compare import *


@given("I add validation steps")
def step_impl(context):
    pass


@when(u'I enter zip code "{110221:d}"')
def step_impl(context, zip_code):
    context.zipcode = zip_code


@step(u'I enter country "{Indonesia:W}"')
def step_impl(context, country):
    context.country_one = country


@step(u'I enter number of population "{4842352147:N}"')
def step_impl(context, habitant):
    context.habitant = habitant


@then("verify than the date enter validate")
def step_impl(context):
    expect(context.zipcode).to_equal("110221")
    expect(context.country_one).to_equals("Indonesia")
    expect(context.habitant).to_equal("4842352147")