from behave import *
from compare import *


@given(
    'I enter the URL address "{url:S}" in any browser')
def step_impl(context, url):
    context.url = str(url)
    print("The URL entered is %s" % url)


@when(
    'I fill in the form basics fields "{FirstName}", "{LastName}", "{Username}", "{Password}", "{ConfirmPassword}", "{MobilePhone}", "{CurrentEmailAddress}" with the following information')
def step_impl(context, FirstName, LastName, Username, Password, ConfirmPassword, MobilePhone, CurrentEmailAddress):
    context.first_name = FirstName
    context.last_name = LastName
    context.username = Username
    context.password = Password
    context.confirm_password = ConfirmPassword
    context.mobile_phone = MobilePhone
    context.current_email_address = CurrentEmailAddress


@step('I fill in the form fields "{Month}", "{Day}", "{Year}", "{Gender}" with the following information')
def step_impl(context, Month, Day, Year, Gender):
    context.month = Month
    context.day = Day
    context.year = Year
    context.gender = Gender


@then("I verify that all the fields have been correctly filled in the form")
def step_impl(context):
    if context.password == context.confirm_password:
        expect(context.first_name).to_equals("William")
        expect(context.last_name).to_equals("Claros")
        expect(context.username).to_equals("will.especialista")
        expect(context.mobile_phone).to_equals("79742992")
        expect(context.current_email_address).to_equals("will@hotmail.com")
        expect(context.month).to_equals("May")
        expect(context.day).to_equals("16")
        expect(context.year).to_equals("1990")
        expect(context.gender).to_equals("Male")
