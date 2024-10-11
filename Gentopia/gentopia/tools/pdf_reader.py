# from PyPDF2 import PdfReader
# from gentopia.tools.basetool import *
# from typing import AnyStr, Optional, Type
# from pydantic import BaseModel, Field


# class PDFReaderArgs(BaseModel):
#     file_path: str = Field(..., description="The file path to the PDF file to read.")


# class PDFReader(BaseTool):
#     """Tool that reads a PDF and returns its text content."""

#     name = "pdf_reader"
#     description = ("A tool for reading PDF files and extracting their content as plain text."
#                    "Input should be the path to the PDF file.")

#     args_schema: Optional[Type[BaseModel]] = PDFReaderArgs

#     def _run(self, file_path: AnyStr) -> str:
#         """Run the tool synchronously and return the extracted text from the PDF."""
#         with open(file_path, 'rb') as file:
#             reader = PdfReader(file)
#             text = ""
#             for page in reader.pages:
#                 text += page.extract_text()
#         return text

#     async def _arun(self, *args: Any, **kwargs: Any) -> Any:
#         raise NotImplementedError


# if __name__ == "__main__":
#     # Example of reading a PDF file
#     pdf_text = PDFReader()._run("sample.pdf")
#     print(pdf_text)


import requests
from PyPDF2 import PdfReader
from gentopia.tools.basetool import *
from typing import AnyStr, Optional, Type
from pydantic import BaseModel, Field
import os

class PDFReaderArgs(BaseModel):
    file_path: str = Field(..., description="The file path to the PDF file or URL to read.")


class PDFReader(BaseTool):
    """Tool that reads a PDF and returns its text content."""

    name = "pdf_reader"
    description = ("A tool for reading PDF files and extracting their content as plain text."
                   "Input should be the path to the PDF file or a URL pointing to a PDF file.")

    args_schema: Optional[Type[BaseModel]] = PDFReaderArgs

    def _download_pdf(self, url: str) -> str:
        """Downloads a PDF from the given URL and saves it locally."""
        local_filename = "downloaded_pdf.pdf"
        response = requests.get(url)
        if response.status_code == 200:
            with open(local_filename, 'wb') as f:
                f.write(response.content)
            return local_filename
        else:
            raise ValueError(f"Failed to download PDF from {url}. Status code: {response.status_code}")

    def _run(self, file_path: AnyStr) -> str:
        """Run the tool synchronously and return the extracted text from the PDF."""
        # Check if the input is a URL
        if file_path.startswith("http://") or file_path.startswith("https://"):
            # Download the PDF from the URL
            file_path = self._download_pdf(file_path)

        # Read the PDF file
        with open(file_path, 'rb') as file:
            reader = PdfReader(file)
            text = ""
            for page in reader.pages:
                text += page.extract_text()

        # Clean up downloaded PDF if applicable
        if os.path.exists("downloaded_pdf.pdf"):
            os.remove("downloaded_pdf.pdf")

        return text

    async def _arun(self, *args: Any, **kwargs: Any) -> Any:
        raise NotImplementedError


if __name__ == "__main__":
    # Example of reading a PDF file or downloading it from a URL
    pdf_text = PDFReader()._run("https://www.bbau.ac.in/Docs/FoundationCourse/TM/AECC105/Grammar.pdf")
    print(pdf_text)





