# import requests
# from bs4 import BeautifulSoup
# from pydantic import BaseModel, Field
# from typing import AnyStr, Optional, Type, Any


# class WebScraperArgs(BaseModel):
#     url: str = Field(..., description="The URL of the webpage to scrape.")
#     headers: Optional[dict] = Field(None, description="Optional headers to include in the request.")


# class WebScraper:
#     """Tool that scrapes a web page and returns cleaned text content."""

#     name = "web_scraper"
#     description = ("A tool for scraping a web page and extracting its text content after cleaning."
#                    "Input should be the URL of the webpage.")

#     args_schema: Optional[Type[BaseModel]] = WebScraperArgs

#     def _run(self, url: AnyStr, headers: Optional[dict] = None) -> str:
#         """Run the tool synchronously and return the extracted and cleaned text from the webpage."""
#         # Send the HTTP request with optional headers
#         response = requests.get(url, headers=headers)

#         # Check if the request was successful
#         if response.status_code == 200:
#             html_content = response.text

#             # Parse the HTML content using BeautifulSoup
#             soup = BeautifulSoup(html_content, 'html.parser')

#             # Extract and clean text (remove all HTML tags)
#             text_content = soup.get_text(separator='\n').strip()

#             return text_content
#         else:
#             raise ValueError(f"Failed to scrape the webpage from {url}. Status code: {response.status_code}")

#     async def _arun(self, *args: Any, **kwargs: Any) -> Any:
#         raise NotImplementedError


# if __name__ == "__main__":
#     # Define the URL and headers
#     url = "https://example.com"  # Replace with your target URL
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
#     }

#     # Example of scraping a webpage
#     scraper = WebScraper()
#     webpage_text = scraper._run(url, headers=headers)

#     # Print the cleaned text
#     print(webpage_text)


import requests
from bs4 import BeautifulSoup
from gentopia.tools.basetool import BaseTool
from typing import AnyStr, Optional, Type, Any
from pydantic import BaseModel, Field

class ScrapeArgs(BaseModel):
    url: str = Field(..., description="The URL of the webpage to scrape.")
    headers: Optional[dict] = Field(None, description="Optional headers to include in the request.")

class WebScraper(BaseTool):
    """Tool that scrapes a web page and saves raw text content."""

    name = "web_scraper"
    description = "A tool for scraping and saving raw web page's text content."

    args_schema: Optional[Type[BaseModel]] = ScrapeArgs

    def _run(self, url: AnyStr, headers: Optional[dict] = None) -> str:
        """Scrape the given URL and save raw text."""
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            html_content = response.text
            soup = BeautifulSoup(html_content, 'html.parser')
            raw_text = soup.get_text(separator='\n').strip()

            # Save raw text to a file
            with open("raw_text.txt", "w", encoding="utf-8") as f:
                f.write(raw_text)

            return "Raw text scraped and saved to 'raw_text.txt'."
        else:
            raise ValueError(f"Failed to scrape the webpage. Status code: {response.status_code}")

    async def _arun(self, *args, **kwargs):
        raise NotImplementedError


if __name__ == "__main__":
    # Example usage for scraping and saving raw content
    scraper = WebScraper()
    result = scraper._run("https://wiki.orc.gmu.edu/mkdocs/Hopper_Quick_Start_Guide/", headers={"User-Agent": "Mozilla/5.0"})
    print(result)



