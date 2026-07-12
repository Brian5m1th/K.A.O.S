# graphify\graphify\file_slice.py

## Símbolos

- [[graphify_graphify_file_slice]] — code: file_slice.py
- [[graphify_graphify_file_slice_fileslice]] — code: FileSlice
- [[graphify_graphify_file_slice_unit_path]] — code: unit_path()
- [[graphify_graphify_file_slice_is_splittable_text]] — code: is_splittable_text()
- [[graphify_graphify_file_slice_best_cut]] — code: _best_cut()
- [[graphify_graphify_file_slice_slice_boundaries]] — code: slice_boundaries()
- [[graphify_graphify_file_slice_expand_oversized_files]] — code: expand_oversized_files()
- [[graphify_graphify_file_slice_read_slice_text]] — code: read_slice_text()
- [[graphify_graphify_file_slice_bisect_slice]] — code: bisect_slice()
- [[graphify_graphify_file_slice_rationale_1]] — code: Intra-file slicing for oversized text documents (#1369).  The extraction packe
- [[graphify_graphify_file_slice_rationale_39]] — code: A contiguous ``[start, end)`` character range of a splittable text file.
- [[graphify_graphify_file_slice_rationale_58]] — code: The on-disk path a unit belongs to (the parent file for a slice).
- [[graphify_graphify_file_slice_rationale_63]] — code: True for plain-text document types that may be sliced.
- [[graphify_graphify_file_slice_rationale_68]] — code: Return a cut index in ``(start, end]`` at the strongest nearby boundary.
- [[graphify_graphify_file_slice_rationale_87]] — code: Contiguous ``(start, end)`` ranges covering all of ``text``, each ≤ max_chars.
- [[graphify_graphify_file_slice_rationale_110]] — code: Replace each oversized splittable-text file with a list of ``FileSlice``s.
- [[graphify_graphify_file_slice_rationale_137]] — code: Read just this slice's characters from its parent file.
- [[graphify_graphify_file_slice_rationale_143]] — code: Split a slice into two halves at a newline near its midpoint, or None.      Us

## Dependências

- [[graphify_graphify_file_slice]] → `contains` → [[graphify_graphify_file_slice_best_cut]]
- [[graphify_graphify_file_slice]] → `contains` → [[graphify_graphify_file_slice_bisect_slice]]
- [[graphify_graphify_file_slice]] → `contains` → [[graphify_graphify_file_slice_expand_oversized_files]]
- [[graphify_graphify_file_slice]] → `contains` → [[graphify_graphify_file_slice_fileslice]]
- [[graphify_graphify_file_slice]] → `contains` → [[graphify_graphify_file_slice_is_splittable_text]]
- [[graphify_graphify_file_slice]] → `contains` → [[graphify_graphify_file_slice_read_slice_text]]
- [[graphify_graphify_file_slice]] → `contains` → [[graphify_graphify_file_slice_slice_boundaries]]
- [[graphify_graphify_file_slice]] → `contains` → [[graphify_graphify_file_slice_unit_path]]
- [[graphify_graphify_file_slice_rationale_1]] → `rationale_for` → [[graphify_graphify_file_slice]]
- [[graphify_graphify_file_slice_bisect_slice]] → `references` → [[graphify_graphify_file_slice_fileslice]]
- [[graphify_graphify_file_slice_expand_oversized_files]] → `calls` → [[graphify_graphify_file_slice_fileslice]]
- [[graphify_graphify_file_slice_rationale_39]] → `rationale_for` → [[graphify_graphify_file_slice_fileslice]]
- [[graphify_graphify_file_slice_read_slice_text]] → `references` → [[graphify_graphify_file_slice_fileslice]]
- [[graphify_graphify_file_slice_unit_path]] → `indirect_call` → [[graphify_graphify_file_slice_fileslice]]
- [[graphify_graphify_file_slice_rationale_58]] → `rationale_for` → [[graphify_graphify_file_slice_unit_path]]
- [[graphify_graphify_file_slice_unit_path]] → `references` → [[graphify_graphify_file_slice_py_path]]
- [[graphify_graphify_file_slice_expand_oversized_files]] → `references` → [[graphify_graphify_file_slice_py_path]]
- [[graphify_graphify_file_slice_is_splittable_text]] → `references` → [[graphify_graphify_file_slice_py_path]]
- [[graphify_graphify_file_slice_expand_oversized_files]] → `calls` → [[graphify_graphify_file_slice_is_splittable_text]]
- [[graphify_graphify_file_slice_rationale_63]] → `rationale_for` → [[graphify_graphify_file_slice_is_splittable_text]]
- [[graphify_graphify_file_slice_rationale_68]] → `rationale_for` → [[graphify_graphify_file_slice_best_cut]]
- [[graphify_graphify_file_slice_slice_boundaries]] → `calls` → [[graphify_graphify_file_slice_best_cut]]
- [[graphify_graphify_file_slice_expand_oversized_files]] → `calls` → [[graphify_graphify_file_slice_slice_boundaries]]
- [[graphify_graphify_file_slice_rationale_87]] → `rationale_for` → [[graphify_graphify_file_slice_slice_boundaries]]
- [[graphify_graphify_file_slice_rationale_110]] → `rationale_for` → [[graphify_graphify_file_slice_expand_oversized_files]]
- [[graphify_graphify_file_slice_rationale_137]] → `rationale_for` → [[graphify_graphify_file_slice_read_slice_text]]
- [[graphify_graphify_file_slice_rationale_143]] → `rationale_for` → [[graphify_graphify_file_slice_bisect_slice]]