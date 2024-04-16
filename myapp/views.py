import logging
from django.http import HttpResponse
from django.shortcuts import render

logger = logging.getLogger(__name__)


# Create your views here.
def index(request):
    logger.info('Index page accessed')
    main_page = '''<!DOCTYPE html>
<html>
<head>
         <title>Главная страница</title>
</head>
<body>
 <h1>Главная страница моего приложения.</h1>
</body>
</html>'''
    return HttpResponse(main_page)


def about(request):
    logger.info('About page accessed')
    about_page = '''<!DOCTYPE html>
<html>
<head>
         <title>Обо мне</title>
</head>
<body>
 <h1>Краткая информация обо мне, как о разработчике приложения.</h1>
</body>
</html>'''
    return HttpResponse(about_page)
