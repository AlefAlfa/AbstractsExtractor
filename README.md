# Abstracts Extractor

Extract and process abstracts from emails labeled as "Papers" in your Gmail account, and get them cleaned up using the power of gpt-3.5-turbo.

## Table of Contents
1. [Features](#features)
2. [Setup and Installation](#setup-and-installation)
    - [Requirements Installation](#requirements-installation)
    - [GCP Project & Authentication](#gcp-project--authentication)
3. [Usage](#usage)
4. [Contribution](#contribution)
5. [License](#license)

## Features
- **Automated Email Fetching**: Fetches emails from Gmail labeled as "Papers".
- **Abstract Extraction**: Extracts abstracts from these emails for consolidated reading.
- **Natural Language Processing**: Uses gpt-3.5-turbo to process and clean up the abstracts.
- **Consolidated Output**: Saves cleaned abstracts to a file.

## Setup and Installation

### Requirements Installation
To set up and run the project locally:

1. Clone this repository:
```bash
git clone https://github.com/AlefAlfa/AbstractsExtractor.git
cd AbstractsExtractor
```

2. Install the required packages:
```bash
pip install -r requirements.txt
```

### GCP Project & Authentication

Before you can fetch emails, you need to authenticate with your Gmail using OAuth2. Follow these steps:

1. Go to the [Google Cloud Platform Console](https://console.cloud.google.com/).
2. Create a new project.
3. Enable the Gmail API for your project.
4. Setup OAuth2 credentials.
5. Download the `credentials.json` and place it in the root directory of this project.
6. For a detailed step-by-step tutorial on these, you can refer to [this guide](https://www.geeksforgeeks.org/python-fetch-your-gmail-emails-from-a-particular-user/).

## Usage

Once set up, you can run the main script to fetch, extract, and process abstracts:

```bash
python main.py
```

The cleaned abstracts will be saved in an output file in the project directory.

## Contribution

Feel free to fork this project and make any contributions you think will benefit the project. Pull requests are warmly welcome.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

Thank you for using or contributing to this project!
