from pydub import AudioSegment

def get_outpath(filepath: str, format: str) -> str:
    """
    """
    result: str
    if format == "pcm16":
        base = filepath.split('.')[0]
        result = f"{base}_pcm16.wav"
    elif format == "mono":
        base = filepath.split('.')[0]
        result = f"{base}_mono.wav"

    return result

def convert_to_pcm16(filepath):
    """
    example:
    filepath: str = "data/audio.wav"
    convert_to_pcm16(filepath)
    """
    audio = AudioSegment.from_wav(filepath)

    audio = audio.set_sample_width(2)
    outpath = get_outpath(filepath, "pcm16")
    audio.export(outpath, format="wav")

def convert_to_mono(filepath):
    """
    """
    audio = AudioSegment.from_wav(filepath)

    audio = audio.set_channels(1)
    outpath = get_outpath(filepath, "mono")
    audio.export(outpath, format="wav")

# for i in range(1, 14):
#     filepath = f"data/speech_{i}.wav"
#     convert_to_pcm16(filepath)

for i in range(1, 14):
    filepath = f"data/speech_{i}.wav"
    convert_to_mono(filepath)
