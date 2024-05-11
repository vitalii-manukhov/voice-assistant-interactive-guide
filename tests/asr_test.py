"""
    ASR test module.
"""
import wave
# from app.asr_class import Asr


# def test_speech_to_text():
#     """
#     Test stt functionality.
#     """
#     asr = Asr("whisper-small")
#     filepath = "./data/speech_1.wav"
#     transription = asr.transcribe(filepath)


def test_audio_mono_pcm():
    """
    Test audio file format.
    """
    for i in range(1, 14):
        filepath = f"data/speech_{i}_pcm16.wav"
        wf = wave.open(filepath, "rb")
        if (wf.getnchannels() != 1 or
                wf.getsampwidth() != 2 or
                wf.getcomptype() != "NONE"):
            raise ValueError("Audio file must be WAV format mono PCM.")
