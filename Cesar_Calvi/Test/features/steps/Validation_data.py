from behave import *


@when('I will enter the postal "{code}" data, "{country}", "{number}" of inhabitants')
def step_impl(context, code, country, number):
    context.code = code
    context.countre_p = country
    context.number_ha = number
    print "context------", context.code
    print "context------", context.code
    print "context------", context.code


@then('The data should comply with its formats')
def step_impl(context):
    print "numero correc-------", context.code
    print "numero country-------", context.countre_p
    if type(context.code) == int:
        print "numero correc- pass-------", context.code
    if type(context.countre_p) == str:
        print "no es int"
    if type(context.number_ha) == int:
        print  "number----", context.number_ha
