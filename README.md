# Web Scraper

This project is a web scraper that retrieves questions from various websites and saves them in a convenient format. It supports scraping questions from different subjects and years, allowing users to gather a comprehensive collection of questions for their studies or reference.

## Features

- Scrapes questions from multiple websites.
- Supports subjects such as Theory of Computation, Computer Networks, Operating Systems, Database Management System, and Artificial Intelligence.
- Retrieves questions from specific years or batches.
- Saves the scraped questions in a Markdown file for easy readability and formatting.
- Converts the Markdown file to a PDF for offline access or printing.

## Requirements

- Python 3.x
- Requests library (`pip install requests`)
- BeautifulSoup library (`pip install beautifulsoup4`)
- simple_term_menu library (`pip install simple_term_menu`)
- tqdm library (`pip install tqdm`)
- mdpdf command-line tool (Installation instructions: [mdpdf](https://www.npmjs.com/package/mdpdf))

## Usage

1. Clone the repository:

```bash
git clone https://github.com/tyzrex/Old-Question-Scraper
```

2. Install the required Python libraries:

```bash
pip install requests beautifulsoup4 simple_term_menu tqdm mdpdf
```

3. Run the web scraper:

```
python3 scrape-og.py
```

4. Follow the prompts to select the website, subject, and other options for scraping questions.
5. The scraped questions will be saved in a Markdown file named `subjectname.md`. and the resuting PDF file, `subjectname.pdf`, will contain the scraped questions in pdf form.
