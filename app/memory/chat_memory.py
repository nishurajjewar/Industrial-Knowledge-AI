# In-memory conversation storage

chat_history = []


def add_message(role, message):
    """
    Save a message to conversation history.
    """

    chat_history.append({
        "role": role,
        "message": message
    })


def get_history():

    return chat_history


def clear_history():

    chat_history.clear()