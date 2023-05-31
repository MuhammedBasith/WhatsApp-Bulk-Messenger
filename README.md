
#WhatsApp Bulk Messenger

**Send bulk messages on WhatsApp easily and for free!**

## Introduction

Do you ever find yourself needing to send bulk messages on WhatsApp but are limited by paid software? Look no further! WhatsApp Bulk Messenger is a Python-based application that allows you to send messages to multiple recipients simultaneously, without any financial constraints. With its user-friendly interface and powerful automation capabilities, you can effortlessly reach a large audience in no time.

## Table of Contents
- [Introduction](#introduction)
- [Table of Contents](#table-of-contents)
- [Project Overview](#project-overview)
- [Usage](#usage)
- [Contributions](#contributions)
- [License](#license)

## Project Overview

WhatsApp Bulk Messenger is a Python-based application that allows users to send bulk messages on WhatsApp conveniently. The project consists of three main code files: `with_attachment.py`, `without_attachment.py`, and `number_extractor.py`. Each file serves a specific purpose in the messaging process, offering flexibility and ease of use.

## Usage

To get started with WhatsApp Bulk Messenger, follow the steps below:

### Prerequisites

1. Ensure you have Python 3.8.4 or higher installed on your system. If you don't have Python installed, you can download it from the official Python website: [Download Python](https://www.python.org/downloads/)

### Installation

1. Clone this repository to your local machine or download the ZIP file and extract it.

2. Open a terminal or command prompt and navigate to the project's root directory.

3. Create a virtual environment (optional but recommended) by running the following command:
    ```
    python3 -m venv venv
    ```

4. Activate the virtual environment:
    - For Windows:
        ```
        venv\Scripts\activate
        ```
    - For Unix or Linux:
        ```
        source venv/bin/activate
        ```

5. Install the project dependencies by running the following command:
    ```
    pip install -r requirements.txt
    ```

### Sending Bulk Messages

1. Run the `with_attachment.py` script to send bulk messages with attachments. Follow the instructions prompted in the terminal to specify the message and the path to the attachment.

2. Run the `without_attachment.py` script to send bulk text-only messages. The script will guide you through the process of specifying the message content.

### Extracting Participant Numbers

1. Run the `number_extractor.py` script to extract participant numbers from a WhatsApp group. The script will automate the extraction process and store the numbers in a text file for further use.

**Note:** The scripts will automatically open WhatsApp Web using Selenium, so make sure you have a working internet connection before running the scripts.

## Contributions

Contributions to WhatsApp Bulk Messenger are welcome! If you find any issues or have ideas for improvements, feel free to open an issue or submit a pull request. We appreciate any feedback and contributions that can help enhance the project.

## License

This project is licensed under the [MIT License](https://github.com/MuhammedBasith/WhatsApp-Bulk-Messenger/blob/main/LICENSE). Please see the [LICENSE](https://github.com/MuhammedBasith/WhatsApp-Bulk-Messenger/blob/main/LICENSE) file for more details.
