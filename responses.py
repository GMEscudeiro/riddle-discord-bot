import random
def handle_response(message):
    p_message = message.lower()
    if p_message == 'enigma':
        return 1, "Level 1", "Level 2"
    if p_message == 'senha':
        return 1, "Level 2", "Level 3"
    return 0, 0, 0
