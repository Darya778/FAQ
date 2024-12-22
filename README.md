# FAQ

Сделать FAQ чат-бот для работы без интернета на tensorflow.

Должен отвечать на вопросы из жизни университета/факультета/кафедры на русском языке.

Остовная (backbone) сеть - любая небольшая языковая модель с поддержкой русского языка. Можно RuBERT.

Схема тренировки - Poly-encoder

Количество базовых пар вопрос-ответ - не менее 50.

Приложение должно состоять из двух программ - программа для тренировки и дистрибутив для установки на машине с питоном. Приложение должно работать (UI) либо через консоль, либо через библиотеку tkinter на ваш выбор.
