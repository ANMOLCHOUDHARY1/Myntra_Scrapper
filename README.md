# Myntra Scrapper

**Myntra Scrapper** is a Python-based web scraper that automates the extraction of product data and images from Myntra's website. The scraper collects product titles, prices, specifications, and up to 500 product images, storing them in a structured directory with metadata in JSON format. This project is ideal for collecting large datasets from Myntra for analysis or research.

## Features

- **Automated Scraping**: Retrieves product links based on search queries and collects metadata such as titles, prices, and specifications.
- **Image Collection**: Downloads product images and stores them in a well-organized directory.
- **Customizable**: Set the number of images or products to scrape. (Default: 500 images)
- **Graceful Stop**: The scraper can be manually stopped, and all data up to that point will be saved.
- **Data Storage**: Stores metadata in JSON format and images in a folder structure for easy access.

## Requirements

- Python 3.x
- Selenium
- WebDriver Manager for Chrome
- Google Chrome

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/ANMOLCHOUDHARY1/Myntra_Scrapper.git
    cd Myntra_Scrapper
    ```

2. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Ensure you have Google Chrome installed on your system.

## Usage

1. Create a file named `clothings.txt` in the root directory with search queries, one per line (e.g., `shoes`, `t-shirts`).

2. Run the scraper:
    ```bash
    python scrapper.py
    ```

3. The scraper will start extracting product data and images based on the search queries in `clothings.txt`. The data will be stored in the `data/` folder, structured by product ID, with images and metadata saved in corresponding subfolders.

## Directory Structure

Myntra_Scrapper/ 
├── clothings.txt # Search queries 
├── data/ # Directory where scraped data will be stored 
│ ├── product_id/ # Folder for each product 
│ │ ├── images/ # Images of the product 
│ │ └── metadata.json # Product metadata 
├── scrapper.py # Main scraper script 
└── requirements.txt # Required Python packages



## Customization

- Modify the default number of images or products to scrape by editing the script.
- You can stop the scraper at any point manually, and all data collected up to that point will be saved.

## Contributing

Feel free to submit issues, fork the repository, and send pull requests to contribute to this project.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.


Feel free to submit issues, fork the repository, and send pull requests to contribute to this project.
