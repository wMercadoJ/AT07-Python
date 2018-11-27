from behave import *
from compare import *

@given("I go to page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@when('I write information')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass



@then('shold be displayed whit zipcode "{zipcode:d}"')
def step_impl(context, zipcode):
    """
    :type context: behave.runner.Context
    """
    expect(123455).to_equal(zipcode)


@then(u'display country "{country:w}"')
def step_impl(context, country):
	"""
    :type context: behave.runner.Context
    """
	expect("inglaterra").to_equal(country)


@then(u'display number of habitants "{num_habitants:n}"')
def step_impl(context, num_habitants):
	"""
    :type context: behave.runner.Context
    """
	expect(num_habitants).to_equal(num_habitants)
  