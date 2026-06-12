@echo off
REM ============================================================
REM K.A.O.S Local Launcher - Batch version for cmd.exe
REM Detecta Python correto (venv > system), roda uv sync, inicia uvicorn
REM ============================================================

set PROJECT_ROOT=C:\workspace\Extras\K.A.O.S\assistant
set PORT=8000
set HOST=0.0.0.0
set NO_RELOAD=false

REM Parse argumentos
set ARG_COUNT=0
:PARSE_ARGS
if "%~1"=="" goto :PARSE_DONE
if /I "%~1"=="--port" (
    set PORT=%~2
    shift /1
    shift /1
    goto :PARSE_ARGS
)
if /I "%~1"=="--host" (
    set HOST=%~2
    shift /1
    shift /1
    goto :PARSE_ARGS
)
if /I "%~1"=="--no-reload" (
    set NO_RELOAD=true
    shift /1
    goto :PARSE_ARGS
)
shift /1
goto :PARSE_ARGS
:PARSE_DONE

echo ============================================================
echo  K.A.O.S Local Launcher (Batch)
echo Projeto: %PROJECT_ROOT%
echo ============================================================

REM Detecta Python correto
set PYTHON=
if not "%~1"=="" (
    set PYTHON=%~1
) else if exist "%PROJECT_ROOT%\.venv\Scripts\python.exe" (
    set PYTHON=%PROJECT_ROOT%\.venv\Scripts\python.exe
    echo Usando Python do venv: %PYTHON%
) else (
    where python >nul 2>&1
    if not errorlevel 1 (
        for /f "tokens=*" %%i in ('where python') do set PYTHON=%%i
        echo Usando Python do PATH: %PYTHON%
    ) else (
        if exist "C:\Users\brian\AppData\Local\Programs\Python\Python312\python.exe" (
            set PYTHON=C:\Users\brian\AppData\Local\Programs\Python\Python312\python.exe
            echo Usando Python 3.12: %PYTHON%
        ) else (
            echo ERRO: Python nao encontrado! Instale Python 3.12+ ou crie venv.
            exit /b 1
        )
    )
)

REM Verifica/instala UV
where uv >nul 2>&1
if errorlevel 1 (
    echo Instalando UV...
    "%PYTHON%" -m pip install -q uv
)

REM Sync dependências
echo Sincronizando dependencias com UV...
cd /d %PROJECT_ROOT%
"%PYTHON%" -m uv sync

REM Monta comando uvicorn
set UVICORN_ARGS=uvicorn app.main:app --host %HOST% --port %PORT%
if "%NO_RELOAD%"=="false" set UVICORN_ARGS=%UVICORN_ARGS% --reload

echo.
echo Iniciando K.A.O.S em http://%HOST%:%PORT%
echo Modelos: kaos (SMART/qwen3:14b), kaos-rag (MEMORY/qwen3:14b), kaos-fast (FAST/qwen3:4b)
echo Pressione Ctrl+C para parar
echo ----------------------------------------------------------

REM Executa
"%PYTHON%" -m uvicorn app.main:app --host %HOST% --port %PORT% %UVICORN_RELOAD%
if errorlevel 1 (
    echo ERRO: Falha ao iniciar servidor
    exit /b 1
)