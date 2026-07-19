"""
Tests for the Technology Observatory (``technology-observatory/observatory.py``).

All ``subprocess.run`` calls (``gh`` and ``pip``) are mocked so tests never
require a working GitHub CLI or network access.  File I/O is redirected to
``tmp_path`` to leave the real ``reports/`` directory untouched.
"""

import json
import subprocess
from unittest import mock

import pytest

# ---------------------------------------------------------------------------
# FRAMEWORKS constant
# ---------------------------------------------------------------------------

class TestFrameworksConstant:
    """Verify the ``FRAMEWORKS`` data structure."""

    def test_each_entry_has_required_keys(self, observatory):
        """Every framework entry must contain 'name', 'repo' and 'pypi'."""
        for entry in observatory.FRAMEWORKS:
            assert "name" in entry, f"Missing 'name' in {entry}"
            assert "repo" in entry, f"Missing 'repo' in {entry}"
            assert "pypi" in entry, f"Missing 'pypi' in {entry}"

    def test_all_names_are_non_empty_strings(self, observatory):
        """No framework name should be empty or None."""
        for entry in observatory.FRAMEWORKS:
            assert entry["name"], f"Empty name in {entry}"
            assert isinstance(entry["name"], str)

    def test_known_frameworks_are_present(self, observatory):
        """Key expected frameworks must be in the list."""
        names = {fw["name"] for fw in observatory.FRAMEWORKS}
        for expected in ("graphrag", "mem0", "airllm", "langgraph", "qdrant"):
            assert expected in names, f"Missing expected framework '{expected}'"


# ---------------------------------------------------------------------------
# check_github_repo
# ---------------------------------------------------------------------------

class TestCheckGitHubRepo:
    """``check_github_repo()`` — queries ``gh repo view`` under the hood."""

    def test_parses_valid_json_response(self, observatory):
        """Return the parsed JSON dict when ``gh`` succeeds."""
        fake_stdout = json.dumps({
            "stargazerCount": 42000,
            "forkCount": 1500,
            "updatedAt": "2025-06-15T10:00:00Z",
            "licenseInfo": {"spdxId": "MIT"},
            "defaultBranch": "main",
        })
        with mock.patch.object(observatory.subprocess, "run") as mock_run:
            mock_run.return_value = mock.MagicMock(
                returncode=0, stdout=fake_stdout,
            )
            result = observatory.check_github_repo("owner/repo")

        assert result["stargazerCount"] == 42000
        assert result["forkCount"] == 1500
        assert result["licenseInfo"]["spdxId"] == "MIT"
        assert result["defaultBranch"] == "main"

    def test_non_zero_returncode_returns_empty_dict(self, observatory):
        """Return ``{}`` when the ``gh`` command exits non-zero."""
        with mock.patch.object(observatory.subprocess, "run") as mock_run:
            mock_run.return_value = mock.MagicMock(
                returncode=1, stdout="",
            )
            result = observatory.check_github_repo("owner/repo")

        assert result == {}

    def test_subprocess_exception_returns_empty_dict(self, observatory):
        """Return ``{}`` when ``subprocess.run`` itself raises an exception."""
        with mock.patch.object(observatory.subprocess, "run") as mock_run:
            mock_run.side_effect = subprocess.TimeoutExpired(cmd="gh", timeout=15)
            result = observatory.check_github_repo("owner/repo")

        assert result == {}

    def test_invalid_json_stdout_returns_empty_dict(self, observatory):
        """Return ``{}`` when stdout is not valid JSON."""
        with mock.patch.object(observatory.subprocess, "run") as mock_run:
            mock_run.return_value = mock.MagicMock(
                returncode=0, stdout="not-json-at-all",
            )
            result = observatory.check_github_repo("owner/repo")

        assert result == {}

    def test_calls_expected_gh_command(self, observatory):
        """Verify the exact CLI arguments passed to ``subprocess.run``."""
        with mock.patch.object(observatory.subprocess, "run") as mock_run:
            mock_run.return_value = mock.MagicMock(returncode=0, stdout="{}")
            observatory.check_github_repo("microsoft/graphrag")

        args, kwargs = mock_run.call_args
        assert args[0][0] == "gh"
        assert args[0][1] == "repo"
        assert args[0][2] == "view"
        assert args[0][3] == "microsoft/graphrag"
        assert "--json" in args[0]
        assert kwargs.get("capture_output") is True
        assert kwargs.get("timeout") == 15


# ---------------------------------------------------------------------------
# check_pypi_version
# ---------------------------------------------------------------------------

class TestCheckPyPiVersion:
    """``check_pypi_version()`` — parses output of ``pip index versions``."""

    def test_returns_latest_version(self, observatory):
        """Extract the first version from 'Available versions: ...'."""
        fake_stdout = "Available versions: 3.1.0, 3.0.0, 2.9.0\n"
        with mock.patch.object(observatory.subprocess, "run") as mock_run:
            mock_run.return_value = mock.MagicMock(
                returncode=0, stdout=fake_stdout,
            )
            version = observatory.check_pypi_version("some-package")

        assert version == "3.1.0"

    def test_no_versions_line_returns_unknown(self, observatory):
        """Return ``'unknown'`` when the output lacks 'Available versions:'."""
        fake_stdout = "No matching distribution found for nonexisent\n"
        with mock.patch.object(observatory.subprocess, "run") as mock_run:
            mock_run.return_value = mock.MagicMock(
                returncode=0, stdout=fake_stdout,
            )
            version = observatory.check_pypi_version("nonexisent")

        assert version == "unknown"

    def test_exception_returns_unknown(self, observatory):
        """Return ``'unknown'`` on any subprocess exception."""
        with mock.patch.object(observatory.subprocess, "run") as mock_run:
            mock_run.side_effect = subprocess.CalledProcessError(
                returncode=1, cmd="pip",
            )
            version = observatory.check_pypi_version("broken-pkg")

        assert version == "unknown"

    def test_correct_pip_command(self, observatory):
        """Verify the exact ``pip index versions`` command is built."""
        with mock.patch.object(observatory.subprocess, "run") as mock_run:
            mock_run.return_value = mock.MagicMock(returncode=0, stdout="")
            observatory.check_pypi_version("my-pkg")

        args, kwargs = mock_run.call_args
        cmd = args[0]
        # Should invoke: python -m pip index versions <package>
        assert "-m" in cmd
        assert "pip" in cmd
        assert "index" in cmd
        assert "versions" in cmd
        assert "my-pkg" in cmd
        assert kwargs.get("capture_output") is True
        assert kwargs.get("timeout") == 15


# ---------------------------------------------------------------------------
# main()
# ---------------------------------------------------------------------------

class TestMain:
    """``main()`` — end-to-end report generation."""

    def test_writes_report_and_latest_json(self, observatory, tmp_path):
        """Produce at least two JSON files (dated + latest) with correct keys."""
        with (
            mock.patch.object(observatory, "REPORTS_DIR", tmp_path),
            mock.patch.object(observatory, "check_github_repo") as mock_gh,
            mock.patch.object(observatory, "check_pypi_version") as mock_pypi,
        ):
            mock_gh.return_value = {
                "stargazerCount": 100,
                "forkCount": 20,
                "updatedAt": "2024-01-01T00:00:00Z",
                "licenseInfo": {"spdxId": "MIT"},
            }
            mock_pypi.return_value = "1.0.0"
            observatory.main()

        # Check that files were written
        json_files = [p for p in tmp_path.iterdir() if p.suffix == ".json"]
        assert len(json_files) >= 2, (
            f"Expected at least 2 JSON files, got {len(json_files)}"
        )

        # Validate latest.json structure
        latest = tmp_path / "latest.json"
        assert latest.exists(), "latest.json was not written"
        with open(latest) as f:
            report = json.load(f)

        assert "generated_at" in report, "Missing 'generated_at' timestamp"
        assert "frameworks" in report, "Missing 'frameworks' list"
        assert len(report["frameworks"]) == len(observatory.FRAMEWORKS)

        # Spot-check the first framework entry
        first = report["frameworks"][0]
        assert "name" in first
        assert "repo" in first
        assert "pypi" in first
        assert "latest_pypi" in first
        assert "github_stars" in first
        assert "github_forks" in first
        assert "license" in first
        assert "checked_at" in first

    def test_report_contains_all_framework_names(self, observatory, tmp_path):
        """Every framework from FRAMEWORKS must appear in the output report."""
        with (
            mock.patch.object(observatory, "REPORTS_DIR", tmp_path),
            mock.patch.object(observatory, "check_github_repo",
                              return_value={"licenseInfo": {"spdxId": "MIT"}}),
            mock.patch.object(observatory, "check_pypi_version",
                              return_value="1.0.0"),
        ):
            observatory.main()

        with open(tmp_path / "latest.json") as f:
            report = json.load(f)

        reported_names = {fw["name"] for fw in report["frameworks"]}
        expected_names = {fw["name"] for fw in observatory.FRAMEWORKS}
        assert reported_names == expected_names

    def test_github_failure_gracefully_reported(self, observatory, tmp_path):
        """When ``gh`` fails, fields should be ``None`` rather than crash."""
        with (
            mock.patch.object(observatory, "REPORTS_DIR", tmp_path),
            mock.patch.object(observatory, "check_github_repo",
                              return_value={}),
            mock.patch.object(observatory, "check_pypi_version",
                              return_value="unknown"),
        ):
            observatory.main()

        with open(tmp_path / "latest.json") as f:
            report = json.load(f)

        for fw in report["frameworks"]:
            assert fw["github_stars"] is None
            assert fw["github_forks"] is None
            assert fw["latest_pypi"] == "unknown"
            assert fw["license"] == "unknown"
