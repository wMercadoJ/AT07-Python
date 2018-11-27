from behave import *

# use_step_matcher("re")
from compare import expect


@given("I go to gmail page")
def step_impl(context):
    pass


@step("I go to create account")
def step_impl(context):
    pass


@when('I fill name with "{name}"')
def step_impl(context, name):
    """
    :type context: behave.runner.Context
    """
    context.name = name
    print(name)
    # raise NotImplementedError(u'STEP: When I fill name with "Lluvia"')
    expect(name).to_equal("lluvia")


@step('I fill last with "{last_name}"')
def step_impl(context, last_name):
    """
    :type context: behave.runner.Context
    """
    context.last_name = last_name
    expect(last_name).to_equal("Zenteno")


@step('I fill username "{username}"')
def step_impl(context, username):
    """
    :type context: behave.runner.Context
    """
    context.username = username
    print(context.username)


@step('I fill create password with "{password:w}"')
def step_impl(context, password):
    """
    :type context: behave.runner.Context
    """
    print(password)
    context.password = password
    expect(password).to_equal("1234asd")


@step('I fill confirm password with "{confirm_pass:w}"')
def step_impl(context, confirm_pass):
    """
    :type context: behave.runner.Context
    """
    print(confirm_pass)
    context.confirm_pass = confirm_pass


@step('I select month with "{moth:w}" day with {data_day:d} year with {data_year:d}')
def step_impl(context, moth, data_day, data_year):
    """
    :type context: behave.runner.Context
    """
    print(moth + " " + str(data_day) + " " + str(data_year))
    context.moth = moth
    context.data_day = data_day
    context.data_year = data_year


@step('I select gender with "{data_gender:w}"')
def step_impl(context, data_gender):
    """
    :type context: behave.runner.Context
    """
    print(data_gender)
    context.data_gender = data_gender


@step("I fill phone with {data_phone:d}")
def step_impl(context, data_phone):
    """
    :type context: behave.runner.Context
    """
    print(data_phone)
    context.data_phone = data_phone


@step('I fill email address "{email_address}"')
def step_impl(context, email_address):
    """
    :type context: behave.runner.Context
    """
    print(email_address)
    context.email_address = email_address


@then("the data should be saved correctly")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    expect(context.name).to_equal("lluvia")
    expect(context.last_name).to_equal("Zenteno")
    expect(context.username).to_equal("lluvia@gmail.com")
    expect(context.password).to_equal("1234asd")
    expect(context.confirm_pass).to_equal("1234asd")
    expect(context.data_gender).to_equal("female")
    expect(context.data_phone).to_equal(34524856)
    expect(context.email_address).to_equal("lluvia2827@gmail.com")
    print("exit")