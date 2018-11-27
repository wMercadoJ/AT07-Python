from behave import given, when, then
from compare import expect


@given(u'I go to the page google')
def step_impl(context):
    pass


@when(u'I into the "{text}" in the field the page')
def step_impl(context, text):
    expect("python in feature").to_equal(text)


@when(u'I click in the button search')
def step_impl(context):
    pass


@then(u'should be display the search in the main page')
def step_impl(context):
    pass
