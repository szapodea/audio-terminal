import speech_recognition as sr


def initMic():
    micIndex = None  # Microphone index
    micName = "MacBook Pro Microphone"  # Microphone Name

    # Setting up correct Microphone
    workingMics = sr.Microphone.list_microphone_names()

    for micVal, name in enumerate(workingMics):
        if micName == name:
            micIndex = micVal

    if micIndex is None:
        print(micName, "not Found, using default")

    r = sr.Recognizer()
    mic = sr.Microphone(device_index=micIndex)
    return r, mic


def getTextFromMic(receiver, microphone):
    try:
        with microphone as source:
            receiver.adjust_for_ambient_noise(source, duration=.5)
            # listens for the user's input
            print("Listening...")
            audio = receiver.listen(source, timeout=10)

            myText = receiver.recognize_google(audio)
            myText = myText.lower()
            #TODO: Handle not connected to internet error

            # Potential Formatting
            # MyText = MyText.capitalize()

            return myText

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        print("unknown error occurred")