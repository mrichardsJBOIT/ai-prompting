# ai-prompting
Collection of AI prompts and sources

## Features

- Fetch AI prompts from any URL and save them as text files
- Automatic file naming based on URL and timestamp
- Simple command-line interface

## Installation

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Fetch prompts from a URL

```bash
python fetch_prompts.py <URL>
```

Example:
```bash
python fetch_prompts.py https://example.com/ai-prompts
```

### Options

- `-o, --output-dir`: Specify output directory (default: `prompts`)
- `-f, --filename`: Custom filename for the saved prompts

Examples:
```bash
# Save to a custom directory
python fetch_prompts.py https://example.com/prompts -o my_prompts

# Use a custom filename
python fetch_prompts.py https://example.com/prompts -f my_custom_prompts.txt
```

## Output

Fetched prompts are saved as text files in the `prompts/` directory (or your specified directory). Files are automatically named with the format:
```
prompts_<domain>_<timestamp>.txt
```

For example: `prompts_example_com_20231012_143022.txt`
