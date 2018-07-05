import alsaaudio
import wave


micro_yeti = 'sysdefault:CARD=Microphone'

s_entree = alsaaudio.PCM(alsaaudio.PCM_CAPTURE, alsaaudio.PCM_NONBLOCK,
                         micro_yeti)
s_entree.setchannels(1)
s_entree.setrate(44100)
s_entree.setformat(alsaaudio.PCM_FORMAT_S16_LE)
s_entree.setperiodsize(1024)

with wave.open('test.wav', 'w') as w:
    w.setnchannels(1)
    w.setsampwidth(2)
    w.setframerate(44100)
    print("Enregistrement en cours... \n Pour le stopper faites <CTLR> + C")

    while True:
        try:
            _, data = s_entree.read()
            w.writeframes(data)
        except KeyboardInterrupt:
            break
    print("Enregistrement terminé")
