Hello, world!
Программа пока поддерживает только IPv4 протокол
 - Основной код лежит в first_ver.py
 - Юниты лежат в test_first_ver.py
Запуск программы осуществляется при помощи командной строки путем передачи пути файла и версии протокола 
```
python C:\Users\...\first_ver.py C:\4\ipv4 4
```

Для корректной работы unit тестов тестовые файлы должны лежать по пути C:\4\ (вы можете изменить данный путь в файле test_first_ver.py)

Пример корректных входных данных:
```
192.168.1.2
192.168.1.3
192.168.1.5
```

В таком случае ответ будет следующим:

```
192.168.1.0/29
```
>Версия Python 3.12

Программа прекращает работу, если в файле будут содержаться некорректные ip адреса

Время выполнения кода: 1.0292530059814453 ms
Время выполнения тестов: 1.5225410461425781 ms
 
