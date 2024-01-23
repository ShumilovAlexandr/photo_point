import datetime
import json
import time
import requests

import httpx

from datetime import timedelta
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from django.utils import timezone


@require_http_methods(['GET'])
def get_current_course(request):
    # Получаю курс от текущего значения и каждые 10 секунд дополнительный
    # запрос
    # course_list = []
    # for _ in range(10):
    #     data = httpx.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    #     timestamp = timezone.now().strftime('%Y-%m-%m %H:%M:%S')
    #     time.sleep(10)
    #     course_list.append({'timestamp': timestamp,
    #                         'currency': data['Valute']['USD']['CharCode'],
    #                         'value': data['Valute']['USD']['Value']})
    #
    # return JsonResponse({'The current dollar exchange rate': course_list},
    #                     safe=False)

    # Получение исторических значений начиная от текущего момента и далее
    # каждые 10 секунд назад
    historical_values = []
    current_time = timezone.now()
    for i in range(10):
        historical_times = current_time - timedelta(seconds=i*10)
        data = httpx.get(
            f'https://api.exchangerate-api.com/v4/latest/USD'
            f'?base=USD&time={historical_times.strftime("%Y-%m-%m %H:%M:%S")}'
        ).json()

        historical_values.append(
            {'date_time': historical_times.strftime('%Y-%m-%m %H:%M:%S'),
             'currency': data['rates']['RUB']}
        )
    return JsonResponse(
        {'The current dollar exchange rate': historical_values}
    )

