# graphify\tests\test_wheel_packaging.py

## Símbolos

- [[graphify_tests_test_wheel_packaging]] — code: test_wheel_packaging.py
- [[graphify_tests_test_wheel_packaging_has_build]] — code: _has_build()
- [[graphify_tests_test_wheel_packaging_skill_bodies]] — code: _skill_bodies()
- [[graphify_tests_test_wheel_packaging_expected_artifacts]] — code: _expected_artifacts()
- [[graphify_tests_test_wheel_packaging_wheel_namelist]] — code: wheel_namelist()
- [[graphify_tests_test_wheel_packaging_test_skill_artifact_ships_in_wheel]] — code: test_skill_artifact_ships_in_wheel()
- [[graphify_tests_test_wheel_packaging_rationale_1]] — code: Packaging guard (#1121 follow-up): the 5 skillgen guards check the *repo tree*,
- [[graphify_tests_test_wheel_packaging_rationale_33]] — code: Every distinct skill body a platform installs (the SKILL.md is copied from
- [[graphify_tests_test_wheel_packaging_rationale_44]] — code: Every committed skill body + references/*.md (per host) + always_on/*.md block.

## Dependências

- [[graphify_tests_test_wheel_packaging]] → `contains` → [[graphify_tests_test_wheel_packaging_expected_artifacts]]
- [[graphify_tests_test_wheel_packaging]] → `contains` → [[graphify_tests_test_wheel_packaging_has_build]]
- [[graphify_tests_test_wheel_packaging]] → `contains` → [[graphify_tests_test_wheel_packaging_skill_bodies]]
- [[graphify_tests_test_wheel_packaging]] → `contains` → [[graphify_tests_test_wheel_packaging_test_skill_artifact_ships_in_wheel]]
- [[graphify_tests_test_wheel_packaging]] → `contains` → [[graphify_tests_test_wheel_packaging_wheel_namelist]]
- [[graphify_tests_test_wheel_packaging_rationale_1]] → `rationale_for` → [[graphify_tests_test_wheel_packaging]]
- [[graphify_tests_test_wheel_packaging_wheel_namelist]] → `calls` → [[graphify_tests_test_wheel_packaging_has_build]]
- [[graphify_tests_test_wheel_packaging_expected_artifacts]] → `calls` → [[graphify_tests_test_wheel_packaging_skill_bodies]]
- [[graphify_tests_test_wheel_packaging_rationale_33]] → `rationale_for` → [[graphify_tests_test_wheel_packaging_skill_bodies]]
- [[graphify_tests_test_wheel_packaging_skill_bodies]] → `references` → [[graphify_tests_test_wheel_packaging_py_path]]
- [[graphify_tests_test_wheel_packaging_expected_artifacts]] → `references` → [[graphify_tests_test_wheel_packaging_py_path]]
- [[graphify_tests_test_wheel_packaging_test_skill_artifact_ships_in_wheel]] → `references` → [[graphify_tests_test_wheel_packaging_py_path]]
- [[graphify_tests_test_wheel_packaging_rationale_44]] → `rationale_for` → [[graphify_tests_test_wheel_packaging_expected_artifacts]]