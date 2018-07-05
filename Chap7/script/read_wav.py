import alsaaudio
import wave


with wave.open('test.wav', 'rb') as w:
    s_sortie = alsaaudio.PCM()
    s_sortie.setchannels(w.getnchannels())
    s_sortie.setrate(w.getframerate())
    s_sortie.setformat(alsaaudio.PCM_FORMAT_S16_LE)
    s_sortie.setperiodsize(1024)
    nom_fichier = w._file.file.name
    print("Nom du fichier lu : ", nom_fichier)

    while True:
        try:
            data = w.readframes(1024)
            if not data:
                break
            s_sortie.write(data)
        except KeyboardInterrupt:
            break

    print("Lecture terminée")
