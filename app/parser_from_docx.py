"""
Parser from DOCX to ChromaDB
"""
from docx import Document
from chromadb import Client, Collection, GetResult


def parse_docx_to_chromadb(filepath: str, collection_name):
    """
    Parses a DOCX file and adds the parsed data to a ChromaDB collection.
    Args:
        filepath (str): The path to the DOCX file to be parsed.
        chromadb_collection (str):
            The name of the ChromaDB collection to add the parsed data to.
    Returns:
        None
    Raises:
        FileNotFoundError: If the specified DOCX file does not exist.
        ValueError: If the specified ChromaDB collection does not exist.
        Exception: If there is an error during the parsing or adding process.
    """
    client = Client()
    collection = client.get_or_create_collection(collection_name)

    doc = Document(filepath)
    table = doc.tables[0]

    pass

def print_collection_contents(collection: Collection):
    """
    Prints the contents of a collection.
    """
    result = collection.get()

    if result["documents"]:
        print(len(result["documents"]))
        for doc in result["documents"]:
            print(doc)
    else:
        raise ValueError("Collection is empty")


def main():
    """
    Main function
    """

    filepath = "app/data/test_docx.docx"
    parse_docx_to_chromadb(filepath, "Неисправность")
    parse_docx_to_chromadb(filepath, "Вероятсная причина")
    parse_docx_to_chromadb(filepath, "Метод устранения")

    pass

if __name__ == "__main__":
    main()
