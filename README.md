В аудитории мы рассмотрели расчет чисел Фибоначчи рекурсией. 
Выполните расчет чисел в Docker. 

Docker должен принимать номер числа фибоначчи и выдавать его значение. Коммуникацю Docker и хоста может быть выполнена любым доступным Вам способом.

В качестве отклика предоставьте ссылку на публичный репозиторий git, 
который будет содержать модуль с вычислением чисел Фибоначчи и 
Dockerfile для запуска этого модуля в изолированной среде Docker (любые 
дополнительные файлы по Вашему усмотрению).

Сборка: `docker build -t <USER>/fib_flask .`

Запуск: `docker run -p 8888:5000 --name fib_flask <USER>/fib_flask`
