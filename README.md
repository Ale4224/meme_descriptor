# Meme Description Generator

This project is a Python script that generates descriptions for a list of meme images using OpenAI's API. The script processes the images, generates descriptions, and creates a document with the descriptions.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You need Python 3.8 or later to run the script. You can have multiple Python versions (2.x and 3.x) installed on the same system without problems.

In Ubuntu, Mint and Debian you can install Python 3 like this:

```bash
sudo apt-get install python3 python3-pip
```

For other Linux flavors, macOS and Windows, packages are available at

https://www.python.org/getit/

### Installing

The first step is to clone the repository:

```bash
git clone https://github.com/Ale4224/meme_descriptor.git
```

Navigate to the project directory:

```bash
cd meme_descriptor
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

## Environment Variables

The script uses the following environment variables:

- `OPENAI_API_KEY`: Your OpenAI API key. This is required to make requests to the OpenAI API for generating meme descriptions.
- `USE_LOCAL_IMAGES`: A boolean value (`true` or `false`). If set to `true`, the script will use local images for generating meme descriptions. If `false`, it will use the URLs specified in `meme_urls.py`.
- `NUMBER_OF_MEMES_TO_GENERATE`: The number of memes for which the script should generate descriptions. It should be a positive integer.
- `MOCK_DATA`: A boolean value (`true` or `false`). If set to `true`, the script will use mock data `mockdata.json` for generating the meme descriptions. This can be useful for testing purposes.
- `SAVE_MOCK_DATA`: A boolean value (`true` or `false`). If set to `true`, the script will save the generated descriptions as mock data in tthe file `mockdata.json`. This can be useful for future testing purposes.

These variables should be set in a `.env` file in the root directory of the project.

### Running the script

To run the script, you can use the following command:

```bash
python src/main.py
```

## Built With

* [Python 3](https://www.python.org/) - The programming language used.
* [OpenAI API](https://openai.com/research/) - The API used to generate descriptions.
* [mdutils](https://mdutils.readthedocs.io/en/latest/) - A Python library used to create Markdown files programmatically.

## Authors

* **Alessandro Tassinari** - *Initial work* - [Ale4224](https://github.com/Ale4224)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

This project is a gift to my sister, who is trying to learn the python programming language.
