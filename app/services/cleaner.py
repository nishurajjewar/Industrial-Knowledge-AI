import re

def clean_text(text):

    # Remove multiple spaces
    text = re.sub(r'\s+', ' ', text)

    # Remove leading/trailing spaces
    text = text.strip()

    return text