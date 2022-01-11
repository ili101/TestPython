```powershell
deactivate
# Remove-Item -Path (Join-Path $env:LOCALAPPDATA 'pypoetry\Cache\') -Recurse
Remove-Item -Path .env, .venv -Recurse
Remove-Item -Path  poetry.lock
poetry install
.\.venv\Scripts\Activate.ps1
pip check
python .\tests\test_my_fun.py
```
WARNING: Error parsing requirements for poetry-demo: Invalid URL: poetry-sub