from bs4 import BeautifulSoup, SoupReplacer

def testMultipleReplacements():
    html = "<div><b>First</b><p>Normal</p><b>Second</b></div>"

    soup = BeautifulSoup(
        html, "html.parser",
        replacer=SoupReplacer("b", "blockquote")
    )

    assert str(soup) == "<div><blockquote>First</blockquote><p>Normal</p><blockquote>Second</blockquote></div>"

def testNestedReplacements():
    html = "<b>Outer <b>Inner</b> Text</b>"

    soup = BeautifulSoup(
        html, "html.parser",
        replacer=SoupReplacer("b", "blockquote")
    )

    assert str(soup) == "<blockquote>Outer <blockquote>Inner</blockquote> Text</blockquote>"