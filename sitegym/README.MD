Бэкенд на Django 4.2.1 + DRF для управления расписанием фитнес-тренеров и клиентами.

В данном проекте не реализованы права доступа к API по токену. Нет ограничения для работы с учетными записями 
пользователей.

Тестовая БД лежит в sitegym/db.sqlite3

**Запуск проекта:**
pip install -r requirements.txt
python manage.py runserver

**Базовый URL**
http://127.0.0.1:8000/

Redoc: http://127.0.0.1:8000/redoc/
Swagger UI:  http://127.0.0.1:8000/swagger/

Пагинация (по умолчанию page_size = 10 - записей на страницу):
GET /trainers/?page=2

**1. Пользователи**

`GET /users/` — список пользователей.
`POST /users/` — создать пользователя.
`GET /users/{id}/` — подробная информация о пользователе.
`PUT /users/{id}/` — полное обновление пользователя.
`PATCH /users/{id}/` — частичное обновление пользователя.
`DELETE /users/{id}/` — удалить пользователя.

**1.1 Получить список всех пользователей по 10 записей на страницу**

GET /users/
Пример ответа:
{
  "count": 3,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "email": "ivanov@mail.com",
      "last_name": "Иванов",
      "first_name": "Иван",
      "middle_name": "Иванович",
      "role": "trainer"
    },
    {
      "id": 2,
      "email": "petrov@mail.com",
      "last_name": "Петров",
      "first_name": "Пётр",
      "middle_name": "Петрович",
      "role": "client"
    }
  ]
}

**1.2. Получить пользователя по ID**

GET /users/{id}/

Пример ответа:
{
  "id": 1,
  "email": "ivanov@mail.com",
  "last_name": "Иванов",
  "first_name": "Иван",
  "middle_name": "Иванович",
  "role": "trainer"
}
1.3. Создать нового пользователя

POST /users/

Тело запроса:
{
  "email": "newuser@mail.com",
  "last_name": "Сидоров",
  "first_name": "Сидор",
  "middle_name": "Сидорович",
  "role": "client"
}
Ответ (201):
{
  "id": 4,
  "email": "newuser@mail.com",
  "last_name": "Сидоров",
  "first_name": "Сидор",
  "middle_name": "Сидорович",
  "role": "client"
}

**1.4. Обновить пользователя**

PUT /users/{id}/

Тело запроса:
{
  "last_name": "Сидоров",
  "first_name": "Сидор",
  "middle_name": "Сидорович",
  "role": "trainer"
}
Ответ (200):
{
  "id": 4,
  "email": "newuser@mail.com",
  "last_name": "Сидоров",
  "first_name": "Сидор",
  "middle_name": "Сидорович",
  "role": "trainer"
}
**1.5. Удалить пользователя**

DELETE /users/{id}/

Ответ (204):
Пустое тело ответа.

**************************************************

**2. Клиенты**

`GET /clients/` — список клиентов.
`GET /clients/{id}/` — подробная информация о клиенте.

**2.1. Получить список клиентов**

GET /clients/

Пример ответа (200):
[
  {
    "id": 1,
    "user": {
      "id": 2,
      "email": "petrov@mail.com",
      "last_name": "Петров",
      "first_name": "Пётр",
      "middle_name": "Петрович"
    },
    "phone": "+77010000002"
  }
]

*************************************************

**3. Записи (Booking)**

`GET /trainer-bookings/` — список всех записей клиентов к тренерам.
`POST /trainer-bookings/` — создать запись.

**3.1. Получить список всех записей**

GET /trainer-bookings/

Пример ответа (200):
[
  {
    "id": 1,
    "trainer": {
      "id": 1,
      "full_name": "Иванов Иван Иванович"
    },
    "client": {
      "id": 2,
      "full_name": "Пётр Петров"
    },
    "gym": {
      "id": 1,
      "name": "Зал №1"
    },
    "start_time": "2025-07-25T10:00:00Z",
    "end_time": "2025-07-25T11:00:00Z"
  }
]
**3.2. Создать запись клиента к тренеру**

POST /trainer-bookings/

Тело запроса:
{
  "trainer_id": 1,
  "client_id": 2,
  "gym_id": 1,
  "start_time": "2025-07-25T10:00:00Z",
  "end_time": "2025-07-25T11:00:00Z"
}
Пример ответа (201):
{
  "id": 4,
  "trainer": { "id": 1, "full_name": "Иванов Иван Иванович" },
  "client": { "id": 2, "full_name": "Пётр Петров" },
  "gym": { "id": 1, "name": "Зал №1" },
  "start_time": "2025-07-25T10:00:00Z",
  "end_time": "2025-07-25T11:00:00Z"
}

*****************************************************

**4. Тренеры**

`GET /trainers/` — список тренеров.
`GET /trainers/{id}/` — подробная информация о тренере.
`GET /trainers/{id}/schedule/` — расписание тренера по залам.

**4.1. Получить список тренеров**

GET /trainers/

Пример ответа (200):
{
  "count": 2,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "user": {
        "id": 1,
        "last_name": "Иванов",
        "first_name": "Иван",
        "middle_name": "Иванович",
        "email": "ivanov@mail.com"
      },
      "gender": "male",
      "birth_date": "1990-03-10",
      "gyms": [
        {
          "id": 1,
          "name": "Зал №1",
          "address": "г. Петропавловск, ул. Абая, 10"
        }
      ]
    }
  ]
}

**4.2. Получить тренера по ID**

GET /trainers/{id}/

Пример ответа (200):
{
  "id": 1,
  "user": {
    "id": 1,
    "last_name": "Иванов",
    "first_name": "Иван",
    "middle_name": "Иванович",
    "email": "ivanov@mail.com"
  },
  "gender": "male",
  "birth_date": "1990-03-10",
  "gyms": [
    {
      "id": 1,
      "name": "Зал №1",
      "address": "г. Петропавловск, ул. Абая, 10"
    }
  ]
}

**4.3. Получить расписание тренера**

GET /trainers/{id}/schedule/

Пример ответа (200):
[
  {
    "id": 1,
    "gym": {
      "id": 1,
      "name": "Зал №1"
    },
    "start_time": "2025-07-18T10:00:00Z",
    "end_time": "2025-07-18T11:00:00Z",
    "client": {
      "id": 2,
      "full_name": "Пётр Петров"
    }
  },
  {
    "id": 2,
    "gym": {
      "id": 2,
      "name": "Зал №2"
    },
    "start_time": "2025-07-19T09:00:00Z",
    "end_time": "2025-07-19T10:00:00Z",
    "client": null
  }
]

*****************************************************

Фильтр по роли пользователя:

GET /users/?role=trainer

****************************************************
Структура базы данных

1. Таблица users_user
    id — PK, целое число.
    email — Email пользователя (уникальный).
    first_name — Имя.
    last_name — Фамилия.
    middle_name — Отчество.
    role — Роль (client, trainer, admin).
    is_active — Логическое, активен ли пользователь.
    is_staff — Логическое, флаг персонала.
    is_superuser — Логическое, флаг суперпользователя.
    password — Хэш пароля.
    last_login — Дата/время последнего входа.

2. Таблица users_trainer_profile
    id — PK.
    user_id — FK → users_user.
    gender — Пол (male, female).
    birth_date — Дата рождения.
    gyms — M2M → gym_room.

3. Таблица users_client_profile
    id — PK.
    user_id — FK → users_user.
    phone — Телефон клиента.
    trainers — M2M → users_trainer_profile.

4. Таблица gym_room
    id — PK.
    name — Название зала.
    address — Адрес.
    capacity — Вместимость.
    phone — Контактный телефон.
    
5. Таблица schedule_model
    id — PK.
    trainer_id — FK → users_trainer_profile.
    gym_id — FK → gym_room.
    start_time — Дата и время начала занятия.
    end_time — Дата и время окончания занятия.
    client_id — FK → users_client_profile (может быть NULL, если слот свободен).

**erDiagram**

    USERS_USER {
        bigint id PK
        string email
        string first_name
        string last_name
        string middle_name
        string role "trainer|client|admin"
    }

    USERS_TRAINER_PROFILE {
        bigint id PK
        bigint user_id FK -> USERS_USER.id
        date   birth_date
        string gender "male|female"
    }

    USERS_CLIENT_PROFILE {
        bigint id PK
        bigint user_id FK -> USERS_USER.id
        string phone
    }

    GYM_ROOM {
        bigint id PK
        string name
        string address
        int    capacity
        string phone
    }

    SCHEDULE_MODEL {
        bigint id PK
        bigint trainer_id FK -> USERS_TRAINER_PROFILE.id
        bigint gym_id FK -> GYM_ROOM.id
        datetime start_time
        datetime end_time
        bigint client_id FK NULL -> USERS_CLIENT_PROFILE.id
    }

    %% Связи
    USERS_USER ||--o| USERS_TRAINER_PROFILE : "1 к 0..1 (тренер)"
    USERS_USER ||--o| USERS_CLIENT_PROFILE  : "1 к 0..1 (клиент)"

    USERS_TRAINER_PROFILE }o--o{ GYM_ROOM : "работает в"
    USERS_TRAINER_PROFILE }o--o{ USERS_CLIENT_PROFILE : "ведёт клиентов"

    USERS_TRAINER_PROFILE ||--o{ SCHEDULE_MODEL : "слоты расписания"
    GYM_ROOM ||--o{ SCHEDULE_MODEL : "занятия в зале"
    USERS_CLIENT_PROFILE ||--o{ SCHEDULE_MODEL : "записи клиента"

| Связь                              | Тип                               | Описание                                                                                                           |
| ---------------------------------- | --------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| `User` → `TrainerProfile`          | OneToOne (опционально)            | Пользователь может быть тренером.                                                                                  |
| `User` → `ClientProfile`           | OneToOne (опционально)            | Пользователь может быть клиентом.                                                                                  |
| `TrainerProfile` ↔ `GymRoom`       | ManyToMany                        | Тренер может работать в нескольких залах; в одном зале может быть несколько тренеров.                              |
| `TrainerProfile` ↔ `ClientProfile` | ManyToMany                        | Тренер может вести несколько клиентов, клиент может заниматься у нескольких тренеров.                              |
| `ScheduleModel`                    | FK на Trainer, Gym, (опц.) Client | Отдельный слот расписания: какой тренер, какой зал, время; если клиент записан — указано, иначе `NULL` (свободно). |

промежуточные таблицы (M2M)
| Таблица                         | Поля                                    | Назначение                    |
| ------------------------------- | --------------------------------------- | ----------------------------- |
| `users_trainer_profile_gyms`    | `trainerprofile_id`, `gymroom_id`       | Связь тренеров и залов.       |
| `users_trainer_profile_clients` | `trainerprofile_id`, `clientprofile_id` | Связь тренеров и их клиентов. |

