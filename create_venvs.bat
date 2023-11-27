py -3.10 -m venv venv3.10 &&^
.\venv3.10\Scripts\python.exe -m pip install -r requirements-upstream.txt &&^
py -3.10 -m venv venv3.10-ce &&^
.\venv3.10-ce\Scripts\python.exe -m pip install -r requirements-ce.txt &&^
py -3.11 -m venv venv3.11 &&^
.\venv3.11\Scripts\python.exe -m pip install -r requirements-upstream.txt &&^
py -3.11 -m venv venv3.11-ce &&^
.\venv3.11-ce\Scripts\python.exe -m pip install -r requirements-ce.txt &&^
py -3.12 -m venv venv3.12 &&^
.\venv3.12\Scripts\python.exe -m pip install -r requirements-upstream.txt &&^
py -3.12 -m venv venv3.12-ce &&^
.\venv3.12-ce\Scripts\python.exe -m pip install -r requirements-ce.txt &&^
python -m venv venv-other &&^
.\venv-other\Scripts\python.exe -m pip install -r requirements-other.txt
