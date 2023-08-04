# Shopify JSON Uploader

This script allows you to upload JSON files to your Shopify store's files section from the command line via API.

## Disclaimer
This tool was independently developed and maintained. It is not in any way affiliated with, endorsed by, or supported by Shopify Inc.

## Setup

The following instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.9+
- pip (Python package manager)

### Installation

**Step 1:** Clone the repository to your local machine:

```bash
git clone https://github.com/JimmyMcKegger/json-uploader.git
```

**Step 2:** Navigate into the project directory:

```bash
cd json-uploader
```

**Step 3:** Create a virtual environment:

```bash
python3 -m venv venv
```

**Step 4:** Activate the virtual environment:

On Windows:

```bash
.\venv\Scripts\activate
```

On MacOS/Linux:

```bash
source venv/bin/activate
```

**Step 5:** Install the requirements:

```bash
pip install -r requirements.txt
```

**Step 6:** Create a `.env` file in the project root directory. Use the following template and replace the placeholders with your actual Shopify store details:

```bash
SHOP=example.myshopify.com
API_ACCESS_TOKEN=123123123123123123123123
API_VERSION=2023-07
API_SECRET_KEY=shpss_12312312312123123123123
```

Save the file.

That's it! You're now ready to use the script.

## Usage

To run the script, pass the name of the JSON file you want to upload as a command-line argument:

```bash
python app.py filename.json
```

This will process the `filename.json` file and upload it to your Shopify store.

## Contributing

Pull requests to add support for more file types are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

* Shopify for their powerful API
* Python community for the amazing tools and libraries
* OpenAI for the LLM that generated this README
