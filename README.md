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



### SQL Injection

##### PoC:

В database хранятся креды учетки админа admin/pass
Если попробовать войти по ним, то успешно войдет
Если изменить пароль или логин, то доступ будет запрещен

Для реализациия SQL Injection необходимо использовать, к примеру, "'--", чтобы отбросить остальную часть SQL запроса
Пример: http://127.0.0.1:5000/sqli/?username=admin%27--




### OS command injection

### Path Traversal

### Brute Force
