# digiteo-backend

## How to Start

1. activate venv

```bash
python -m venv venv
source venv/Scripts/activate
```

2. dependency install

```bash
pip install -r requirements.txt
```

3. env 파일 만들기
   [.env 파일 만들기](https://www.notion.so/no-devides-found/91266a9c1b3c404da03bfb7e1b25178f?pvs=4)

4. migrate

```bash
python manage.py migrate --settings=digiteo.settings.local
```

5. runserver

```bash
python manage.py runserver --settings=digiteo.settings.local
```
