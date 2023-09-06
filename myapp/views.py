from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
import logging
from datetime import datetime

logger = logging.getLogger(__name__)


class MainPageView(TemplateView):
    template_name = 'myapp/index.html'

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['name'] = '��������� ����'
        contex['email'] = 'b222265@yandex.ru'
        contex['phone'] = '+79189251197'
        logger.info(f'��������� �������� index �: {datetime.now()}')
        return contex


class AboutView(TemplateView):
    template_name = 'myapp/about.html'

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['name'] = '��������� ����'
        contex['email'] = 'b222265@yandex.ru'
        contex['phone'] = '+79189251197'
        logger.info(f'��������� �������� about �: {datetime.now()}')
        return contex


def index(request):
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>��� ������ Django-����</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                line-height: 1.5;
                margin: 0;
                padding: 20px;
            }
            
            h1 {
                color: #333;
            }
            
            p {
                color: #777;
            }
        </style>
    </head>
    <body>
        <h1>����� ���������� �� ��� ������ Django-����!</h1>
    
        <h2>� �����</h2>
        <p>���� ���� ���������� � �������������� ������� ���������� Django. ����� ����������� � ������������ ��������� �������� � ������ � ������� �������.</p>
    
        <h2>��� ���</h2>
        <p>������, ���� ����� ��������� ����. � ������� ���������� ������ GeekBrains.</p>
    
        <footer>
            <p>��� ���������� ������: b222265@yandex.ru | +79189251197</p>
        </footer>
    </body>
    </html>
    """
    logger.info(f'��������� �������� index �: {datetime.now()}')
    return HttpResponse(html)


def about(request):
    html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>��� ���</title>
</head>
        <style>
            body {
                font-family: Arial, sans-serif;
                line-height: 1.5;
                margin: 0;
                padding: 20px;
            }
            
            h1 {
                color: #333;
            }
            
            p {
                color: #777;
            }
        </style>
<body>
    <header>
        <h1>������! � ��������� ����</h1>
    </header>

    <main>
        <section>
            <h2>���� ������</h2>
            <ul>
                <li>����� ������ 1</li>
                <li>����� ������ 2</li>
                <li>����� ������ 3</li>
            </ul>
        </section>

        <section>
            <h2>�����������</h2>
            <ul>
                <li>����������� 1</li>
                <li>����������� 2</li>
            </ul>
        </section>

        <section>
            <h2>������</h2>
            <ul>
                <li>����� 1</li>
                <li>����� 2</li>
                <li>����� 3</li>
            </ul>
        </section>
    </main>

    <footer>
        <p>��� ���������� ������: b222265@yandex.ru | +79189251197</p>
    </footer>
</body>
</html>
"""
    logger.info(f'��������� �������� about �: {datetime.now()}')
    return HttpResponse(html)