#!/usr/bin/env python3
"""
Fetch AI prompts from a URL and save them to a text file.
"""

import argparse
import os
import sys
from datetime import datetime
from urllib.parse import urlparse

try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    print("Error: Required dependencies not installed.")
    print("Please run: pip install -r requirements.txt")
    sys.exit(1)


def fetch_url_content(url):
    """Fetch content from the given URL."""
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching URL: {e}")
        sys.exit(1)


def extract_prompts(html_content):
    """Extract text content from HTML that could be prompts."""
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Remove script and style elements
    for script in soup(["script", "style"]):
        script.decompose()
    
    # Get text content
    text = soup.get_text()
    
    # Clean up whitespace
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)
    
    return text


def generate_filename(url):
    """Generate a filename based on the URL and current timestamp."""
    parsed_url = urlparse(url)
    domain = parsed_url.netloc.replace('www.', '')
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    
    # Clean domain name for filename
    domain_clean = domain.replace('.', '_')
    
    return f"prompts_{domain_clean}_{timestamp}.txt"


def save_prompts(content, output_dir, filename):
    """Save the extracted prompts to a text file."""
    os.makedirs(output_dir, exist_ok=True)
    
    filepath = os.path.join(output_dir, filename)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return filepath


def main():
    parser = argparse.ArgumentParser(
        description='Fetch AI prompts from a URL and save them to a text file.'
    )
    parser.add_argument('url', help='URL to fetch prompts from')
    parser.add_argument(
        '-o', '--output-dir',
        default='prompts',
        help='Output directory for saved prompts (default: prompts)'
    )
    parser.add_argument(
        '-f', '--filename',
        help='Custom filename (optional, auto-generated if not provided)'
    )
    
    args = parser.parse_args()
    
    print(f"Fetching content from: {args.url}")
    html_content = fetch_url_content(args.url)
    
    print("Extracting prompts...")
    prompts = extract_prompts(html_content)
    
    if not prompts.strip():
        print("Warning: No content extracted from the URL")
        sys.exit(1)
    
    filename = args.filename if args.filename else generate_filename(args.url)
    
    # Ensure filename has .txt extension
    if not filename.endswith('.txt'):
        filename += '.txt'
    
    print(f"Saving prompts to file...")
    filepath = save_prompts(prompts, args.output_dir, filename)
    
    print(f"✓ Prompts saved successfully to: {filepath}")
    print(f"  ({len(prompts)} characters)")


if __name__ == '__main__':
    main()
