from torch.hub import load
from torch import Tensor
import soundfile


class TextToSpeechClass:
    def __init__(self, device: str = "cpu"):
        """
        Initializes the TextToSpeechClass object with the specified device.

        Args:
            device (str): The device to use. Defaults to "cpu".
        """
        self.__language = "ru"
        self.__model_id = "v4_ru"
        self.__model_name = "silero_tts"
        self.__repository = "snakers4/silero-models"
        self.__sample_rate = 48000
        self.__speaker = "baya"
        self.__device = device

        self.__model, _ = load(
            repo_or_dir=self.__repository,
            model=self.__model_name,
            language=self.__language,
            speaker=self.__model_id,
            device=self.__device,
        )

    def _get_audio_from_text(self, text: str) -> Tensor:
        """
        Generates audio from the input text using the Text-to-Speech model.

        Args:
            text (str): The input text to convert to audio.

        Returns:
            Tensor: The generated audio tensor.
        """
        audio = self.__model.apply_tts(
            text=text, speaker=self.__speaker, sample_rate=self.__sample_rate
        )
        return audio

    def _save_audio(self, audio: Tensor, path: str):
        """
        Saves the given audio tensor to a file at the specified path.

        Args:
            audio (Tensor): The audio tensor to save.
            path (str): The path to the file where the audio will be saved.

        Returns:
            None
        """
        soundfile.write(path, audio.numpy(), samplerate=self.__sample_rate)

    def text_to_speech(self, text: str):
        """
        Converts the given text into speech and saves it as a WAV file.

        Parameters:
            text (str): The text to be converted into speech.

        Returns:
            None
        """
        audio = self._get_audio_from_text(text)
        self._save_audio(audio, "./resources/output.wav")


if __name__ == "__main__":
    tts = TextToSpeechClass()
    tts.text_to_speech("Не включилось шестое реле управления")
