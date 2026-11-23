# Milestone 4

## Overview

In Milestone 4, I extended BeautifulSoup to support iteration over all nodes in the parse tree. This allows users to loop through nested HTML elements directly using a for loop.

## Implementation

I implemented the `__iter__()` method inside the BeautifulSoup class in `bs4/__init__.py`.

Instead of creating a new traversal algorithm, I reused BeautifulSoup's existing `descendants` generator, which visits nodes in document order.

```python
def __iter__(self) -> Iterator[PageElement]:
    """Iterate over all nodes in the BeautifulSoup tree."""

    # Visit nodes one at a time without creating a list
    return self.descendants
```

This allows users to write:

```python
soup = BeautifulSoup(html, "html.parser")

for node in soup:
    print(node)
```

## Design Decisions

I chose to reuse the existing `descendants` generator instead of implementing a separate traversal method. This keeps the implementation simple and avoids duplicating functionality already available in BeautifulSoup.

The generator produces nodes one at a time rather than storing them in a list. This avoids additional memory usage proportional to the number of nodes and is useful when working with large HTML documents.

The iterator includes nested tags, text nodes, and comments. Each call to `iter(soup)` also creates an independent iterator, allowing the same document to be traversed multiple times.

## Testing

I implemented five unit tests covering:

1. Iteration over nested tags and text nodes.
2. Iteration over an empty document.
3. Iteration over different node types.
4. Multiple independent iterators.
5. Iteration over deeply nested HTML.

All five tests passed.

## Recommendation

I recommend using BeautifulSoup's existing `descendants` generator to implement the iterable API. It provides the required functionality while keeping the code simple and avoiding unnecessary memory overhead.

This approach also maintains compatibility with existing BeautifulSoup functionality and allows users to iterate over the parse tree using standard Python syntax.