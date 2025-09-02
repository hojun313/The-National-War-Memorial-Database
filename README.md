# The National War Memorial Database Scraper

This project is a Python-based web scraper designed to extract war dead data from The National War Memorial of Korea website (warmemo.or.kr). It automates the process of collecting names of fallen soldiers, specifically focusing on various United Nations (UN) branches, and organizes the data into structured Excel files.

## Features

*   **Targeted Scraping**: Currently configured to scrape data for UN Navy, UN Air Force, and UN Marine Corps.
*   **Data Extraction**: Extracts the names of war dead from the website's honor lists.
*   **Excel Output**: Saves the scraped names into `.xlsx` files, formatted with sequential numbering alongside each name.
*   **Error Handling**: Includes basic error handling for network requests and page parsing.
*   **Polite Scraping**: Incorporates delays between requests to avoid overwhelming the server.
*   **Directory Management**: Automatically creates output directories for each branch if they don't exist.

## Project Structure

```
.
├───.gitattributes
├───전체 명단.zip             # A complete dataset
├───combine_army_data.py    # Script for combining army data (if applicable)
├───get_html.py             # Utility for fetching HTML content
├───get_un_total_pages.py   # Script to determine total pages for UN data (if applicable)
├───requirements.txt        # Python dependencies
├───warmemo_scraper.py      # Main scraping script
├───airforce/               # Directory for Air Force data
│   └───war_dead_data_airforce.xlsx
├───army/                   # Directory for Army data
│   └───war_dead_data_army_combined.xlsx
├───marine_corps/           # Directory for Marine Corps data
│   └───war_dead_data_marine_corps.xlsx
├───navy/                   # Directory for Navy data
│   └───war_dead_data_navy.xlsx
├───UN_AIRFORCE/            # Output directory for UN Air Force data
│   └───war_dead_data_UN_AIRFORCE.xlsx
├───UN_ARMY/                # Output directory for UN Army data
│   └───war_dead_data_UN_ARMY.xlsx
├───UN_MARINE_CORPS/        # Output directory for UN Marine Corps data
│   └───war_dead_data_UN_MARINE_CORPS.xlsx
└───UN_NAVY/                # Output directory for UN Navy data
    └───war_dead_data_UN_NAVY.xlsx
```

## Installation

To set up the project, follow these steps:

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/The-National-War-Memorial-Database.git
    cd The-National-War-Memorial-Database
    ```
    *(Note: Replace `your-username` with the actual GitHub username if this project is hosted on GitHub.)*

2.  **Install dependencies**:
    Ensure you have Python installed (Python 3.x is recommended). Then, install the required libraries using `pip`:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To run the scraper and collect data, execute the main scraping script:

```bash
python warmemo_scraper.py
```

The script will start scraping data for the configured UN branches. Progress will be displayed in the console.

## Data Output

Scraped data will be saved in `.xlsx` files within their respective branch directories (e.g., `UN_NAVY/`, `UN_AIRFORCE/`, `UN_MARINE_CORPS/`).

Each Excel file (`war_dead_data_[BRANCH_NAME].xlsx`) will contain the names of the war dead, formatted as follows:

| Column A | Column B | Column C | Column D | ... | Column S | Column T |
| :------- | :------- | :------- | :------- | :-- | :------- | :------- |
| 1        | Name 1   | 2        | Name 2   | ... | 10       | Name 10  |
| 11       | Name 11  | 12       | Name 12  | ... | 20       | Name 20  |
| ...      | ...      | ...      | ...      | ... | ...      | ...      |

Each row contains 10 pairs of (sequential number, soldier's name).
