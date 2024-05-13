from sentence_transformers import SentenceTransformer, util
from torch import Tensor


class SentenceSimilarityClass:

    def __init__(
        self, device: str = "cpu", model_name: str = "sentence-transformers/LaBSE"
    ):
        """
        Initializes the SentenceSimilarity object with the specified device and model name.

        Args:
            device (str): The device to use for the similarity model. Defaults to "cpu".
            model_name (str): The name of the model to use. Defaults to "sentence-transformers/LaBSE".
        """  # noqa: E501
        self.__device = device
        self.__model_name = model_name
        self.__similarity_model = SentenceTransformer(
            self.__model_name, device=self.__device
        )

    def _create_embedding(self, sentences: list[str]) -> Tensor:
        """
        Creates an embedding for the given origin sentence using the pre-trained similarity model.

        Args:
            origin_sentence (list[str]): The sentence for which to create an embedding.

        Returns:
            Tensor: The embedding of the origin sentence as a tensor.

        """  # noqa: E501
        return self.__similarity_model.encode(sentences, convert_to_tensor=True)

    def _get_similarity(self, embeddings_1: Tensor, embeddings_2: Tensor) -> Tensor:
        """
        Calculates the similarity between two embeddings using the pre-trained similarity model.

        Args:
            embedding_1 (Tensor): The first embedding.
            embedding_2 (Tensor): The second embedding.

        Returns:
            Tensor: The similarity between the two embeddings.

        """  # noqa: E501
        return util.pytorch_cos_sim(embeddings_1, embeddings_2)

    def get_similarity_dict(
        self, origin_sentence: str, sentences: list[str]
    ) -> dict[str, float]:
        """
        Calculates the similarity between the origin sentence and a list of sentences.

        Args:
            origin_sentence (str): The original sentence for comparison.
            sentences (list[str]): List of sentences to compare with the origin sentence.

        Returns:
            dict[str, float]: A dictionary containing the similarity score between the origin sentence and each sentence in the list.
        """  # noqa: E501
        original_embedding = self._create_embedding(origin_sentence)
        sentences_embeddings = [
            self._create_embedding(sentence) for sentence in sentences
        ]
        similarity_dict = {
            sentence: self._get_similarity(
                original_embedding, sentence_embedding
            ).item()
            for sentence, sentence_embedding in zip(sentences, sentences_embeddings)
        }
        similarity_dict[origin_sentence] = self._get_similarity(
            original_embedding, original_embedding
        ).item()
        return similarity_dict

    def get_similarity_matrix(self, sentences: list[str]) -> Tensor:
        """
        Calculates the similarity matrix between a list of sentences.

        Args:
            sentences (list[str]): A list of sentences.

        Returns:
            Tensor: The similarity matrix, where each element i,j represents the similarity between sentence i and sentence j.
        """  # noqa: E501
        sentences_embeddings = self._create_embedding(sentences)
        return self._get_similarity(sentences_embeddings, sentences_embeddings)


if __name__ == "__main__":
    ssc = SentenceSimilarityClass()
    test_original_sentence = "Не включилось РУ6"
    test_sentences = [
        "Не включилось РУ6",
        "РУ6 не включилось",
        "не включилось шестое реле управления",
        "Реле РУ6 срабатывает, но не включается реле времени РВ1, РВ2",
        'При нажатии кнопки "Пуск дизеля" (все нужные автоматы включены) КМН не включается.',  # noqa: E501
        'При нажатии кнопки "Пуск дизеля" контактор КМН включается, но маслопрокачивающий насос не работает',  # noqa: E501
        "При пуске прокачка масла есть (60-90 сек), но после отключения КМН пусковые контакторы не включаются",  # noqa: E501
        'При нажатии кнопки "ПД" включаются пусковые контакторы без предварительной прокачки масла',  # noqa: E501
    ]
    semilarity_dict = ssc.get_similarity_dict(test_original_sentence, test_sentences)
    print(semilarity_dict)

    semilatiry_matrix = ssc.get_similarity_matrix(test_sentences)
    print(semilatiry_matrix)
