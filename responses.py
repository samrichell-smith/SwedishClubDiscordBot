from random import choice, randint



def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == '':
        return 'Well you\'re awfully silent...'
    elif 'hello' or 'hi' in lowered:
        return 'Hej!'
    elif 'how are you' in lowered:
        return 'Jag mår bra tack.'
    elif 'bye' in lowered:
        return 'Hej då!'
    elif 'roll dice' in lowered:
        return f'Du rullade en {randint(1,6)}'
    elif 'club' in lowered:
        return 'University of Auckland Swedish Club is a newly formed (2023) club focussing on appreciating Swedish culture!'
    else:
        return choice(['Jag förstår inte (I don\'t understand...)', 'Vad menar du? (What do you mean?)',
                        'Kan du omformulera det? (Can you rephrase that?)'])
