## Milestone 2 - Part 2: API Source Code Locations

The following are the BeautifulSoup API functions I used in Milestone 1 and Milestone 2 Part 1. These locations refer to the original source code before modifications.

- **BeautifulSoup()** — `bs4/__init__.py`, line 209
- **find_all()** — `bs4/element.py`, line 2715
- **prettify()** — `bs4/element.py`, line 2601
- **find_parent()** — `bs4/element.py`, line 992
- **get_text()** — `bs4/element.py`, line 524
- **SoupStrainer()** — `bs4/filter.py`, line 345
- **Tag.__setitem__()** — `bs4/element.py`, line 2223

### Additional Notes

In Milestone 1 Task 6, I used `tag.name` to rename tags. This attribute is initialized in `bs4/element.py` at line 1648.

In Milestone 1 Task 7, I used `tag["class"] = "test"` to update attributes. This uses the `__setitem__()` method at line 2223 in `bs4/element.py`.