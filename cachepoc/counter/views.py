import functools
from django.http import HttpResponse
import datetime
from .models import Counter


@functools.lru_cache()
def get_current_number(self):
    print('Get current number')
    number = Counter.objects.last().number

    return HttpResponse(f'Number:{number}')


def update_number(self):
    get_current_number.cache_clear()
    try:
        current_number = Counter.objects.last().number
        new_number = current_number + 1
        Counter.objects.create(number=new_number)
        return HttpResponse(f'Successfully and number is {new_number}')
    except:
        Counter.objects.create(number=1)
        return HttpResponse('Successfully and number is 1')
