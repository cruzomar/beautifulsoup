# SWE 262 Milestone 2: Part 1 -Task 3 - Omar Cruz
import sys
from bs4 import BeautifulSoup, SoupStrainer
from pathlib import Path

"""
    Task Three
    1. Check if the user provided a file path as a command-line argument
    2. Retrieve the file path from the command-line arguments
    3. Determine which parser to use based on the file extension: if not a .html or .xml file it is not supported
    4. Create a SoupStrainer to match all tags
    5. Parse the file using BeautifulSoup and SoupStrainer
    6. Print out all tags in the document
"""
if (len(sys.argv) < 2):
    print("File must be given as a command line argument.")
    sys.exit(1)

fileName = sys.argv[1]
path = Path(fileName)

if path.suffix.lower() == ".html":
    parser = "html.parser"
elif path.suffix.lower() == ".xml":
    parser = "xml"
else:
    print(f"{path.suffix} files are unsupported by this application.")
    sys.exit(1)

allTags = SoupStrainer(True)

with open(fileName, "rb") as file:
    soup = BeautifulSoup(file, parser, parse_only=allTags)

for tag in soup.find_all(True):
    print(tag)