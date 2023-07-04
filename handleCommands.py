import os

def handleListNoFlags(text: str):
    if 'list' in text:
        text = text.replace('list', 'ls')

    system_call = os.system(text)


    return system_call