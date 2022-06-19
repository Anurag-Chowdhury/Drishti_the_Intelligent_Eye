import cv2
import modules.functions as function
import modules.speech as speech
import modules.getIntent as Intent

# create an object from speech module
engine = speech.Speech()
listening = False
intent = None

while True:
    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    if not listening:
        resp = engine.recognize_speech()
        if(resp != None):
            intent = Intent.get_intent(resp)
        if(intent == 'drishti' and resp != None):
            listening = True

    else:
        engine.text_to_speech("What can I help you with?")
        intent = ''
        engine.text_to_speech("Listening")
        resp = engine.recognize_speech()
        engine.text_to_speech("Processing")

        if(resp != None):
            intent = Intent.get_intent(resp)
            intent = intent.lower()

            if(intent == 'describe'):
                print("description of the scene")

            elif(intent == 'read'):
                print("read the text")

            elif(intent == 'play'):
                function.play_file("audio_files/sound.mp3")

            elif(intent == 'brightness'):
                function.get_brightness(cam=cam)

            elif(intent == 'time'):
                function.get_time()

            else:
                # no intent matched
                engine.text_to_speech(
                    "Sorry, I did not understood. Can you say it again?")

    cam.release()
