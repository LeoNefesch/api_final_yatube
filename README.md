### О чём проект?
##### Проект написан с применением архитектуры REST
##### Представляет из себя соцсеть со следующими возможностями:
 - авторизация и аутентификация пользователя;
 - добавление, редактирование и удаление пользователем своих постов;
 - возможность классифицировать свои посты по темам;
 - просмотров постов других пользователей;
 - возможность оставлять комментарии;
 - подписка на интересных авторов.

 **Стэк технологий:**
 - VSCode;
 - Python;
 - Django;
 - djangorestframework;
 - djangorestframework-simplejwt;
 - djoser;
 - Pillow;
 - requests;
 - Rest Client VSCode Extension.

**Польза проекта**
- лаконичная реализация REST API;
- позволяет авторизованным пользователям делиться интересными мыслями;
- просматривать посты других пользователей, комментировать и подписываться;
- настоящая соцсеть в миниатюре :)  

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://git@github.com:LeoNefesch/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение :

```
python3.9 -m venv env
```

* Если у вас Linux/macOS

    ```
    source env/bin/activate
    ```
    или
    ```
    . env/bin/activate
    ```

* Если у вас windows

    ```
    source env/scripts/activate
    ```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

При необходимости установить djoser:

```
pip install djoser
```

Нахадясь в папке с файлом manage.py, выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

### Некоторые примеры запросов и ответов:
**Регистрация нового пользователя**
```
POST http://127.0.0.1:8000/api/v1/users/
Content-Type: application/json

{
    "username": "newuser",
    "password": "Change_me"
}
```

**Ответ**
```
{
    "email": "",
    "username": "newuser",
    "id": 1
}
```

**Запрос на получение JWT-токена**
```
POST http://127.0.0.1:8000/api/v1/jwt/create/
Content-Type: application/json
*тело запроса:*
{
    "username": "newuser",
    "password": "Change_me"
}
```

**Ответ**
```
{
    "refresh": "string",
    "access": "string"
}
```

**Запрос на создание публикации**
```
POST http://127.0.0.1:8000/api/v1/posts/
Content-Type: application/json
Authorization: Bearer <jwt-токен, значение ключа "access">

{
    "text": "string",
    "image": "string",
    "group": 0
}
```

**Ответ**
```
{
    "id": 0,
    "author": "string",
    "text": "string",
    "pub_date": "2019-08-24T14:15:22Z",
    "image": "string",
    "group": 0
}
```


### Проект выполнил студент Яндекс Практикума
### [Леонид Негашев](https://github.com/LeoNefesch/)