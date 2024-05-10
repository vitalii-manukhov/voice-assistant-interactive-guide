import wave
from app.asr_class import asr

def test_speech_to_text():
    filepath = ""
    transription = asr.transcribe(filepath)


def test_audio_pcm16():
    for i in range(1, 14):
        filepath = f"data/speech_{i}_pcm16.wav"
        wf = wave.open(filepath, "rb")
        if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
            print("Audio file must be WAV format mono PCM.")
            assert False