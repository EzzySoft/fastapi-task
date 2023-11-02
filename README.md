## Описание

FastAPI приложение для работы с Clickhouse таблицей
Ссылка на контейнер в dockerhub с описанием: https://hub.docker.com/repository/docker/ezzysoft/fastapi-task/general
## Запуск

1. **Загрузите контейнер**

   First, you need to pull the Docker image by running the following command:

   ```bash
   docker pull ezzysoft/fastapi-task:latest
   ```


2. **Запустите контейнер с указанием переменных окружения**
   
    Укажите `port` и Clickhouse `password` затем запустите контейнер:
    
    По умолчанию для переменной `password` установлено значение `GQ25VTN~6lBLI`
    ```bash
    docker run -p 9090:9090 -e PASSWORD=<password> ezzysoft/fastapi-task
    ```
    


# Контакты
Ссылка на резюме: https://innopolis.hh.ru/resume/75d0b254ff0c4829400039ed1f4d536e6e6935