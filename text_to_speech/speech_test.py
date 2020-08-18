from datetime import datetime

from gtts import gTTS


def speech_1(text, sender):
    msg = 'Da: {}. Oggetto: {}'.format(sender, text)
    tts = gTTS(text=msg, lang='it')
    now = datetime.now()
    title = sender.replace(' ', '_') + now.strftime('_%d-%m-%y_%H-%M-%S') + '.mp3'
    print(title)
    tts.save(title)
    print('_________________________________________________________________')


if __name__ == '__main__':
    msg = '''
    So dove abiti. Ti ho visto l'altra sera con il cane.
    Se provi a spaventare Pietro ancora una volta, ti metto una puntina su per il culo.
    '''
    speech_1(msg, 'Pit')
