from django.shortcuts import render
from django.views import View
from .models import Author, AuthorProfile, Entry, Tag
from django.db.models import Q, Max, Min, Avg, Count


class TrainView(View):
    def get(self, request):
        # Создайте здесь запросы к БД
        max_self_esteem = Author.objects.aggregate(max_self_esteem=Max('self_esteem'))
        self.answer1 = Author.objects.filter(self_esteem=max_self_esteem['max_self_esteem'])  # TODO Какие авторы имеют самую высокую уровень самооценки(self_esteem)?
        max_count_entry = Author.objects.annotate(entry_count=Count('entries')).values('id', 'entry_count').order_by('-entry_count')
        self.answer2 = Author.objects.get(id=max_count_entry[0]['id'])  # TODO Какой автор имеет наибольшее количество опубликованных статей?
        self.answer3 = Entry.objects.filter(Q(tags__name='Кино') | Q(tags__name='Музыка')).distinct()  # TODO Какие статьи содержат тег 'Кино' или 'Музыка' ?
        self.answer4 = Author.objects.filter(gender='ж').count()  # TODO Сколько авторов женского пола зарегистрировано в системе?
        count_authors = Author.objects.aggregate(count_authors=Count('status_rule'))
        self.answer5 = Author.objects.filter(status_rule=True).count()/(count_authors['count_authors']/100)  # TODO Какой процент авторов согласился с правилами при регистрации?
        self.answer6 = Author.objects.filter(authorprofile__stage__range=(1,5))  # TODO Какие авторы имеют стаж от 1 до 5 лет?
        max_age = Author.objects.aggregate(max_age=Max('age'))
        self.answer7 = Author.objects.get(age=max_age['max_age'])  # TODO Какой автор имеет наибольший возраст?
        self.answer8 = Author.objects.filter(phone_number__isnull=False).count()  # TODO Сколько авторов указали свой номер телефона?
        self.answer9 = Author.objects.filter(age__lte=25)  # TODO Какие авторы имеют возраст младше 25 лет?
        count_entry = Author.objects.annotate(entry_count=Count('entries')).values('id', 'entry_count').order_by('id')
        # for idx, value in enumerate(count_entry):
        #     a_id = value['id']
        #     e_count = value['entry_count']
        self.answer10 = None  # TODO Сколько статей написано каждым автором?

        context = {f'answer{index}': self.__dict__[f'answer{index}'] for index in range(1, 11)}

        return render(request, 'train_db/training_db.html', context=context)
