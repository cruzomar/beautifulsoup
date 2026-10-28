class SoupReplacer:
    # Stores the original tag and the tag that will replace it during parsing
    def __init__(self, og_tag, alt_tag):
        self.og_tag = og_tag
        self.alt_tag = alt_tag