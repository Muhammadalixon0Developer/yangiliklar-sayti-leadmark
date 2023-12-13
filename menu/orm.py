News.objects.all()[:2] #Xoxlagan malumotimizni kesib olish
News.objects.order_by('pk')  # BU malumotlarni tartiblash uchun kerak
News.objects.all().reverse  # bu malumotlarni teskari tariblash uchun kerak
News.objects.filter(pk__lte=2) #Bu malumotlarni id si 2 dan kicik yoki tenglarini filterlab beradi
News.objects.filter() #Bu malumotlarni kerakli malumot bo'yicha filterlab beradi
News.objects.filter(pk__gte=2)#Bu malumotlarni id si 2 dan katta yoki tenglarini filterlab beradi
w=News.objects.get(pk=2)  #id si bo'yicha malumotni olib beradi
w.cat
w.cat.name # catgoriyaning name ni olib beradi



#qayata aloqa qilish uchun

c=Category.objects.get(pk=2)   # catgoriyaning ozini qaytaradi
c.news_set.all() #categoriyadan newsni narsalarini olib beradi
News.objects.filter(title__contains='li') #Kichik harfli malumotlarni topib beradi
News.objects.filter(title__icontains='LI') #katta harfli malumotlarni topib beradi
News.objects.filter(pk__in=[2,3,4,5], is_published=True) #ikkala shart bajarilsagina malumotni qaytaradi
News.objects.filter(cat__in=[1,2]) #Malumotni categoriyadagi id si bo'yicha olib beradi



connection.queries #queriesni ulash. query bu malumot

from django.db.models import Q # or va and ning orniga qollaniluvchi !modul
News.objects.filter(Q(pk__lt=1) | Q(cat_id=1)) # bu or ning orniga qollaniladi
News.objects.filter(Q(pk__lt=1) & Q(cat_id=1)) # bu and ning orniga qollaniladi
News.objects.filter(~Q(pk__lt=1) | Q(cat_id=1)) #not ning orniga qollaniladi


News.objects.first() #modeldagi birinchi malumotni olib beradi
News.objects.last() #modeldagi malumotlarni oxirgisi olib beradi
News.objects.order_by('title').first()

News.objects.latest('time') #vaqti bo'yicha so'ngisini olib beradi
News.objects.earliest('time') # bu  vaqti bo'yicha birinchisini olib beradi


p=News.objects.get(pk=3) #bu pk bilan oberdi
p.get_previous_by_time_update() #bundan avvalgi malumotni olib beradi
p.get_next_by_time_update() #bu bundan keyingi malumotni olib beradi

name=Category.objects.get(pk=3) #bu pk i 3 bolgan kategoriyalardagini olib beradi
name.news_set.exists()  # shu kategoriyada malumot bor tyoqligini qaytaradi / tru/False qayrtaradi
name.news_set.count()  #shu kkategoriyada bor malumotlar sanog'ini qaytaradi

News.objects.filter(pk__lt=10).count() #pk si 10 kichik va tenglarini olib beradi


News.objects.filter(cat_slug='Jahon') #categoriyasi jahon bo'lganlarni olib beradi



News.objects.filter(cat__name__contains='on') #categoriyasi nomida 'on' bo'lganlarini olib beradi

Category.objects.filter(news__title__contains='mir') #bu newsning titleda mir borlarini categoriyasini qaytaradi
Category.objects.filter(news__title__contains='mir').distinct() #bu 2 yoki kop bo'lsaham bittasini olib beradi


News.objects.count() # newsdagi malumotlar sanog'ini qaytaradi
News.objects.aggregate(Min('cat_id'), Max('cat_id')) # bu cat id si min va max lini olib beradi
News.objects.aggregate(cat_min=Min('cat_id'), cat_max=Max('cat_id')) # bu ham yuqoridagi



News.objects.aggregate(res=Sum('cat_id')- Count('cat_id')) #bu cat id si ustida amallarni bajaradi


News.objects.aggregate(res=Avg('cat_id')) #cat id larning kottasini olib beradi


News.objects.values('title', 'cat__name',).get(pk=1) #shu nomli qiymatlarni berilgan pk ga qarab olib beradi
s=News.objects.values('title', 'cat__name') #shu nomli qiymatlarni o'zgaruvchiga tayinlaydi
for p in s:
    print(p['title'], p['cat__name'])




k=Category.objects.annotate(Count('news')) #


k[0].news__count

from django.db.models import F #pastdagi amalni bajarish uchun F kerak
News.objects.filter(pk__gt=F('cat_id'))


from django.db.models.functions import Length

ps=News.objects.annotate(len=Length('title'))
for i in ps:
    print(i.title, i.len)
