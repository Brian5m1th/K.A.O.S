# graphify\worked\httpx\raw\utils.py

## Símbolos

- [[graphify_worked_httpx_raw_utils]] — code: utils.py
- [[graphify_worked_httpx_raw_utils_primitive_value_to_str]] — code: primitive_value_to_str()
- [[graphify_worked_httpx_raw_utils_normalize_header_key]] — code: normalize_header_key()
- [[graphify_worked_httpx_raw_utils_flatten_queryparams]] — code: flatten_queryparams()
- [[graphify_worked_httpx_raw_utils_parse_content_type]] — code: parse_content_type()
- [[graphify_worked_httpx_raw_utils_obfuscate_sensitive_headers]] — code: obfuscate_sensitive_headers()
- [[graphify_worked_httpx_raw_utils_unset_all_cookies]] — code: unset_all_cookies()
- [[graphify_worked_httpx_raw_utils_is_known_encoding]] — code: is_known_encoding()
- [[graphify_worked_httpx_raw_utils_build_url_with_params]] — code: build_url_with_params()
- [[graphify_worked_httpx_raw_utils_rationale_1]] — code: Utility functions shared across the library. Small helpers that don't belong in
- [[graphify_worked_httpx_raw_utils_rationale_13]] — code: Convert a primitive value to its string representation.
- [[graphify_worked_httpx_raw_utils_rationale_20]] — code: Convert a header key to its canonical Title-Case form.
- [[graphify_worked_httpx_raw_utils_rationale_25]] — code: Expand a params dict into a flat list of (key, value) pairs.     List values be
- [[graphify_worked_httpx_raw_utils_rationale_40]] — code: Parse a Content-Type header value.     Returns (media_type, params_dict).
- [[graphify_worked_httpx_raw_utils_rationale_56]] — code: Return a copy of headers with sensitive values replaced by [obfuscated].
- [[graphify_worked_httpx_raw_utils_rationale_64]] — code: Clear all cookies from a cookie jar in place.
- [[graphify_worked_httpx_raw_utils_rationale_69]] — code: Check if a character encoding label is recognized by Python's codec system.
- [[graphify_worked_httpx_raw_utils_rationale_79]] — code: Append query parameters to a URL string.

## Dependências

- [[graphify_worked_httpx_raw_utils_unset_all_cookies]] → `references` → [[graphify_worked_httpx_raw_models_cookies]]
- [[graphify_worked_httpx_raw_utils]] → `contains` → [[graphify_worked_httpx_raw_utils_build_url_with_params]]
- [[graphify_worked_httpx_raw_utils]] → `contains` → [[graphify_worked_httpx_raw_utils_flatten_queryparams]]
- [[graphify_worked_httpx_raw_utils]] → `contains` → [[graphify_worked_httpx_raw_utils_is_known_encoding]]
- [[graphify_worked_httpx_raw_utils]] → `contains` → [[graphify_worked_httpx_raw_utils_normalize_header_key]]
- [[graphify_worked_httpx_raw_utils]] → `contains` → [[graphify_worked_httpx_raw_utils_obfuscate_sensitive_headers]]
- [[graphify_worked_httpx_raw_utils]] → `contains` → [[graphify_worked_httpx_raw_utils_parse_content_type]]
- [[graphify_worked_httpx_raw_utils]] → `contains` → [[graphify_worked_httpx_raw_utils_primitive_value_to_str]]
- [[graphify_worked_httpx_raw_utils]] → `contains` → [[graphify_worked_httpx_raw_utils_unset_all_cookies]]
- [[graphify_worked_httpx_raw_utils_rationale_1]] → `rationale_for` → [[graphify_worked_httpx_raw_utils]]
- [[graphify_worked_httpx_raw_utils_flatten_queryparams]] → `calls` → [[graphify_worked_httpx_raw_utils_primitive_value_to_str]]
- [[graphify_worked_httpx_raw_utils_rationale_13]] → `rationale_for` → [[graphify_worked_httpx_raw_utils_primitive_value_to_str]]
- [[graphify_worked_httpx_raw_utils_rationale_20]] → `rationale_for` → [[graphify_worked_httpx_raw_utils_normalize_header_key]]
- [[graphify_worked_httpx_raw_utils_build_url_with_params]] → `calls` → [[graphify_worked_httpx_raw_utils_flatten_queryparams]]
- [[graphify_worked_httpx_raw_utils_rationale_25]] → `rationale_for` → [[graphify_worked_httpx_raw_utils_flatten_queryparams]]
- [[graphify_worked_httpx_raw_utils_rationale_40]] → `rationale_for` → [[graphify_worked_httpx_raw_utils_parse_content_type]]
- [[graphify_worked_httpx_raw_utils_rationale_56]] → `rationale_for` → [[graphify_worked_httpx_raw_utils_obfuscate_sensitive_headers]]
- [[graphify_worked_httpx_raw_utils_rationale_64]] → `rationale_for` → [[graphify_worked_httpx_raw_utils_unset_all_cookies]]
- [[graphify_worked_httpx_raw_utils_rationale_69]] → `rationale_for` → [[graphify_worked_httpx_raw_utils_is_known_encoding]]
- [[graphify_worked_httpx_raw_utils_rationale_79]] → `rationale_for` → [[graphify_worked_httpx_raw_utils_build_url_with_params]]