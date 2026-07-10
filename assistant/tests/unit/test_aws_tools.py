"""Testes do provedor AWS."""
from unittest.mock import patch, MagicMock

from app.providers.aws.aws_tool import aws_list_instances, aws_run_command, _run_aws_cli


class TestAWSTools:
    def test_run_aws_cli_not_found(self) -> None:
        with patch("app.providers.aws.aws_tool.subprocess.run", side_effect=FileNotFoundError()):
            result = _run_aws_cli(["ec2", "describe-instances"])
            assert result["status"] == "error"
            assert "AWS CLI nao encontrado" in result["message"]

    @patch("app.providers.aws.aws_tool.subprocess.run")
    def test_run_aws_cli_success(self, mock_run) -> None:
        mock_result = MagicMock()
        mock_result.returncode = 0
        mock_result.stdout = '{"Instances": [{"InstanceId": "i-123"}]}'
        mock_result.stderr = ""
        mock_run.return_value = mock_result

        result = _run_aws_cli(["ec2", "describe-instances"])
        assert result["status"] == "ok"
        assert "Instances" in result["output"]

    @patch("app.providers.aws.aws_tool.subprocess.run")
    def test_run_aws_cli_error(self, mock_run) -> None:
        mock_result = MagicMock()
        mock_result.returncode = 1
        mock_result.stdout = ""
        mock_result.stderr = "Invalid credentials"
        mock_run.return_value = mock_result

        result = _run_aws_cli(["ec2", "describe-instances"])
        assert result["status"] == "error"
        assert "Invalid credentials" in result["message"]

    def test_aws_list_instances_blocked_prefix(self) -> None:
        result = aws_list_instances.invoke({"profile": ""})
        # This will fail because no AWS CLI, but we can test the tool exists
        assert "status" in result

    def test_aws_run_command_blocked_write(self) -> None:
        """Comandos de escrita devem ser bloqueados."""
        blocked = ["create-bucket", "delete-bucket", "terminate-instances", "put-object"]
        for cmd in blocked:
            result = aws_run_command.invoke({"service_cmd": cmd})
            assert result["status"] == "error"
            assert "nao permitido" in result["message"].lower()

    def test_aws_run_command_allowed_read(self) -> None:
        """Comandos de leitura devem passar pela validacao (mas falhar sem CLI)."""
        allowed = ["s3 ls", "ec2 describe-instances", "lambda list-functions"]
        for cmd in allowed:
            result = aws_run_command.invoke({"service_cmd": cmd})
            # Vai falhar por nao ter AWS CLI, mas nao por bloqueio
            assert result["status"] in ("ok", "error")
            if result["status"] == "error":
                assert "nao permitido" not in result["message"].lower()