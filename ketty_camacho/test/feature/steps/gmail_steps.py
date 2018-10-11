from behave import *
from compare import expect


@given(u'I go page page gmail')
def step_impl(context):
    print("you into to page gmail")
    pass


@step(u'I go click new account')
def step_impl(context):
    print("you did click for new account gmail ")
    pass


@when('I fill the field data with "{first_name}", "{last_name}", "{user_name}", "{create_password}", "{confirm_password}", "{birthday}", "{Gender}", "{email}", "{phone}"')
def step_impl(context, first_name, last_name, user_name, create_password, confirm_password, birthday, Gender, email,
              phone):
    """
    :type context: behave.runner.Context
    :type first_name: str
    :type last_name: str
    :type user_name: str
    :type create_password: str
    :type confirm_password: str
    :type birthday: str
    :type Gender: str
    :type email: str
    :type phone: str

    """
    context.first = first_name
    context.last = last_name
    context.name = user_name
    context.password = create_password
    context.confirm_passw = confirm_password
    context.user_birthday = birthday
    context.user_gender = Gender
    context.user_email = email
    context.user_phone = phone
    print(context.first)
    print(context.last)
    print(context.name)
    print(context.password)
    print(context.confirm_passw)
    print(context.user_birthday)
    print(context.user_gender)
    print(context.user_email)
    print(context.user_phone)


@then(u'I should be displayed on new account')
def step_impl(context):
    expect(context.first).to_equal('Karina')
    expect(context.last).to_equal('Vargas')
    expect(context.name).to_equal('Karina01')
    expect(context.password).to_equal('123456')