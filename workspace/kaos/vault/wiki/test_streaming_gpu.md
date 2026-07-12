# airllm\air_llm\tests\test_streaming_gpu.py

## Símbolos

- [[airllm_air_llm_tests_test_streaming_gpu]] — code: test_streaming_gpu.py
- [[airllm_air_llm_tests_test_streaming_gpu_cap_vram]] — code: cap_vram()
- [[airllm_air_llm_tests_test_streaming_gpu_run_airllm]] — code: run_airllm()
- [[airllm_air_llm_tests_test_streaming_gpu_run_reference]] — code: run_reference()
- [[airllm_air_llm_tests_test_streaming_gpu_main]] — code: main()
- [[airllm_air_llm_tests_test_streaming_gpu_rationale_1]] — code: Manual GPU test harness for AirLLM layer-streaming inference.  Runs a model th
- [[airllm_air_llm_tests_test_streaming_gpu_rationale_27]] — code: Limit how much of the GPU this process may allocate, to emulate a smaller card.
- [[airllm_air_llm_tests_test_streaming_gpu_rationale_63]] — code: Full-load run for correctness comparison (only feasible for small models).

## Dependências

- [[airllm_air_llm_tests_test_streaming_gpu_run_airllm]] → `calls` → [[airllm_air_llm_airllm_auto_model_automodel_from_pretrained]]
- [[airllm_air_llm_tests_test_streaming_gpu]] → `contains` → [[airllm_air_llm_tests_test_streaming_gpu_cap_vram]]
- [[airllm_air_llm_tests_test_streaming_gpu]] → `contains` → [[airllm_air_llm_tests_test_streaming_gpu_main]]
- [[airllm_air_llm_tests_test_streaming_gpu]] → `contains` → [[airllm_air_llm_tests_test_streaming_gpu_run_airllm]]
- [[airllm_air_llm_tests_test_streaming_gpu]] → `contains` → [[airllm_air_llm_tests_test_streaming_gpu_run_reference]]
- [[airllm_air_llm_tests_test_streaming_gpu_rationale_1]] → `rationale_for` → [[airllm_air_llm_tests_test_streaming_gpu]]
- [[airllm_air_llm_tests_test_streaming_gpu_main]] → `calls` → [[airllm_air_llm_tests_test_streaming_gpu_cap_vram]]
- [[airllm_air_llm_tests_test_streaming_gpu_rationale_27]] → `rationale_for` → [[airllm_air_llm_tests_test_streaming_gpu_cap_vram]]
- [[airllm_air_llm_tests_test_streaming_gpu_main]] → `calls` → [[airllm_air_llm_tests_test_streaming_gpu_run_airllm]]
- [[airllm_air_llm_tests_test_streaming_gpu_main]] → `calls` → [[airllm_air_llm_tests_test_streaming_gpu_run_reference]]
- [[airllm_air_llm_tests_test_streaming_gpu_rationale_63]] → `rationale_for` → [[airllm_air_llm_tests_test_streaming_gpu_run_reference]]