# SWE 262 Milestone 2: Task 6 - Omar Cruz
import sys
from bs4 import BeautifulSoup, SoupReplacer
from pathlib import Path

"""
    Task Six
    1. Check if the user provided a file path as a command-line argument
    2. Retrieve the file path from the command-line arguments
    3. Determine which parser to use based on the file extension: if not a .html or .xml file it is not supported
    4. Open the input file and read its contents
    5. Parse the file contents into a BeautifulSoup tree
    6. Find all <b> tags and rename them to <blockquote>
    7. Create an outputs directory if it does not exist
    8. Write the modified tree to a new file
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

with open(fileName, "r", encoding="utf-8") as file:
    result = file.read()

# Replace <b> tags with <blockquote> during parsing
bToBlockqoute = SoupReplacer("b", "blockquote")

soup = BeautifulSoup(result, parser, replacer=bToBlockqoute)

# Create the outputs folder inside apps/m2
outputDir = Path(__file__).resolve().parent / "outputs"
outputDir.mkdir(exist_ok=True)

outputFile = outputDir / f"{path.stem}-blockquote{path.suffix}"

with open(outputFile, "w", encoding="utf-8") as file:
    file.write(soup.prettify())

print("Output written in outputs folder.")