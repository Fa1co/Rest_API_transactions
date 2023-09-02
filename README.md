# Rest_API_transactions

REST API для системы учета транзакций

# Эндпоинты:
1) Авторизация. Параметры: email и пароль
2) Записать транзакцию: Параметры: Сумма (Число), Дата(Дата без времени), Категория (Строка) /  Доступно авторизованным пользователям
3) Получить все записанные пользователем тарнзакции (включая прошлые сессии) / Ответ в формате JSON / Доступно авторизованным пользователям

# Варианты использования:
1) Пользователь авторизуется исползуя эндпоинт (1) (если такого пользователя нет то он создается) получает сессионный токен.
2) Пользователь записывает транзакции используя эндпоинт (2)
3) Пользователь может прочитать все свои транзакции используя эндпоинт (3)

# Средства разработки
Фреймворк: Flask
База данных: Sqllite

# База данных
В базе данных используются 2 модели: User и Transaction
```
Модель User:
user_id - Уникальный номер для каждого пользователя
e_mail - Поле, где хранится электронная почта пользователя
password - Поле, где хранится хешированный пароль пользователя
```

```
Модель Transaction:
transaction_id - Уникальный номер транзакций 
transaction_sum - Поле, где хранится сумма транзакций
transaction_date - Поле, где хранится дата транзакций
transaction_category - Поле, где хранится Категория транзакций
user_id - Уникальный номер пользователя
```
