# graphify\graphify\wiki.py

## Símbolos

- [[graphify_graphify_wiki]] — code: wiki.py
- [[graphify_graphify_wiki_safe_filename]] — code: _safe_filename()
- [[graphify_graphify_wiki_md_link]] — code: _md_link()
- [[graphify_graphify_wiki_cross_community_links]] — code: _cross_community_links()
- [[graphify_graphify_wiki_community_article]] — code: _community_article()
- [[graphify_graphify_wiki_god_node_article]] — code: _god_node_article()
- [[graphify_graphify_wiki_index_md]] — code: _index_md()
- [[graphify_graphify_wiki_to_wiki]] — code: to_wiki()
- [[graphify_graphify_wiki_rationale_13]] — code: Make a label safe for use as a filename across platforms.      Substitutes cha
- [[graphify_graphify_wiki_rationale_28]] — code: Render a link to another wiki article as a portable relative markdown link.
- [[graphify_graphify_wiki_rationale_52]] — code: Return (community_label, edge_count) pairs for cross-community connections, sort
- [[graphify_graphify_wiki_rationale_219]] — code: Generate a Wikipedia-style wiki from the graph.      Writes:       - index.md

## Dependências

- [[graphify_graphify_wiki]] → `imports_from` → [[graphify_graphify_build]]
- [[graphify_graphify_wiki_community_article]] → `calls` → [[graphify_graphify_build_edge_data]]
- [[graphify_graphify_wiki_god_node_article]] → `calls` → [[graphify_graphify_build_edge_data]]
- [[graphify_graphify_wiki]] → `contains` → [[graphify_graphify_wiki_community_article]]
- [[graphify_graphify_wiki]] → `contains` → [[graphify_graphify_wiki_cross_community_links]]
- [[graphify_graphify_wiki]] → `contains` → [[graphify_graphify_wiki_god_node_article]]
- [[graphify_graphify_wiki]] → `contains` → [[graphify_graphify_wiki_index_md]]
- [[graphify_graphify_wiki]] → `contains` → [[graphify_graphify_wiki_md_link]]
- [[graphify_graphify_wiki]] → `contains` → [[graphify_graphify_wiki_safe_filename]]
- [[graphify_graphify_wiki]] → `contains` → [[graphify_graphify_wiki_to_wiki]]
- [[graphify_graphify_wiki_rationale_13]] → `rationale_for` → [[graphify_graphify_wiki_safe_filename]]
- [[graphify_graphify_wiki_to_wiki]] → `calls` → [[graphify_graphify_wiki_safe_filename]]
- [[graphify_graphify_wiki_community_article]] → `calls` → [[graphify_graphify_wiki_md_link]]
- [[graphify_graphify_wiki_god_node_article]] → `calls` → [[graphify_graphify_wiki_md_link]]
- [[graphify_graphify_wiki_index_md]] → `calls` → [[graphify_graphify_wiki_md_link]]
- [[graphify_graphify_wiki_rationale_28]] → `rationale_for` → [[graphify_graphify_wiki_md_link]]
- [[graphify_graphify_wiki_community_article]] → `calls` → [[graphify_graphify_wiki_cross_community_links]]
- [[graphify_graphify_wiki_rationale_52]] → `rationale_for` → [[graphify_graphify_wiki_cross_community_links]]
- [[graphify_graphify_wiki_to_wiki]] → `calls` → [[graphify_graphify_wiki_community_article]]
- [[graphify_graphify_wiki_to_wiki]] → `calls` → [[graphify_graphify_wiki_god_node_article]]
- [[graphify_graphify_wiki_to_wiki]] → `calls` → [[graphify_graphify_wiki_index_md]]
- [[graphify_graphify_wiki_rationale_219]] → `rationale_for` → [[graphify_graphify_wiki_to_wiki]]
- [[graphify_graphify_wiki_to_wiki]] → `references` → [[graphify_graphify_wiki_py_path]]