from behave import *
from compare import *


# -----------------------------------------------------------------
#                           FIRST FEATURE
# -----------------------------------------------------------------

@given("fill in the required fields")
def step_impl(context):
    pass


@when('I fill the fields "{first_name}","{last_name}", "{email}", "{password}", "{confirm_password}"')
def step_impl(context, first_name, last_name, email, password, confirm_password):
    context.name = first_name
    context.last = last_name
    context.username = email
    context.passw = password
    context.confirm = confirm_password


@then("account created")
def step_impl(context):
    expect(context.name).to_equal("Manuel")
    expect(context.last).to_equal("Caseres")
    expect(context.username).to_equal("uno@gmail.com")
    expect(context.passw).to_equal("123456")
    expect(context.confirm).to_equal("123456")


# -----------------------------------------------------------------
#                              SECOND FEATURE
# -----------------------------------------------------------------

@given("I fill the fields with information invalidate")
def step_impl(context):
    pass


@when('I enter "{password}", "{confirm_password}"')
def step_impl(context, password, confirm_password):
    context.passwords = password
    context.confirmpassword = confirm_password


@then('I can not create account "{message_error}"')
def step_impl(context, message_error):
    if context.passwords != context.confirmpassword:
        print(message_error)
