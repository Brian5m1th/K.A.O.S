# airllm\air_llm\airllm\tokenization_baichuan.py

## Símbolos

- [[airllm_air_llm_airllm_tokenization_baichuan]] — code: tokenization_baichuan.py
- [[airllm_air_llm_airllm_tokenization_baichuan_baichuantokenizer]] — code: BaichuanTokenizer
- [[airllm_air_llm_airllm_tokenization_baichuan_baichuantokenizer_init]] — code: .__init__()
- [[airllm_air_llm_airllm_tokenization_baichuan_baichuantokenizer_getstate]] — code: .__getstate__()
- [[airllm_air_llm_airllm_tokenization_baichuan_baichuantokenizer_setstate]] — code: .__setstate__()
- [[airllm_air_llm_airllm_tokenization_baichuan_baichuantokenizer_vocab_size]] — code: .vocab_size()
- [[airllm_air_llm_airllm_tokenization_baichuan_baichuantokenizer_get_vocab]] — code: .get_vocab()
- [[airllm_air_llm_airllm_tokenization_baichuan_baichuantokenizer_tokenize]] — code: ._tokenize()
- [[airllm_air_llm_airllm_tokenization_baichuan_baichuantokenizer_convert_token_to_id]] — code: ._convert_token_to_id()
- [[airllm_air_llm_airllm_tokenization_baichuan_baichuantokenizer_convert_id_to_token]] — code: ._convert_id_to_token()
- [[airllm_air_llm_airllm_tokenization_baichuan_baichuantokenizer_convert_tokens_to_string]] — code: .convert_tokens_to_string()
- [[airllm_air_llm_airllm_tokenization_baichuan_baichuantokenizer_save_vocabulary]] — code: .save_vocabulary()
- [[airllm_air_llm_airllm_tokenization_baichuan_baichuantokenizer_build_inputs_with_special_tokens]] — code: .build_inputs_with_special_tokens()
- [[airllm_air_llm_airllm_tokenization_baichuan_baichuantokenizer_get_special_tokens_mask]] — code: .get_special_tokens_mask()
- [[airllm_air_llm_airllm_tokenization_baichuan_baichuantokenizer_create_token_type_ids_from_sequences]] — code: .create_token_type_ids_from_sequences()
- [[airllm_air_llm_airllm_tokenization_baichuan_rationale_44]] — code: Construct a Baichuan tokenizer. Based on byte-level Byte-Pair-Encoding.      A
- [[airllm_air_llm_airllm_tokenization_baichuan_rationale_108]] — code: Returns vocab as a dict
- [[airllm_air_llm_airllm_tokenization_baichuan_rationale_114]] — code: Returns a tokenized string.
- [[airllm_air_llm_airllm_tokenization_baichuan_rationale_118]] — code: Converts a token (str) in an id using the vocab.
- [[airllm_air_llm_airllm_tokenization_baichuan_rationale_122]] — code: Converts an index (integer) in a token (str) using the vocab.
- [[airllm_air_llm_airllm_tokenization_baichuan_rationale_127]] — code: Converts a sequence of tokens (string) in a single string.
- [[airllm_air_llm_airllm_tokenization_baichuan_rationale_146]] — code: Save the vocabulary and special tokens file to a directory.          Args:
- [[airllm_air_llm_airllm_tokenization_baichuan_rationale_186]] — code: Retrieve sequence ids from a token list that has no special tokens added. This m
- [[airllm_air_llm_airllm_tokenization_baichuan_rationale_223]] — code: Creates a mask from the two sequences passed to be used in a sequence-pair class

## Dependências

- [[airllm_air_llm_airllm_tokenization_baichuan]] → `contains` → [[airllm_air_llm_airllm_tokenization_baichuan_baichuantokenizer]]
- [[airllm_air_llm_airllm_tokenization_baichuan_baichuantokenizer]] → `method` → [[airllm_air_llm_airllm_tokenization_baichuan_baichuantokenizer_build_inputs_with_special_tokens]]
- [[airllm_air_llm_airllm_tokenization_baichuan_baichuantokenizer]] → `method` → [[airllm_air_llm_airllm_tokenization_baichuan_baichuantokenizer_convert_id_to_token]]
- [[airllm_air_llm_airllm_tokenization_baichuan_baichuantokenizer]] → `method` → [[airllm_air_llm_airllm_tokenization_baichuan_baichuantokenizer_convert_token_to_id]]
- [[airllm_air_llm_airllm_tokenization_baichuan_baichuantokenizer]] → `method` → [[airllm_air_llm_airllm_tokenization_baichuan_baichuantokenizer_convert_tokens_to_string]]
- [[airllm_air_llm_airllm_tokenization_baichuan_baichuantokenizer]] → `method` → [[airllm_air_llm_airllm_tokenization_baichuan_baichuantokenizer_create_token_type_ids_from_sequences]]
- [[airllm_air_llm_airllm_tokenization_baichuan_baichuantokenizer]] → `method` → [[airllm_air_llm_airllm_tokenization_baichuan_baichuantokenizer_get_special_tokens_mask]]
- [[airllm_air_llm_airllm_tokenization_baichuan_baichuantokenizer]] → `method` → [[airllm_air_llm_airllm_tokenization_baichuan_baichuantokenizer_get_vocab]]
- [[airllm_air_llm_airllm_tokenization_baichuan_baichuantokenizer]] → `method` → [[airllm_air_llm_airllm_tokenization_baichuan_baichuantokenizer_getstate]]
- [[airllm_air_llm_airllm_tokenization_baichuan_baichuantokenizer]] → `method` → [[airllm_air_llm_airllm_tokenization_baichuan_baichuantokenizer_init]]
- [[airllm_air_llm_airllm_tokenization_baichuan_baichuantokenizer]] → `method` → [[airllm_air_llm_airllm_tokenization_baichuan_baichuantokenizer_save_vocabulary]]
- [[airllm_air_llm_airllm_tokenization_baichuan_baichuantokenizer]] → `method` → [[airllm_air_llm_airllm_tokenization_baichuan_baichuantokenizer_setstate]]
- [[airllm_air_llm_airllm_tokenization_baichuan_baichuantokenizer]] → `method` → [[airllm_air_llm_airllm_tokenization_baichuan_baichuantokenizer_tokenize]]
- [[airllm_air_llm_airllm_tokenization_baichuan_baichuantokenizer]] → `method` → [[airllm_air_llm_airllm_tokenization_baichuan_baichuantokenizer_vocab_size]]
- [[airllm_air_llm_airllm_tokenization_baichuan_baichuantokenizer]] → `inherits` → [[airllm_air_llm_airllm_tokenization_baichuan_py_pretrainedtokenizer]]
- [[airllm_air_llm_airllm_tokenization_baichuan_rationale_44]] → `rationale_for` → [[airllm_air_llm_airllm_tokenization_baichuan_baichuantokenizer]]
- [[airllm_air_llm_airllm_tokenization_baichuan_baichuantokenizer_init]] → `references` → [[airllm_air_llm_airllm_tokenization_baichuan_py_any]]
- [[airllm_air_llm_airllm_tokenization_baichuan_rationale_108]] → `rationale_for` → [[airllm_air_llm_airllm_tokenization_baichuan_baichuantokenizer_get_vocab]]
- [[airllm_air_llm_airllm_tokenization_baichuan_rationale_114]] → `rationale_for` → [[airllm_air_llm_airllm_tokenization_baichuan_baichuantokenizer_tokenize]]
- [[airllm_air_llm_airllm_tokenization_baichuan_rationale_118]] → `rationale_for` → [[airllm_air_llm_airllm_tokenization_baichuan_baichuantokenizer_convert_token_to_id]]
- [[airllm_air_llm_airllm_tokenization_baichuan_rationale_122]] → `rationale_for` → [[airllm_air_llm_airllm_tokenization_baichuan_baichuantokenizer_convert_id_to_token]]
- [[airllm_air_llm_airllm_tokenization_baichuan_rationale_127]] → `rationale_for` → [[airllm_air_llm_airllm_tokenization_baichuan_baichuantokenizer_convert_tokens_to_string]]
- [[airllm_air_llm_airllm_tokenization_baichuan_rationale_146]] → `rationale_for` → [[airllm_air_llm_airllm_tokenization_baichuan_baichuantokenizer_save_vocabulary]]
- [[airllm_air_llm_airllm_tokenization_baichuan_rationale_186]] → `rationale_for` → [[airllm_air_llm_airllm_tokenization_baichuan_baichuantokenizer_get_special_tokens_mask]]
- [[airllm_air_llm_airllm_tokenization_baichuan_rationale_223]] → `rationale_for` → [[airllm_air_llm_airllm_tokenization_baichuan_baichuantokenizer_create_token_type_ids_from_sequences]]