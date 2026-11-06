class SoupReplacer:
    # Stores the original tag and the tag that will replace it during parsing
    def __init__(self, og_tag = None, alt_tag = None, name_xformer = None, attrs_xformer = None, xformer = None):

        # Stores the original and replacement tag names
        self.og_tag = og_tag
        self.alt_tag = alt_tag

        # Functions used to transform tags during parsing

        # Returns a new name for a tag
        self.name_xformer = name_xformer

        # Returns new attributes for a tag
        self.attrs_xformer = attrs_xformer

        # Modifies a tag directly without returning a value
        self.xformer = xformer