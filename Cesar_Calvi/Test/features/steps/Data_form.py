from behave import *
from compare import *


@given('I enter the google page to create an account')
def step_impl(context):
    pass


@when('I submit the data to the form "{first_name}", "{last_name}", "{choose_email}", "{password}", "{confirm_pass}"')
def step_impl(context, first_name, last_name, choose_email, password, confirm_pass):
    context.first = first_name
    context.last = last_name
    context.choose = choose_email
    context.password = password
    context.confirm = confirm_pass
    print context.confirm, " ---confirm"
    print context.first, " ---first"
    print context.password, " -----pass"
    print context.choose, " ----choose"
    print context.last, " -----last"


@then('The data that is entered should not change and should be saved correctly')
def step_impl(context):
    expect(context.last).to_equal("Calvi")
    expect(context.first).to_equal("Cesar")
    expect(context.confirm).to_equal("cessss1414")
    expect(context.password).to_equal("cessss1414")
    expect(context.choose).to_equal("cesar1414")


@given('I enter the google page to create an account https://accounts.google.com/signup/v2/webcreateaccount?hl=es-419&flowName=GlifWebSignIn&flowEntry=SignUp')
def step_impl(context):
    pass


@when('I submit the data the form "{monday}", "{day}", "{year}", "{gener}", "{mobile_phone}", "{current_email}"')
def step_impl(context, monday, day, gener, year, mobile_phone, current_email):
    context.monday = monday
    context.day = day
    context.year = year
    context.gener = gener
    context.mobile = mobile_phone
    context.current = current_email


@then('The data that is entered should not change and should be saved correctly.')
def step_impl(context):
    expect(context.monday).to_equal("december")
    expect(context.day).to_equal("friday")
    expect(context.year).to_equal("1994")
    print context.gener , "genero"
    expect(context.gener).to_equal("male")
    expect(context.mobile).to_equal("67681749")
    expect(context.current).to_equal("ccalvilujan@gmail.com")
