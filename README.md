# python_basic — учебные решения Moodle (темы 1–7)

| Папка | Содержание |
|---|---|
| `sissejuhatus/` | Основы Python: 45 упражнений + `opilase_paev.py` |
| `2_tingimuslaused/` | Условия: 32 упражнения + `opilase_tulemus.py` |
| `3_tsuklid/` | Циклы: 42 упражнения + `arvude_analuusaator.py` |
| `4_soned/` | Строки и Tkinter: 40 упражнений |
| `5_jarjendid/` | Списки и файлы: 37 упражнений + контрольная |
| `6_funktsioonid/` | Функции: 50 упражнений + контрольная |
| `7_andmevahetus/` | Файлы и веб-данные: 38 упражнений + контрольная |

Всего 290 Python-файлов. Все прошли синтаксическую проверку `compileall`; интерактивные, сетевые и графические программы ещё требуют запуска в соответствующем окружении.

## Проверка синтаксиса

Из корня проекта:

```bash
python3 -m compileall -q sissejuhatus 2_tingimuslaused 3_tsuklid 4_soned 5_jarjendid 6_funktsioonid 7_andmevahetus
```

## Tkinter в Ubuntu

Если `import tkinter` завершается с `ModuleNotFoundError`, установи системный пакет:

```bash
sudo apt update
sudo apt install python3-tk
```

Затем в том же виртуальном окружении, которое выбрано в VS Code, проверь:

```bash
python -c "import tkinter; print(tkinter.TkVersion)"
```

Не используй `pip install tkinter`: в Ubuntu это системная зависимость Python.

## Git

Корневой `.gitignore` исключает `.venv/`, `venv/`, `__pycache__/` и файлы байткода. Перед коммитом проверяй `git status --short` и не добавляй виртуальное окружение.

Перед распаковкой поверх существующего репозитория создай резервную копию: ZIP содержит полный комплект заданий и может заменить одноимённые файлы.
