"""
Module for ASR (Automatic Speech Recognition)

This module provides a class for ASR transcription.

"""
from typing import Any
import whisper
import nemo.collections.asr as nemo_asr


class Asr:
    """
    ASR class for transcription.

    Attributes:
        model_name (str):
            The name of the model to use for transcription.
        model (Any):
            The model to use for transcription.

    Methods:
        transcribe(self, filepath: str)
        set_model(self, model_name: str)
        get_model(self)
    """
    def __init__(self, model_name: str) -> None:
        """
        Initialize the ASR class with the specified model.
        Args:
            model_name (str):
                The name of the model to use for transcription.
        Returns:
            None
        Raises:
            ValueError: If the specified ASR model is not supported.
        """
        try:
            if model_name not in ["whisper-small", "nvidia-nemo-asr"]:
                raise ValueError("The specified ASR model is not supported.")
            self.model_name = model_name
            if model_name == "whisper-small":
                self.model = whisper.load_model("small")
            elif model_name == "nvidia-nemo-asr":
                model = nemo_asr.models.EncDecRNNTBPEModel.from_pretrained(
                    "nvidia/stt_ru_conformer_transducer_large"
                )
                self.model = model
        except ValueError as exc:
            raise ValueError(
                "The specified ASR model is not supported."
            ) from exc

    def transcribe(self, filepath: str) -> str:
        """
        Transcribes the audio file using the specified ASR model.
        Args:
            filepath (str): The path to the audio file to be transcribed.
        Returns:
            str: The transcribed text.
        """
        if self.model_name == "whisper-small":
            result = self.model.transcribe(filepath, language="ru", fp16=False)
            return result["text"]
        elif self.model_name == "nvidia-nemo-asr":
            result = self.model.transcribe([filepath])
            return result
        else:
            raise ValueError("The specified ASR model is not supported.")

    def set_model(self, model_name: str) -> None:
        """
        Sets the model for the ASR class.
        Args:
            model_name (str):
                The name of the model to set.
                Valid options are "whisper-small" and "nvidia-nemo-asr".
        Returns:
            None
        Raises:
            ValueError: If the specified ASR model is not supported.
        """
        try:
            if model_name not in ["whisper-small", "nvidia-nemo-asr"]:
                raise ValueError("The specified ASR model is not supported.")

            self.model_name = model_name
            if model_name == "whisper-small":
                self.model = whisper.load_model("small")
            elif model_name == "nvidia-nemo-asr":
                model = nemo_asr.models.EncDecRNNTBPEModel.from_pretrained(
                    "nvidia/stt_ru_conformer_transducer_large"
                )
                self.model = model
        except ValueError as exc:
            raise ValueError(
                "The specified ASR model is not supported."
            ) from exc

    def get_model(self) -> Any:
        """
        Get the model used by the ASR class.
        Returns:
            Any: The model used by the ASR class.
        """
        return self.model
