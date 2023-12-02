# HTTP HTTPS и их параметры 
***
## Лабораторная работа №1

### РГУПС

Скрипт с помощью которого мы получаем информацию о сайте  __[‍РГУПС](https://www.rgups.ru)__: 

`curl rgups.ru -I -v -L -k`
  
Используем такие ключи как:

`-I` - Этот ключ указывает отправить только заголовки HTTP-ответа сервера, без тела ответа.  
`-v` - Этот ключ делает подробный вывод информации о запросе.  
`-L` - Этот ключ указывает следовать перенаправлениям при запросе, если сервер возвращает код (301 или 302).  
`-k` - Этот ключ отключает проверку SSL-сертификата.

Что мы получаем:

```shell
> HEAD / HTTP/1.1 Метод HEAD запрашивает HTTP-заголовок, который сервер отправит в ответ на GET-запрос по указанному URL-адресу.
> Host: rgups.ru Заголовок запроса Host, указывающий доменное имя сервера, к которому отправляется запрос (rgups.ru).
> User-Agent: curl/8.2.1 Заголовок запроса User-Agent, сообщающий серверу информацию о клиенте (curl/8.2.1), который отправляет запрос.
> Accept: */* Заголовок запроса Accept, указывающий клиент предпочитает принимать все типы контента (/).
> Отделяет заголовки запроса и тело запроса. В данном случае тело отсутствует.

> HTTP/1.1 200 OK Статусная строка ответа HTTP/1.1, указывающая успешное выполнение запроса (200 OK).
< Server: nginx/1.19.1  Заголовок ответа Server, содержащий информацию о программном обеспечении сервера (nginx/1.19.1).
< Date: Fri, 15 Sep 2023 07:31:28 GMT Заголовок ответа Date, показывающий дату и время ответа сервера в формате GMT.
< Content-Type: text/html charset=utf-8 Заголовок ответа Content-Type, указывающий на тип данных и кодировку ответа серве (text/html и utf-8).
< Connection: keep-alive Заголовок ответа Connection, информирующий о состоянии соединения (keep-alive) между клиентом и сервером
< X-Powered-By: ProcessWire CMS Заголовок ответа X-Powered-By, указывающий на программное обеспечение, используемое сервером (ProcessWire CMS).
< Set-Cookie: wire=9f8f2c2aeb9ef498d20d0e93631cc882; path=/; HttpOnly; SameSite=Lax Заголовок ответа Set-Cookie, устанавливающий куки для клиента с указанными параметрами.
< Expires: Thu, 19 Nov 1981 08:52:00 GMT Заголовок ответа Expires, указывающий дату и время, после которых ответ считается устаревшим.
< Cache-Control: no-store, no-cache, must-revalidate Заголовок ответа Cache-Control, управляющий кэшированием данных ответа на стороне клиента.
< Pragma: no-cache Заголовок ответа Pragma с директивой no-cache, указывающей на то, что данные ответа не должны кэшироваться.
< 
 
> 0HTTP/1.1 301 Moved Permanently Статусная строка ответа HTTP/1.1 301, указывающая на постоянное перенаправление ресурса.
< Server: nginx/1.19.1 Заголовок ответа Server, содержащий информацию о программном обеспечении сервера (nginx/1.19.1).
> Date: Fri, 15 Sep 2023 07:31:26 GMT Заголовок ответа Date, показывающий дату и время ответа сервера в формате GMT
> Content-Type: text/html Заголовок ответа Content-Type, указывающий на тип данных ответа сервера (text/html).
> Content-Length: 169 Заголовок ответа Content-Length, сообщающий размер тела ответа в байтах (169 байт).
> Connection: keep-alive Заголовок ответа Connection, информирующий о состоянии соединения (keep-alive) между клиентом и сервером.
< Location: https://rgups.ru/  Заголовок ответа Location, указывающий URL-адрес нового местоположения ресурса для перенаправления

> HTTP/1.1 200 OK Статусная строка ответа HTTP/1.1, указывающая на успешное выполнение запроса (200 OK) после перенаправления.
< Server: nginx/1.19.1 Заголовок ответа Server, содержащий информацию о программном обеспечении сервера (nginx/1.19.1).
> Date: Fri, 15 Sep 2023 07:31:28 GMT Заголовок ответа Date, показывающий дату и время ответа сервера в формате GMT.
> Content-Type: text/html; charset=utf-8 Заголовок ответа 
> Content-Type, указывающий на тип данных и кодировку ответа сервера (text/html и utf-8).
> Connection: keep-alive Заголовок ответа Connection, информирующий о состоянии соединения (keep-alive) между клиентом и сервером.
> X-Powered-By: ProcessWire CMS Заголовок ответа X-Powered-By, указывающий на программное обеспечение, используемое сервером (ProcessWire CMS).
< Set-Cookie: wire=9f8f2c2aeb9ef498d20d0e93631cc882; path=/; HttpOnly; SameSite=Lax Заголовок ответа Set-Cookie, устанавливающий куки для клиента с указанными параметрами.
> Expires: Thu, 19 Nov 1981 08:52:00 GMT Заголовок ответа Expires, указывающий дату и время, после которых ответ считается устаревшим.
> Cache-Control: no-store, no-cache, must-revalidate Заголовок ответа Cache-Control, управляющий кэшированием данных ответа на стороне клиента.
> Pragma: no-cache Заголовок ответа Pragma с директивой no-cache, указывающей на то, что данные ответа не должны кэшироваться.
```

### GitHub

Скрипт с помощью которого мы получаем информацию о сайте  __[GitHub](https://github.com/)__:

`curl github.com -I -v -L -k`

Что мы получаем:

```shell
> HEAD / HTTP/1.1
> Host: github.com
> User-Agent: curl/8.0.1
> Accept: */*
>
< HTTP/1.1 200 OK
< Server: GitHub.com
< Date: Fri, 15 Sep 2023 07:55:34 GMT
< Content-Type: text/html; charset=utf-8
< Vary: X-PJAX, X-PJAX-Container, Turbo-Visit, Turbo-Frame, Accept-Language, Accept-Encoding, Accept, X-Requested-With -  Этот заголовок указывает на факторы, которые могут влиять на кэширование ответа на стороне клиента или прокси-сервера. 
< content-language: en-US - Этот заголовок указывает на язык контента, который отправляется в ответе.
< ETag: W/"aa79b40beb07f510ff7a2bb5f2081380" - Этот заголовок представляет собой метку, которая идентифицирует уникальную версию ресурса. Он используется для управления кэшированием на стороне клиента. Если ресурс изменяется, ETag изменяется, и клиент может использовать его для определения, нужно ли ему получить обновленную версию ресурса.
< Cache-Control: max-age=0, private, must-revalidate
< Strict-Transport-Security: max-age=31536000; includeSubdomains; > < preload - Этот заголовок относится к безопасности. Он указывает, что клиент должен поддерживать строгую защиту транспортного уровня (HTTPS) в течение 31536000 секунд и включать поддомены 
< X-Frame-Options: deny - Это мера безопасности, которая может помочь предотвратить атаки.
< X-Content-Type-Options: nosniff - Этот заголовок предотвращает браузер от интерпретации содержимого как чего-то, отличного от указанного в Content-Type.
< X-XSS-Protection: 0 - Этот заголовок указывает на то, что браузер не должен активировать механизм защиты от межсайтового скриптового выполнения (XSS)
< Referrer-Policy: origin-when-cross-origin, strict-origin-when-cross-origin - Этот заголовок управляет тем, какой информацией о предыдущей странице делится браузер при переходе по ссылке.
< Set-Cookie: logged_in=no; Path=/; Domain=github.com; Expires=Wed, 11 Sep 2024 14:43:05 GMT; HttpOnly; Secure; SameSite=Lax 
< Accept-Ranges: bytes - Этот заголовок указывает, что сервер поддерживает диапазоны запросов для данного ресурса.
< X-GitHub-Request-Id: 2E8B:15B8:5BC1C76:5D0480A:64FF2779 - Этот заголовок содержит идентификатор запроса, который может быть полезен для отслеживания запроса на стороне сервера.
```

### РЖД

Скрипт с помощью которого мы получаем информацию о сайте __[РЖД](https://www.rzd.ru/)__:

`curl rzd.ru -I -v -L -k`

Что мы получаем:

```shell
> HEAD / HTTP/1.1 - Запрос HEAD HTTP/1.1. Метод HEAD запрашивает HTTP-заголовок, который сервер отправит в ответ на GET-запрос по указанному URL-адресу.
> Host: rzd.ru Заголовок запроса Host, указывающий доменное имя сервера, к которому отправляется запрос (rzd.ru).
> User-Agent: curl/8.2.1 Заголовок запроса User-Agent, сообщающий серверу информацию о клиенте (curl/8.2.1), который отправляет запрос.
> Accept: */* Заголовок запроса Accept, указывающий клиент предпочитает принимать все типы контента (/).
>
* schannel: server closed the connection
< HTTP/1.1 403 Forbidden  Статусная строка ответа HTTP/1.1, указывающая на запрещенный доступ к ресурсу (403 Forbidden).
< Connection: close Заголовок ответа Connection, информирующий о состоянии соединения (close) между клиентом и сервером.
< Content-Length: 109 Заголовок ответа Connection, информирующий о состоянии соединения (close) между клиентом и сервером.
< Content-Type: text/html text/html: Заголовок ответа Content-Type, указывающий на тип данных ответа сервера (text/html).
<
> HTTP/1.1 301 Moved Permanently Статусная строка ответа HTTP/1.1 301, указывающая на постоянное перенаправление ресурса.
> Date: Fri, 15 Sep 2023 07:57:59 GMT
> Content-Type: text/html
> Content-Length: 150 Заголовок ответа Content-Length, сообщающий размер тела ответа в байтах (150 байт).
> Connection: keep-alive
> Location: https://rzd.ru:443/
```

### Yandex

Скрипт с помощью которого мы получаем информацию о сайте __[Яндекс](https://yandex.ru/)__:

`curl yandex.ru -I -v -L -k`

Что мы получаем:

```shell
> HEAD /?yredirect=true HTTP/1.1 - Этот запрос будет направлен на сервер с указанием пути / и параметра запроса yredirect=true, и сервер должен ответить только заголовками ресурса, без передачи фактического содержимого.
> Host: dzen.ru
> User-Agent: curl/8.0.1
> Accept: */*
>
< HTTP/1.1 200 Ok
< Cache-Control: no-cache, no-store, max-age=0, must-revalidate
< Content-Type: text/html; charset=utf-8
< Set-Cookie: _yasc=lEL1OdfoCCl7jklQgIf8S+Optkf45jvhWHzi3fU4FfbSajUWSDPA9wu8Y7Vyrzr74Q==; domain=.dzen.ru; path=/; expires=Thu, 08 Sep 2033 15:33:37 GMT; secure
< X-Content-Type-Options: nosniff
< X-Frame-Options: deny
< X-Requestid: 379459519.223.1694446417520.59980 -  Этот заголовок содержит идентификатор запроса, который может быть полезен для отслеживания запроса на стороне сервера.
< X-XSS-Protection: 1; mode=block
< X-Yandex-Req-Id: 1694446417486451-151878967925589959100109-production-app-host-sas-zen-518 - Заголовок представляет собой уникальный идентификатор запроса, который полезен для отслеживания запроса на стороне сервера Yandex или системы, которая обрабатывает запросы.
> Content-Type: text/html; charset=utf-8
> Set-Cookie: _yasc=AdJZhkgXWXPclWsFS/fnUPvV6v2x88WiPy3i26KQ6R07/M0PxPSneSqC3iniHXOm; domain=.dzen.ru; path=/; expires=Mon, 12 Sep 2033 08:06:14 GMT; secure
< X-Content-Type-Options: nosniff
< X-Frame-Options: deny
< X-Requestid: 373737889.142.1694765174435.61831
< X-XSS-Protection: 1; mode=block
< X-Yandex-Req-Id: 1694765174368792-427184405324276660000110-production-app-host-sas-zen-277
```

### Python

Скрипт с помощью которого мы получаем информацию о сайте  __[Python](https://www.python.org/)__:

`curl python.org -I -v -L -k`

Что мы получаем:



```shell
> HEAD / HTTP/1.1
> Host: python.org
> User-Agent: curl/8.2.1
> Accept: */*
>
< HTTP/1.1 301 Moved Permanently
< Connection: close
< Content-Length: 0
< Server: Varnish
< Retry-After: 0
< Accept-Ranges: bytes
< Date: Fri, 15 Sep 2023 08:16:39 GMT
< Via: 1.1 varnish
< X-Served-By: cache-bma1647-BMA
< X-Cache: HIT
< X-Cache-Hits: 0
< X-Timer: S1694765800.962505,VS0,VE0
< Location: https://www.python.org/
< Strict-Transport-Security: max-age=315360000; preload
<
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
* Closing connection
* Clear auth, redirects to port from 80 to 443
* Issue another request to this URL: 'https://www.python.org/'
*   Trying 151.101.84.223:443...
* Connected to www.python.org (151.101.84.223) port 443
* schannel: disabled automatic use of client certificate
  0     0    0     0    0     0      0      0 --:--:--  0:00:01 --:--:--     0* using HTTP/1.x
> HEAD / HTTP/1.1
> Host: www.python.org
> User-Agent: curl/8.2.1
> Accept: */*
>
< HTTP/1.1 200 OK
< Connection: keep-alive
< Content-Length: 50392
< Server: nginx
< Content-Type: text/html; charset=utf-8
< X-Frame-Options: SAMEORIGIN
< Via: 1.1 vegur, 1.1 varnish, 1.1 varnish
< Accept-Ranges: bytes
< Date: Fri, 15 Sep 2023 08:16:41 GMT
< Age: 1272
< X-Served-By: cache-iad-kiad7000025-IAD, cache-bma1652-BMA
< X-Cache: HIT, HIT
< X-Cache-Hits: 8, 3
< X-Timer: S1694765802.953450,VS0,VE0
< Vary: Cookie
< Strict-Transport-Security: max-age=63072000; includeSubDomains; preload
```



### Git

Скрипт с помощью которого мы получаем информацию о сайте  __[Git](https://git-scm.com/)__:

`curl git-scm.com -I -v -L -k`

Что мы получаем: 

```shell
> HEAD / HTTP/1.1
> Host: git-scm.com
> User-Agent: curl/8.0.1
> Accept: */*
>
< HTTP/1.1 200 OK
< Date: Fri, 15 Sep 2023 08:16:41 GMT
< Content-Type: text/html; charset=utf-8
< Connection: keep-alive
< X-Frame-Options: SAMEORIGIN
< X-Xss-Protection: 1; mode=block
< X-Content-Type-Options: nosniff
< X-Download-Options: noopen - Этот заголовок указывает, что файлы не должны открываться автоматически после загрузки.
< X-Permitted-Cross-Domain-Policies: none - Этот заголовок указывает, что политики, связанные с кросс-доменными запросами, отсутствуют.
< Referrer-Policy: strict-origin-when-cross-origin
< Cache-Control: public, max-age=14400
< Etag: W/"db69273d9410cbf4536e9d4b3a59685d"
< X-Request-Id: 08e865a2-bae1-4a5d-90cb-b387a1e71555
< X-Runtime: 0.012125 - Этот заголовок указывает на время, затраченное на выполнение запроса на стороне сервера
< Via: 1.1 vegur
< CF-Cache-Status: HIT
< Age: 5122
< Server: cloudflare
< CF-RAY: 805130f80da00e89-AMS - Этот заголовок может содержать информацию о запросе и обработке на стороне Cloudflare.
```

### JetBrains

Скрипт с помощью которого мы получаем информацию о сайте  __[JetBrains](https://www.jetbrains.com/)__:

`curl jetbrains.com -I -v -L -k`

Что мы получаем:

```shell
> HEAD / HTTP/1.1
> Host: www.jetbrains.com
> User-Agent: curl/8.0.1
> Accept: */*
>
< HTTP/1.1 200 OK
< Content-Type: text/html; charset=utf-8
< Content-Length: 47113
< Connection: keep-alive
< Date: Fri, 15 Sep 2023 08:16:41 GMT
< Server: nginx
< X-Content-Type-Options: nosniff
< Referrer-Policy: same-origin
< Expires: Mon, 11 Sep 2023 16:23:58 GMT - Этот заголовок указывает на дату и время истечения срока действия ответа в кэше.
< Cache-Control: max-age=0
< Pragma: no-cache
< X-Frame-Options: DENY
< X-Content-Type-Options: nosniff
< X-Xss-Protection: 1; mode=block
< Strict-Transport-Security: max-age=31536000;
< Vary: Accept-Encoding
< Via: 1.1 c26999728b9b80253ea8308df470deba.cloudfront.net (CloudFront)
< Age: 167
< Set-Cookie: cf_country-region=RU-MOW; Domain=jetbrains.com; Path=/; Secure
< X-Cache: Hit from cloudfront
< X-Amz-Cf-Pop: ARN56-P2 - Этот заголовок содержит информацию о Point of Presence CloudFront, через который прошел запрос.
< X-Amz-Cf-Id: nzXFCf6XZGkdhF33CihLxVYacKmATuF9KgLJfqJNR609Qxa5-ux39A== - Этот заголовок может содержать идентификатор запроса и обработки на стороне CloudFront.
```

### VSC

Скрипт с помощью которого мы получаем информацию о сайте  __[VSC](https://code.visualstudio.com/)__:

`curl code.visualstudio.com -I -v -L -k`

Что мы получаем:

```shell
> HEAD / HTTP/1.1
> Host: code.visualstudio.com
> User-Agent: curl/8.0.1
> Accept: */*
>
< HTTP/1.1 200 OK
< Content-Length: 50213
< Content-Type: text/html; charset=utf-8
< Accept-Ranges: bytes
< ETag: W/"c425-XBxswsHoV0dlJCAKuBbwZ9s5rjQ"
< Strict-Transport-Security: max-age=31536000; includeSubDomains
< Content-Security-Policy: frame-ancestors 'self' -  Этот заголовок определяет политику безопасности контента и разрешает встраивание ресурсов только с текущего домена.
< X-Frame-Options: SAMEORIGIN
< X-XSS-Protection: 1; mode=block
< X-Content-Type-Options: nosniff
< X-Powered-By: ASP.NET
< x-azure-ref: 0MUH/ZAAAAAASb7vV5T3+TLJL4hpnRGDlQU1TMDRFREdFMTkyMgBiZTg3ZGM2ZC00MGY5LTQ1YjAtODgxMC05OTEwODdlZjhiMjk=
< X-Cache: CONFIG_NOCACHE
< Date: Fri, 15 Sep 2023 08:16:41 GMT
```

>>_Дорогу осилит идущий_ ;)