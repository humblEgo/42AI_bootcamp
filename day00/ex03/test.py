# test.py

a = {
        'event': {
            'text': 'hello',
            'text2': 'bye'
            },
        'no_event': {
            'text': 'byebye',
            'text2': 'hihi'
            }
    }

if 'hello' == a['event']['text']:
    print("check")
