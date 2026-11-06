import sys
from pathlib import Path
from bs4 import BeautifulSoup
from bs4.replacer import SoupReplacer


# Add or replace class="test" on all paragraph tags
def update_attrs(tag):
    if tag.name == "p":
        new_attrs = dict(tag.attrs)
        new_attrs["class"] = ["test"]
        return new_attrs

    # Leave attributes of other tags unchanged
    return tag.attrs


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 -m apps.m3.task7 <html_file>")
        return

    # Read the HTML file provided through the command line
    with open(sys.argv[1], "r", encoding="utf-8") as file:
        html = file.read()

    # Apply attribute transformations during parsing
    replacer = SoupReplacer(attrs_xformer=update_attrs)
    soup = BeautifulSoup(html, "html.parser", replacer=replacer)

    # Write the modified HTML tree to an output file
    output_path = Path("apps/m3/outputs/task7_output.html")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as file:
        file.write(soup.prettify())

    print(f"Modified HTML saved to {output_path}")


if __name__ == "__main__":
    main()