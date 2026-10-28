# SWE 262 Milestone 2: Part 1 -Task 4 - Omar Cruz
import sys
from bs4 import BeautifulSoup, SoupStrainer
from pathlib import Path

"""
    Task Four
    1. Check if the user provided a file path as a command-line argument
    2. Retrieve the file path from the command-line arguments
    3. Determine which parser to use based on the file extension: if not a .html or .xml file it is not supported
    4. Create a SoupStrainer to match tags with an id attribute
    5. Parse the file using BeautifulSoup and SoupStrainer
    6. Print out all tags containing an id attribute
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

onlyIds = SoupStrainer(id=True)

with open(fileName, "rb") as file:
    soup = BeautifulSoup(file, parser, parse_only=onlyIds)

for tag in soup.find_all(id=True):
    print(tag)