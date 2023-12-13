"""Bu pagination uchun sqilinadigan kodlar """
from django.core.paginator import Paginator

cars = ['cobalt', 'bmw m5', 'bmw m4 competiton', 'bmw x7', 'onix'] #modellarimiz
title = Paginator(cars, 3) #pGINtorni import  qilish va sahifalar sonini ko'rsatish
title.count # dagi narlsalarni sanog'i
5
title.num_pages # sahifalar soni
2

title.page_range
range(1, 3)

title.page(1)
<Page 1 of 2>

car = title.page(1)

car
<Page 1 of 2>

car.object_list
['cobalt', 'bmw m5', 'bmw m4 competiton']

car.has_next()
True

car.has_previous()
False

car.has_other_pages()
True

car.next_page_number()
2

car.previous_page_number()
Traceback (most recent call last):
  File "C:\Program Files\JetBrains\PyCharm Community Edition 2023.1.3\plugins\python-ce\helpers\pydev\pydevconsole.py", line 364, in runcode
    coro = func()
           ^^^^^^