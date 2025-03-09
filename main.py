from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders.parsers import RapidOCRBlobParser
from langchain_community.document_loaders.parsers import TesseractBlobParser
from langchain_community.document_loaders import FileSystemBlobLoader
from langchain_community.document_loaders.generic import GenericLoader
from langchain_community.document_loaders.parsers import PyPDFParser
from pprint import pprint

import os
from dotenv import load_dotenv

load_dotenv()

def simple_text_extractor(file_path):
    """
       Simple Method to extract texts from PDF
    """
    loader = PyPDFLoader(file_path)
    pages = []

    for doc in loader.lazy_load():
        pages.append(doc)
    
    pprint(f"Metadata - {pages[0].metadata}\n")
    pprint(f"Pages Content - {pages[0].page_content}")

    return


def extract_pdf_as_langchain_documents(file_path):
    """
        Each page is extracted as a langchain Document object
        In this mode the pdf is split by pages and the resulting Documents metadata contains the page number. 
    """

    loader = PyPDFLoader(file_path, mode= "page")
    docs = loader.load()
    pprint(f"Type of documents - {type(docs)}\n")
    pprint(f"Pages Content - {docs[0].page_content}")

    return


def extract_pdf_as_single_documents(file_path):
    """
        Extract the whole PDF as a single langchain Document object
    """
    loader = PyPDFLoader(file_path, 
                         mode="single", 
                         pages_delimiter="\n-------THIS IS A CUSTOM END OF PAGE-------\n"
                        )
    docs = loader.load()
    pprint(f"Type of documents - {type(docs)}\n")
    pprint(f"Pages Metadata - {docs[0].metadata}")
    pprint(f"Page Contents - {docs[0].page_content[:5780]}")

    return


def extract_pdf_using_rapidocr(file_path):
    """
        Extract images from the PDF with rapidOCR
    """

    loader = PyPDFLoader(
        file_path,
        mode="page",
        images_inner_format="markdown-img",
        images_parser=RapidOCRBlobParser(),
    )
    docs = loader.load()

    print(docs[0].page_content)

    return


def extract_pdf_using_tesseract(file_path):
    """
        Extract images from the PDF with Tesseract.
        This module doesn't work in my local
    """

    loader = PyPDFLoader(
        file_path,
        mode="page",
        images_inner_format="html-img",
        images_parser=TesseractBlobParser(),
    )
    docs = loader.load()

    print(docs[0].page_content)

    return


def extract_pdf_using_openai(file_path):
    """
       Extracted PDF using OpenAI

    """
    from langchain_community.document_loaders.parsers import LLMImageBlobParser
    from langchain_openai import ChatOpenAI

    loader = PyPDFLoader(
        file_path,
        mode="page",
        images_inner_format="markdown-img",
        images_parser=LLMImageBlobParser(model=ChatOpenAI(model="gpt-4o", max_tokens=1024)),
    )

    docs = loader.load()
    print(docs[6].page_content)

    return

def working_with_files(file_directory):

    loader = GenericLoader(
        blob_loader=FileSystemBlobLoader(
            path=file_directory,
            glob="*.pdf",
        ),
        blob_parser=PyPDFParser(),
    )
    docs = loader.load()
    print(docs[0].page_content)
    pprint(docs[0].metadata)

if __name__ == "__main__":
    file_path = "data/Deepseek-R1-Paper.pdf"
    # simple_text_extractor(file_path)
    # extract_pdf_as_single_documents(file_path)
    # extract_pdf_using_rapidocr(file_path)
    # extract_pdf_using_tesseract(file_path)
    # extract_pdf_using_openai(file_path)
    working_with_files(file_directory="data/")