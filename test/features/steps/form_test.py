from behave import *
from compare import *


@given("I go to page create Google account")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@when('I fill my Name "{name}"')
def step_impl(context, name):
    expect(name).to_equal("Estalin")


@step('I fill my last name "{lastName}"')
def step_impl(context, lastName):
    """
    :type context: behave.runner.Context
    """
    expect(lastName).to_equal("Hurtado")


@step('I fill my new username for new Gmail account "{username}"')
def step_impl(context, username):
    """
    :type context: behave.runner.Context
    """
    expect(username).to_equal("yerelEstalin123")


@step('I fill my new password for my new account "{password}"')
def step_impl(context, password):
    """
    :type context: behave.runner.Context
    """
    expect(password).to_equal("&estalinyerel123&")


@step('I fill my password for confirm "{confirmPassword}"')
def step_impl(context, confirmPassword):
    """
    :type context: behave.runner.Context
    """
    expect(confirmPassword).to_equal("&estalinyerel123&")


@step('I select my month Birthday "{month}"')
def step_impl(context, month):
    """
    :type context: behave.runner.Context
    """
    expect(month).to_equal("july")


@step('I fill my day of Birthday "{day}"')
def step_impl(context, day):
    """
    :type context: behave.runner.Context
    """
    expect(day).to_equal("12")


@step('I fill my year of Birthday "{year}"')
def step_impl(context, year):
    """
    :type context: behave.runner.Context
    """
    expect(year).to_equal("1960")


@step('I select my gender "{gender}"')
def step_impl(context, gender):
    """
    :type context: behave.runner.Context
    """
    expect(gender).to_equal("M")


@step('I select my code "{code:S}" with my number "{number}"')
def step_impl(context, code, number):
    """
    :type context: behave.runner.Context
    """
    expect(code).to_equal("+591")
    expect(number).to_equal("6789123")


@step('I fill my current email address "{email:S}"')
def step_impl(context, email):
    """
    :type context: behave.runner.Context
    """
    expect(email).to_equal("Yerel.Hurtado@fundacion-jala.org")


@then("I should see my new account of Gmail")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass
