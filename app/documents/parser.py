from pathlib import Path

from pypdf import PdfReader
from docx import Document


class DocumentParser:
    """
    Extracts plain text from supported document types.
    """
    def parse(self, file_path: str) -> str:
        """
        Parse a document and return its text content.
        """
        extension = Path(file_path).suffix.lower()

        if extension == ".pdf":
            return self._parse_pdf(file_path)

        elif extension == ".docx":
            return self._parse_docx(file_path)

        elif extension == ".txt":
            return self._parse_txt(file_path)

        raise ValueError(
            f"Unsupported file type: {extension}. "
            "Only PDF, DOCX and TXT files are supported."
        )

    def _parse_pdf(self, file_path: str) -> str:
        reader = PdfReader(file_path)

        pages = []

        for page in reader.pages:
            text = page.extract_text()

            if text:
                pages.append(text)

        return "\n".join(pages)

    def _parse_docx(self, file_path: str) -> str:
        document = Document(file_path)

        paragraphs = []

        for paragraph in document.paragraphs:
            if paragraph.text.strip():
                paragraphs.append(paragraph.text)

        return "\n".join(paragraphs)

    def _parse_txt(self, file_path: str) -> str:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()