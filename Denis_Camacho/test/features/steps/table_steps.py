from behave import given


@given(u'these Users')
def step_impl(context):
    for row in context.table:
        print(row['name'])
        print(row['date of birth'])
    pass
