from pytest_bdd import given, when, then, parsers

@then(parsers.parse('je vois \'{text}\''))
def then_text_shown(context, text):
    response = context['response']
    print('text:', text)
    assert text in response.data.decode('utf-8')
