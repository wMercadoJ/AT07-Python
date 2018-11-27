from behave import given, when, then
from compare import expect


@given(u'I go to the gmail page')
def step_impl(context):
    pass


@given(u'I click in new account')
def step_impl(context):
    pass


@when(
    'I fill the fields with "{first_name}","{last_name}","{choose_email}","{create_pass}","{confirm_pass}","{month}","{day}","{year}","{gender}","{mobile_phone}","{current_email}"')
def step_impl(context, first_name, last_name, choose_email, create_pass, confirm_pass, month, day, year, gender,
              mobile_phone, current_email):
    """
    :type context: behave.runner.Context
    :type first_name: str
    :type last_name: str
    :type choose_email: str
    :type create_pass: str
    :type confirm_pass: str
    :type month: str
    :type day: str
    :type year: str
    :type gender: str
    :type mobile_phone: str
    :type current_email: str
    """
    context.first_name = first_name
    context.last_name = last_name
    context.choose_email = choose_email
    context.create_pass = create_pass
    context.confirm_pass = confirm_pass
    context.month = month
    context.day = day
    context.year = year
    context.gender = gender
    context.mobile_phone = mobile_phone
    context.current_email = current_email
    print(context.first_name, context.last_name)
    print(context.choose_email, context.create_pass)
    print(context.confirm_pass, context.month)
    print(context.day, context.year)
    print(context.gender, context.mobile_phone)
    print(context.current_email)


@then(u'should be created account with the information was create')
def step_impl(context):
    expect(context.first_name).to_equal("Denis")
    expect(context.last_name).to_equal("Camacho")
    expect(context.choose_email).to_equal("denis_cc1720ero")
    expect(context.create_pass).to_equal("QWqw12/*")
    expect(context.confirm_pass).to_equal("QWqw12/*")
    expect(context.month).to_equal("August")
    expect(context.day).to_equal("29")
    expect(context.year).to_equal("1989")
    expect(context.gender).to_equal("male")
    expect(context.mobile_phone).to_equal("69489750")
    expect(context.current_email).to_equal("denissined@gmail.com")
