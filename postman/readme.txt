Все скачать и заимпортить, лучше через ссылки 
Запустить по одному - проверить, что глобалки подтянулись
Запустить Runner - означает, что основной бизнес-процесс работает
Запускать newman через консоль в папке. где лежат файлы

1. Бизнес процесс
https://www.getpostman.com/collections/b52ec9311c37b9fbbcca
Запуск
newman run https://www.getpostman.com/collections/b52ec9311c37b9fbbcca --globals workspace.postman_globals.json

2. POST(1-3)
https://www.getpostman.com/collections/ab8f8b240029d4592db4
Запуск
newman run https://www.getpostman.com/collections/ab8f8b240029d4592db4 --iteration-data post_case_v6.csv

3. POST(4-6)
https://www.getpostman.com/collections/d2bf8857707779662848
Запуск
newman run https://www.getpostman.com/collections/d2bf8857707779662848 --globals workspace.postman_globals.json

4. GET/POST
https://www.getpostman.com/collections/c98bb4a108774c14a1a1
Запуск
newman run https://www.getpostman.com/collections/c98bb4a108774c14a1a1 --globals workspace.postman_globals.json

Проблемы:
1. При изменении структуры в body в POST - не могу пока сделать через один файлик и один прогон
2. POST_Case_4 - создание {} пустого объекта - поле ID надо проверять на непустоту
3. МБ вынести все глобалки в документ, тогда не будут работать 2 папки кейсов POST
