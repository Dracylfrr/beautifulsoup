# Milestone-3

- Added functional transformers: `name_xformer`, `attrs_xformer`, and `xformer`
- Enables dynamic, functional modification of tags during parsing.
- Can rename tags conditionally, modify attributes, or apply side effects (e.g., delete attributes).

# Recommendation

Milestone 3’s function-based design is more extensible. It decouples logic from the parser and allows users to define custom transformations without subclassing `BeautifulSoup`.  
If incorporated into BeautifulSoup officially, it should include validation and logging hooks for safety and developer feedback.
