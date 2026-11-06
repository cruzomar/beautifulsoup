from bs4 import BeautifulSoup
from bs4.replacer import SoupReplacer


# Test 1: Replace tag names using name_xformer
def test_name_xformer():
    html = "<div><b>Hello</b><p>World</p></div>"

    # Replace only <b> tags with <blockquote>
    replacer = SoupReplacer(
        name_xformer=lambda tag: "blockquote" if tag.name == "b" else tag.name
    )

    soup = BeautifulSoup(html, "html.parser", replacer=replacer)

    # Verify the tag was replaced and other tags remain unchanged
    assert soup.find("blockquote").text == "Hello"
    assert soup.find("b") is None
    assert soup.find("p").text == "World"


# Test 2: Add or replace attributes using attrs_xformer
def test_attrs_xformer():
    html = '<div><p class="old">Hello</p><p>World</p></div>'

    # Replace or add class="test" to all <p> tags
    def update_attrs(tag):
        if tag.name == "p":
            new_attrs = dict(tag.attrs)
            new_attrs["class"] = ["test"]
            return new_attrs

        return tag.attrs

    replacer = SoupReplacer(attrs_xformer=update_attrs)
    soup = BeautifulSoup(html, "html.parser", replacer=replacer)

    # Verify both paragraphs have the updated class
    paragraphs = soup.find_all("p")
    assert len(paragraphs) == 2
    assert paragraphs[0]["class"] == ["test"]
    assert paragraphs[1]["class"] == ["test"]

    # Verify the text remains unchanged
    assert paragraphs[0].text == "Hello"
    assert paragraphs[1].text == "World"


# Test 3: Modify tags directly using xformer
def test_xformer():
    html = '<div class="container"><p class="old">Hello</p></div>'

    # Remove class attributes without returning a value
    def remove_class(tag):
        if "class" in tag.attrs:
            del tag.attrs["class"]

    replacer = SoupReplacer(xformer=remove_class)
    soup = BeautifulSoup(html, "html.parser", replacer=replacer)

    # Verify class attributes were removed
    assert soup.find("div").get("class") is None
    assert soup.find("p").get("class") is None

    # Verify the HTML structure and text remain unchanged
    assert soup.find("div").find("p").text == "Hello"


# Test 4: Use all three transformer functions together
def test_multiple_xformers():
    html = '<b class="old">Hello</b>'

    # Replace <b> with <blockquote>
    def change_name(tag):
        return "blockquote" if tag.name == "b" else tag.name

    # Add a new attribute to the tag
    def change_attrs(tag):
        new_attrs = dict(tag.attrs)
        new_attrs["data-test"] = "updated"
        return new_attrs

    # Remove the original class attribute
    def remove_class(tag):
        if "class" in tag.attrs:
            del tag.attrs["class"]

    replacer = SoupReplacer(
        name_xformer=change_name,
        attrs_xformer=change_attrs,
        xformer=remove_class
    )

    soup = BeautifulSoup(html, "html.parser", replacer=replacer)
    tag = soup.find("blockquote")

    # Verify all three transformations were applied
    assert tag is not None
    assert tag["data-test"] == "updated"
    assert tag.get("class") is None
    assert tag.text == "Hello"


# Test 5: Transform nested tags correctly
def test_nested_tags():
    html = "<div><b>Outer <b>Inner</b> End</b><p>Next</p></div>"

    # Replace all <b> tags, including nested ones
    replacer = SoupReplacer(
        name_xformer=lambda tag: "blockquote" if tag.name == "b" else tag.name
    )

    soup = BeautifulSoup(html, "html.parser", replacer=replacer)

    # Verify both <b> tags were replaced
    blockquotes = soup.find_all("blockquote")
    assert len(blockquotes) == 2
    assert soup.find("b") is None

    # Verify the nested structure was preserved
    outer = blockquotes[0]
    inner = blockquotes[1]

    assert inner.parent is outer
    assert inner.text == "Inner"
    assert outer.get_text(" ", strip=True) == "Outer Inner End"

    # Verify the following paragraph remains outside the nested tags
    assert soup.find("p").parent.name == "div"


# Test 6: Preserve compatibility with the Milestone 2 API
def test_original_replacer():
    html = "<div><b>Hello</b><p>World</p></div>"

    # Use the original Milestone 2 constructor
    replacer = SoupReplacer("b", "blockquote")
    soup = BeautifulSoup(html, "html.parser", replacer=replacer)

    # Verify the original replacement functionality still works
    assert soup.find("blockquote").text == "Hello"
    assert soup.find("b") is None

    # Verify unrelated tags remain unchanged
    assert soup.find("p").text == "World"
    assert soup.find("div") is not None
