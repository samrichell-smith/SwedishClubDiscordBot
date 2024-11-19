from random import choice, randint



def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == '':
        return 'Well you\'re awfully silent...'
    elif 'hello' in lowered:
        return 'Hello there!'
    elif 'how are you' in lowered:
        return 'Good, thanks!'
    elif 'bye' in lowered:
        return 'See you later!'
    elif 'roll dice' in lowered:
        return f'You rolled: {randint(1,6)}'
    else:
        return choice(['I don\'t understand...', 'What do you mean?', 'Can you rephrase that?'])