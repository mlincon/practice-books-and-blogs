import os
from urllib import parse

import requests
from bs4 import BeautifulSoup


def download_main(url: str, output_dir: str):
    """Download all the html pages from a provided link.

    Args:
        url (str): the URL to scrape
        output_dir (str): the directory to store files in
    """

    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Fetch the page
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all links to .html files
    links = soup.find_all("a", href=True)

    for link in links:
        href = link["href"]

        # If it's a .html file
        if href.endswith(".html"):
            # Make a full URL if necessary
            if not href.startswith("http"):
                href = parse.urljoin(url, href)

            # Fetch the .html file
            print(f"downloading {href}")
            file_response = requests.get(href)

            # Write it to a file
            file_name = os.path.join(output_dir, os.path.basename(href))
            with open(file_name, "w", encoding="utf-8") as file:
                file.write(file_response.text)


if __name__ == "__main__":
    download_main(
        url="https://docs.llamaindex.ai/en/stable/",
        output_dir="./llamaindex-docs/",
    )
