# VulnApp
Уязвимое приложение, которое включает в себя следующие уязвимости: XSS, IDOR, SQL Injection, OS command injection, Path Traversal, Brute Force

### Инструкция по сборке и запуску приложения
1. git clone https://github.com/Oyagee/VulnApp.git
2. pip install -r .\requirements.txt
3. python main.py

# Proof of Concept

### XSS

1. В качестве параметров URL'а можно вводить значение переменной name 
Пример: /?name=123

![image](https://github.com/Oyagee/VulnApp/assets/73120241/05ee5afa-b226-49d1-864c-fe61a24c0a6d)

2. Таким образом в качестве параметра можно вставить XSS Payload
Пример: /?name="<script>alert(123)</script>"

![image](https://github.com/Oyagee/VulnApp/assets/73120241/0e9ba0c1-66a8-4db0-b209-a2556a06cbf8)


### IDOR

![image](https://github.com/Oyagee/VulnApp/assets/73120241/5e444309-1726-4385-9825-4e81f4062251)

Для эксплуатирования IDOR необходимо менять ID пользователя в ссылке http://127.0.0.1:5000/user/1 (создано только два пользователя с id 1 и 2)

![image](https://github.com/Oyagee/VulnApp/assets/73120241/ed70b0e7-7dde-4172-a149-f95848ee8582)


### SQL Injection

url: http://127.0.0.1:5000/sqli/?username=admin&password=pass
url: http://127.0.0.1:5000/sqli/?username=admin&password=pass123
url: http://127.0.0.1:5000/sqli/?username=admin'--

В database хранятся креды учетки админа admin/pass
Если попробовать войти по ним, то успешно войдет
Если изменить пароль или логин, то доступ будет запрещен

Для реализациия SQL Injection необходимо использовать, к примеру, конструкцию "'--", чтобы отбросить остальную часть SQL запроса
Пример: http://127.0.0.1:5000/sqli/?username=admin%27--

### OS command injection

Для эксплуатации данной уязвимости необходимо вводить в форму команды
Например dir /b, которая выведет список файлов в текущей директории
Либо можно с помощью направления информационного выхода записать его в файл: dir /b > file.txt
А затем с помощью команды type file.txt посмотреть содержимое файла
Таким образом можно смотреть содержимое всех файлов, например type main.py

### Path Traversal

url: http://127.0.0.1:5000/pathtraversal/
Для эксплуатация Path Traversal требуется в input ввести название файла, по дефолту обращение происходит в папку Uploads, в котором лежат файлы
Чтобы открывать файлы находящиеся в корневой директории(/) проекта, необходимо использовать следующий синтаксис:

Пример: ../main.py 

![image](https://github.com/Oyagee/VulnApp/assets/73120241/2a7766c7-c619-4a93-895b-538a2ae067d9)


### Brute Force

url: http://127.0.0.1:5000/sqli/

Для брутфорса можно использовать утилиту ffuf

Используя следующую команду и файл с подборкой паролей можно забрутить пароль
```
ffuf -u "http://127.0.0.1:5000/sqli/?username=admin&password=FUZZ" -w C:\Users\USERNAME\Desktop\ffuf\passwords.txt -t 201
```
Таким образом в поле password будут подставляться пароли из password.txt

password.txt находится в папке с проектом



