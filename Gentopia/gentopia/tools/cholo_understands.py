# import requests
# from bs4 import BeautifulSoup
# from gentopia.tools.basetool import BaseTool
# from typing import AnyStr, Optional, Type, Any
# from pydantic import BaseModel, Field
# import os

# class ScrapeArgs(BaseModel):
#     url: str = Field(..., description="The URL of the webpage to scrape.")
#     headers: Optional[dict] = Field(None, description="Optional headers to include in the request.")

# class WebScraper(BaseTool):
#     """Tool that scrapes a web page and returns cleaned text content."""

#     name = "web_scraper"
#     description = "A tool for scraping and cleaning a web page's text content."

#     args_schema: Optional[Type[BaseModel]] = ScrapeArgs

#     def _run(self, url: AnyStr, headers: Optional[dict] = None) -> str:
#         """Scrape the given URL and return cleaned text."""
#         response = requests.get(url, headers=headers)

#         if response.status_code == 200:
#             html_content = response.text
#             soup = BeautifulSoup(html_content, 'html.parser')
#             text_content = soup.get_text(separator='\n').strip()
#             return text_content
#         else:
#             raise ValueError(f"Failed to scrape the webpage. Status code: {response.status_code}")

#     async def _arun(self, *args: Any, **kwargs: Any) -> Any:
#         raise NotImplementedError

# class CholoUnderstandsArgs(BaseModel):
#     url: str = Field(..., description="The URL of the webpage to scrape.")
#     headers: Optional[dict] = Field(None, description="Optional headers for scraping.")

# class CholoUnderstands(BaseTool):
#     """Tool that scrapes a website, cleans the text, and saves it."""

#     name = "cholo_understands"
#     description = "A tool to scrape a website, clean the text, and save it for future use."

#     args_schema: Optional[Type[BaseModel]] = CholoUnderstandsArgs

#     def _run(self, url: AnyStr, headers: Optional[dict] = None) -> str:
#         # Initialize scraper and scrape the text
#         scraper = WebScraper()
#         clean_text = scraper._run(url, headers=headers)

#         # Save the cleaned text to a file
#         with open("cleaned_text.txt", "w", encoding="utf-8") as f:
#             f.write(clean_text)

#         return "Scraped and cleaned text saved to 'cleaned_text.txt'."

#     async def _arun(self, *args: Any, **kwargs: Any) -> Any:
#         raise NotImplementedError


# if __name__ == "__main__":
#     # Example usage for scraping and saving the content
#     cholo = CholoUnderstands()
#     result = cholo._run("https://example.com", headers={"User-Agent": "Mozilla/5.0"})
#     print(result)



import os
from gentopia.tools.basetool import BaseTool
from typing import AnyStr, Optional, Type, Any
from pydantic import BaseModel, Field

class CholoUnderstandsArgs(BaseModel):
    """Arguments to clean the scraped text."""
    file_path: str = Field(..., description="The path to the raw text file.")

class CholoUnderstands(BaseTool):
    """Tool that cleans raw scraped text."""

    name = "cholo_understands"
    description = "A tool to clean raw scraped text and save it for future use."

    args_schema: Optional[Type[BaseModel]] = CholoUnderstandsArgs

    def _run(self, file_path: AnyStr) -> str:
        """Clean the text and save it."""
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                raw_text = f.read()

            # Example cleaning: Removing excess whitespace
            cleaned_text = " ".join(raw_text.split())

            # Save the cleaned text to a new file
            with open("cleaned_text.txt", "w", encoding="utf-8") as f:
                f.write(cleaned_text)

            return "Cleaned text saved to 'cleaned_text.txt'."
        else:
            raise FileNotFoundError(f"The file {file_path} was not found.")

    async def _arun(self, *args, **kwargs):
        raise NotImplementedError


if __name__ == "__main__":
    # Example usage for cleaning and saving text
    cleaner = CholoUnderstands()
    result = cleaner._run("raw_text.txt")
    print(result)
