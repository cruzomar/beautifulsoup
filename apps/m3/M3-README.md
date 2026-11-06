
# Milestone 3: SoupReplacer API

## Overview

In Milestone 2, I implemented SoupReplacer to replace HTML tag names during parsing. In Milestone 3, I extended the API to support higher-order functions, allowing users to customize how tags and their attributes are modified.

## Milestone 2 vs. Milestone 3

The Milestone 2 API was simple and easy to use. Users could provide an original tag name and a replacement tag name, such as `SoupReplacer("b", "blockquote")`. However, it was limited to replacing tag names.

The Milestone 3 API is more flexible because it accepts functions as arguments. The `name_xformer` function changes tag names, `attrs_xformer` replaces attributes, and `xformer` allows users to modify tags directly. This gives developers more control over how HTML is transformed.

Both implementations perform transformations during parsing, avoiding the need to traverse the entire tree again afterward. However, the Milestone 3 API is more complex and requires users to understand how the transformer functions work.

## Recommendation

I would recommend keeping both interfaces. The Milestone 2 API is useful for simple tag replacements, while the Milestone 3 API supports more advanced transformations.

By making the new parameters optional, we can preserve backward compatibility while giving developers more flexibility. This approach allows existing programs to continue working without changes and gives developers additional functionality when needed.
