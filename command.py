import mic as mic
import os
import handleCommands as handle


def main():
    r, microphone = mic.initMic()
    text = mic.getTextFromMic(receiver=r, microphone=microphone)

    if 'option' in text or 'flag' in text:
        print('Functionality for flags not handled yet')
    else:
        system_call_return = handle.handleListNoFlags(text)
        if system_call_return != 0:
            print("Error!\n{0} was not a valid command!".format(text))










if __name__ == '__main__':
    main()