
import pytest
from bs4 import BeautifulSoup, Comment, NavigableString, Tag


# Test 1: Verify iteration visits nested tags and text nodes in order
def test_nested_iteration():
    html = "<div><p>Hello <b>World</b></p></div>"
    soup = BeautifulSoup(html, "html.parser")

    # Get an iterator that visits nodes one at a time
    nodes = iter(soup)

    # Verify that opening tags are visited in document order
    assert next(nodes).name == "div"
    assert next(nodes).name == "p"

    # Verify that text nodes are included in iteration
    text = next(nodes)
    assert isinstance(text, NavigableString)
    assert str(text) == "Hello "

    # Verify that nested tags and their text are visited
    bold = next(nodes)
    assert isinstance(bold, Tag)
    assert bold.name == "b"
    assert str(next(nodes)) == "World"

    # Verify that iteration stops after visiting every node
    with pytest.raises(StopIteration):
        next(nodes)


# Test 2: Verify iteration over an empty document
def test_empty_iteration():
    soup = BeautifulSoup("", "html.parser")

    # Create an iterator for the empty document
    nodes = iter(soup)

    # Verify that there are no nodes to visit
    with pytest.raises(StopIteration):
        next(nodes)

    # Verify that iterating again still produces no nodes
    assert sum(1 for node in soup) == 0


# Test 3: Verify iteration includes tags, text, and comments
def test_different_node_types():
    html = "<div>Hello<!-- This is a comment --><p>World</p></div>"
    soup = BeautifulSoup(html, "html.parser")

    # Create an iterator to visit nodes one at a time
    nodes = iter(soup)

    # Verify the first node is a div tag
    div = next(nodes)
    assert isinstance(div, Tag)
    assert div.name == "div"

    # Verify the second node is text
    text = next(nodes)
    assert isinstance(text, NavigableString)
    assert str(text) == "Hello"

    # Verify the third node is an HTML comment
    comment = next(nodes)
    assert isinstance(comment, Comment)
    assert str(comment) == " This is a comment "

    # Verify the paragraph tag and its text are included
    paragraph = next(nodes)
    assert isinstance(paragraph, Tag)
    assert paragraph.name == "p"
    assert str(next(nodes)) == "World"

    # Verify that all nodes have been visited
    with pytest.raises(StopIteration):
        next(nodes)

        
# Test 4: Verify multiple iterators work independently
def test_multiple_iterators():
    html = "<div><p>Hello</p><p>World</p></div>"
    soup = BeautifulSoup(html, "html.parser")

    # Create two separate iterators from the same soup object
    first = iter(soup)
    second = iter(soup)

    # Both iterators should begin at the first node
    assert next(first).name == "div"
    assert next(second).name == "div"

    # Advancing one iterator should not affect the other
    assert next(first).name == "p"
    assert str(next(first)) == "Hello"
    assert next(second).name == "p"

    # Verify the second iterator still reaches the same text node
    assert str(next(second)) == "Hello"

    # Both iterators should have 2 remaining nodes
    assert sum(1 for node in first) == 2
    assert sum(1 for node in second) == 2


# Test 5: Verify iteration handles deeply nested HTML
def test_deeply_nested_iteration():
    html = "<div><section><article><p><b>Deep</b></p></article></section></div>"
    soup = BeautifulSoup(html, "html.parser")

    # Visit all nodes without collecting them into a list
    nodes = iter(soup)

    # Verify each nested tag appears in the correct order
    assert next(nodes).name == "div"
    assert next(nodes).name == "section"
    assert next(nodes).name == "article"
    assert next(nodes).name == "p"
    assert next(nodes).name == "b"

    # Verify the deepest text node is visited
    assert str(next(nodes)) == "Deep"

    # Verify iteration ends after the last node
    with pytest.raises(StopIteration):
        next(nodes)
