from behave import *




@given(u'these Users')
def step_impl(context):
    for row in context.table:
        assert (True, row['name'] == ('Michael Jackson'))
        print "name ---", row['name']
