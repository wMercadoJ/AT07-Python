from behave import *


@given(u'these Users')
def step_impl(context):
    for row in context.table:
        assert (True, row['name'] == ('Mich Jackson'))
        print "name ---", row['name']
