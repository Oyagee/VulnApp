# VulnApp
Vulnerable application that implements the following vulnerabilities: XSS, IDOR, SQL Injection, OS command injection, Path Traversal, Brute Force

### Инструкция по сборке и запуску приложения

requirements.txt

# Proof of Concept

### XSS

##### PoC:
1. В качестве параметров URL'а можно вводить значение переменной name 
Пример: /?name=123
2. Таким образом в качестве параметра можно вставить XSS Payload
Пример: /?name="<script>alert(123)</script>"

### IDOR

##### PoC:

Для эксплуатирования IDOR необходимо менять ID пользователя в ссылке http://127.0.0.1:5000/user/1 (создано только два пользователя с id 1 и 2)

### SQL Injection

##### PoC:
url: http://127.0.0.1:5000/sqli/?username=admin&password=pass
url: http://127.0.0.1:5000/sqli/?username=admin&password=pass123
url: http://127.0.0.1:5000/sqli/?username=admin'--

В database хранятся креды учетки админа admin/pass
Если попробовать войти по ним, то успешно войдет
Если изменить пароль или логин, то доступ будет запрещен

Для реализациия SQL Injection необходимо использовать, к примеру, конструкцию "'--", чтобы отбросить остальную часть SQL запроса
Пример: http://127.0.0.1:5000/sqli/?username=admin%27--




### OS command injection

### Path Traversal

##### PoC:
url: http://127.0.0.1:5000/pathtraversal/
Для эксплуатация Path Traversal требуется в input ввести название файла, по дефолту обращение происходит в папку Uploads, в котором лежат файлы
Можно попробовать открывать следующее: test.py/test.txt
Чтобы открывать файлы находящиеся в корневой директории(/), необходимо использовать следующий синтаксис:

Пример: ../main.py 

![image](https://github.com/Oyagee/VulnApp/assets/73120241/2a7766c7-c619-4a93-895b-538a2ae067d9)


### Brute Force

##### PoC:
url: http://127.0.0.1:5000/sqli/

Для брутфорса можно использовать утилиту ffuf

Используя следующую команду и файл с подборкой паролей можно забрутить пароль
```
ffuf -u "http://127.0.0.1:5000/sqli/?username=admin&password=FUZZ" -w C:\Users\USERNAME\Desktop\ffuf\passwords.txt -t 201
```
Таким образом в поле password будут подставляться пароли из password.txt
password.txt находится в папке с проектом



