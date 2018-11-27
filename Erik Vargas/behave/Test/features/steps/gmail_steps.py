from behave import *
from compare import *


@given("I go to gmail page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@when(
    "I fill field {first_name},{last_name},{user_name},{password},{confirm_password},{month},{day},{year},{gender},{phone}, {email}")
def step_impl(context, first_name, last_name, user_name, password, confirm_password, month, day, year, gender, phone,
              email):
    """
    :type context: behave.runner.Context
    :type first_name: str
    :type last_name: str
    :type user_name: str
    :type password: str
    :type confirm_password: str
    :type month: str
    :type day: str
    :type year: str
    :type gender: str
    :type phone: str
    :type email: str
    """
    context.first_name = first_name
    context.last_name = last_name
    context.user_name = user_name
    context.password = password
    context.confirm_password = confirm_password
    context.month = month
    context.day = day
    context.year = year
    context.gender = gender
    context.phone = phone
    context.email = email


@then(
    'should be displayed information "{first_name},{last_name},{user_name},{password},{confirm_password},{month},{day},{year},{gender},{phone}, {email}"')
def step_impl(context, first_name, last_name, user_name, password, confirm_password, month, day, year, gender, phone,
              email):
    """
    :type context: behave.runner.Context
    :type first_name: str
    :type last_name: str
    :type user_name: str
    :type password: str
    :type confirm_password: str
    :type month: str
    :type day: str
    :type year: str
    :type gender: str
    :type phone: str
    :type email: str
    """
    expect(context.first_name).to_equal(first_name)
    expect(context.last_name).to_equal(last_name)
    expect(context.user_name).to_equal(user_name)
    expect(context.password).to_equal(password)
    expect(context.confirm_password).to_equal(confirm_password)
    expect(context.month).to_equal(month)
    expect(context.day).to_equal(day)
    expect(context.year).to_equal(year)
    expect(context.gender).to_equal(gender)
    expect(context.phone).to_equal(phone)
    expect(context.email).to_equal(email)
