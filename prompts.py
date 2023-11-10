# Response messages
WELCOME_MESSAGE = "Hi, welcome to Emotion Help, you can ask me about certain emotions and how to handle your feelings"
HELP_MESSAGE = "You can ask me about an emotion you're feeling, or, you can say exit... What can I help you with?"
HELP_REPROMPT = "What can I help you with?"
FALLBACK_MESSAGE = "I can't help you with that. I can tell you more about your emotions however",
FALLBACK_REPROMPT = "What can I help you with?"
ERROR_MESSAGE = "Sorry, an error occurred."
STOP_MESSAGE = "Ok Bye"


# Provides emotion details
def get_emotion_info(emotion_name):
    emotion = emotion_name.lower().replace('-', '').replace(' ', '')
    if emotion == 'Happy' or emotion == 'Happiness' or emotion == 'Joy':
        return 'Example Response 1'
    elif emotion == 'Sad' or emotion == 'Saddness':
        return 'Example Response 2'
    elif emotion == 'Angry' or emotion == 'Anger':
        return 'Example Response 3'
    elif emotion == 'Fear' or emotion == 'Scared':
        return 'Example Response 4'
    elif emotion == 'Depression' or emotion == 'Depressed' or emotion == 'Melancholy':
        return 'Example Response 5' \
               'Example Response 5 continued'
    else:
        return 'Im not sure about that emotion'