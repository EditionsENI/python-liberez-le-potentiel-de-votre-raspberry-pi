from pydub import AudioSegment


def convert_to_mp3(fichier_in, fichier_out):
    sound = AudioSegment.from_file(fichier_in)
    sound.export(fichier_out, format="mp3", bitrate="128k")


if __name__ == '__main__':
    f_in = "test.wav"
    f_out = "test.mp3"

    convert_to_mp3(f_in, f_out)
