import wave
import numpy as np

def encode_audio(audio_path: str, message: str, output_path: str):
    """Codifica uma mensagem em um arquivo de áudio"""
    audio = wave.open(audio_path, 'r')
    params = audio.getparams()
    frames = audio.readframes(params.nframes)
    audio.close()

    message_bits = ''.join(format(ord(i), '08b') for i in message) + '1111111111111110'  # Fim da mensagem
    message_bits = list(map(int, message_bits))
    
    audio_data = np.frombuffer(frames, dtype=np.uint8)
    for i in range(len(message_bits)):
        audio_data[i] = (audio_data[i] & 0xFE) | message_bits[i]
    
    encoded_audio = wave.open(output_path, 'w')
    encoded_audio.setparams(params)
    encoded_audio.writeframes(audio_data.tobytes())
    encoded_audio.close()
