# Flask Docker CI/CD Demo

Демонстрационный проект Flask приложения с настройкой CI/CD через GitHub Actions.

## Описание

Этот проект демонстрирует полный цикл CI/CD для Flask приложения:

- Автоматическое тестирование
- Сборка Docker-образа
- Публикация образа в Docker Hub
- Проверка образа на уязвимости

## Требования

- Docker
- Python 3.9+
- GitHub аккаунт (для GitHub Actions)
- Docker Hub аккаунт (для публикации образа)

## Локальная разработка

### Настройка окружения

```bash
# Клонировать репозиторий
git clone <url-вашего-репозитория>
cd <название-репозитория>

# Создать виртуальное окружение
python -m venv venv
source venv/bin/activate  # На Windows: venv\Scripts\activate

# Установить зависимости
pip install -r app/requirements.txt
```

### Запуск тестов

```bash
pytest app/tests/
```

### Запуск приложения локально

```bash
python app/main.py
```

## Использование Docker

### Сборка образа

```bash
docker build -t actions-test .
```

### Запуск контейнера

```bash
docker run -p 7890:7890 actions-test
```

Приложение будет доступно по адресу <http://localhost:7890>

## Настройка GitHub Actions

1. Необходимо добавить в репозиторий следующие секреты:
   - `DOCKERHUB_USERNAME` - имя пользователя Docker Hub
   - `DOCKERHUB_TOKEN` - токен доступа Docker Hub

2. GitHub Actions автоматически запустит процесс CI/CD при:
   - Push в ветки `main` или `master`
   - Создании Pull Request в эти ветки
   - Ручном запуске через интерфейс GitHub

## Структура проекта

```
.
├── .github/workflows       # Конфигурация GitHub Actions
│   └── docker-build-push.yml
├── app                     # Исходный код приложения
│   ├── main.py             # Основной файл приложения
│   ├── requirements.txt    # Зависимости Python
│   └── tests/              # Тесты
├── Dockerfile              # Файл для сборки Docker-образа
├── .dockerignore           # Список файлов, игнорируемых при сборке образа
└── README.md               # Документация проекта
```
