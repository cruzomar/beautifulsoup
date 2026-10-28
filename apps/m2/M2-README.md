# SWE 262 - Milestone 2 - Omar Cruz

## Part 1: SoupStrainer
- `task2.py` - Print all hyperlinks using `SoupStrainer("a")`.
- `task3.py` - Print all tags using `SoupStrainer(True)`.
- `task4.py` - Print all tags containing an `id` attribute using `SoupStrainer(id=True)`.

## Part 2: API Source Code Locations

The following locations refer to the original BeautifulSoup 4.13.0 source code before modifications.

- `BeautifulSoup.__init__()` - `bs4/__init__.py`, line 209
- `find_all()` - `bs4/element.py`, line 2715
- `prettify()` - `bs4/element.py`, line 2601
- `find_parent()` - `bs4/element.py`, line 992
- `get_text()` - `bs4/element.py`, line 524
- `SoupStrainer.__init__()` - `bs4/filter.py`, line 345
- `Tag.__setitem__()` - `bs4/element.py`, line 2223

In Milestone 1 Task 6, I used `tag.name` to rename tags. This attribute is initialized in `bs4/element.py` at line 1648.

In Milestone 1 Task 7, I used `tag["class"] = "test"` to modify tag attributes, which uses `Tag.__setitem__()`.

## Part 3: SoupReplacer

Implemented a new API called `SoupReplacer(og_tag, alt_tag)` that replaces specified tags during parsing.

Changes made:
- Created `bs4/replacer.py` containing the `SoupReplacer` class.
- Modified `BeautifulSoup.__init__()` to accept an optional `replacer` argument.
- Modified `handle_starttag()` and `handle_endtag()` to handle replacements during parsing.
- Added two tests in `bs4/tests/test_replacer.py`.
- Created `apps/m2/task6.py` to replace `<b>` tags with `<blockquote>` tags using the new API.

### Testing

Both new unit tests passed:
- Multiple replacements in one document.
- Nested tag replacements.

Run the tests:

```bash
python -m pytest bs4/tests/test_replacer.py -v
```

Run Task 6:

```bash
python apps/m2/task6.py path/to/file.html
```

The modified document is saved in `apps/m2/outputs/`.