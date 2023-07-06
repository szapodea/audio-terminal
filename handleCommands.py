import os

def handleListNoFlags(text: str):
    if 'list' in text:
        text = text.replace('list', 'ls')
    if 'change directory' in text:
        text = text.replace('change directory', 'cd')
    if 'change folder' in text:
        text = text.replace('change folder', 'cd')
    if 'move' in text:
        text = text.replace('move', 'mov')
    if 'root' in text:
        text = text.replace('root', '.')
    if 'back' in text:
        text = text.replace('back', '..')
    if 'dot dot' in text:
        text = text.replace('dot dot', '..')


    system_call = os.system(text)


    return system_call