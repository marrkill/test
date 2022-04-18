# test
Все скачать и заимпортить. 
Запустить по одному - проверить, что глобалки подтянулись
Запустить Runner - означает, что основной бизнес-процесс работает

https://chlist.sitechco.ru/project/30753/checklist

Прописаны
1. Бизнес процесс (есть в постмане)
2. POST (есть на питоне без кейсов, прост запрос)
3. GET (есть на питоне без кейсов, прост запрос)
4. UPDATE
5. DELETE

Собирается стэк
1.  jira/ситичко/redmine/confluense - баг трекинг, воркфлоу, чек листы, тест кейсы, тест планы, дока
2. Swagger/postman/firecamp - api + покрытие тестами + прогоны и тд, websocket
3. Python + framework - авто


newman

newman run https://www.getpostman.com/collections/cb0cea0af1467c8008fb --environment env.json --iteration-data data.csv --globals globals.json --timeout-request 5000

newman run c:\test1.json --reporters cli,html,json,junit --reporter-json-export jsonOut.json --reporter-junit-export xmlOut.xml --reporter-html-export htmlOut.html
