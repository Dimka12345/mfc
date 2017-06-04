from django.conf import settings
from django.db import models
from django.forms import MultiValueField, CharField, MultiWidget, TextInput

from django.core.exceptions import ValidationError

SHORT_TEXT_LEN = 400

class Image(models.Model):
    photo = models.ImageField(null=False, blank=False, upload_to="images/", verbose_name='Изображение')

    def __str__(self):
        return self.photo.name

#class User(models.Model):
   # login = models.CharField(max_length=15)
  #  password = models.CharField(max_length=20)
   # snils = models.ForeignKey('Snils')

   # def __str__(self):
        #return self.login

#class List_of_request(models.Model):
   # request = models.ForeignKey('Request')

    #def __str__(self):
        #return self.title

class Request(models.Model):
    title = models.CharField(max_length=250, verbose_name='Наименование заявки')
    date_of_beginning = models.DateTimeField(blank=False, auto_now_add=True, verbose_name='Дата добавления')
    date_of_ending = models.DateTimeField()
    participant_one = models.ForeignKey('Document', related_name='participant_one', blank=False, default=None)
    participant_two = models.ForeignKey('Document', related_name='participant_two', blank=True, default=None, null=True)
    participant_three = models.ForeignKey('Document', related_name='participant_three', blank=True, default=None, null=True)
    participant_four = models.ForeignKey('Document', related_name='participant_four', blank=True, default=None, null=True)
    participant_five = models.ForeignKey('Document', related_name='participant_five', blank=True, default=None, null=True)
    participant_six = models.ForeignKey('Document', related_name='participant_six', blank=True, default=None, null=True)
    participant_seven = models.ForeignKey('Document', related_name='participant_seven', blank=True, default=None, null=True)
    participant_eight = models.ForeignKey('Document', related_name='participant_eight', blank=True, default=None, null=True)
    participant_nine = models.ForeignKey('Document', related_name='participant_nine', blank=True, default=None, null=True)
    participant_ten = models.ForeignKey('Document', related_name='participant_ten', blank=True, default=None, null=True)
    status_choice = (('подана', 'подана'), ('обрабатывается', 'обрабатывается'), ('завершена', 'завершена'))
    status = models.CharField(max_length=14, choices=status_choice, default='подана')
    service_fk = models.ForeignKey('Service')
    login = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.title

class New(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Содержание')
    time_of_publishing = models.DateTimeField(blank=False, auto_now_add=True, verbose_name='Дата добавления')
    time_of_editing = models.DateTimeField(blank=False, auto_now=True, verbose_name='Дата изменения')
    picture = models.ForeignKey('Image', blank=True, verbose_name='Изображение')

    def __str__(self):
        return self.title

    def get_short_text(self):
        if len(self.text)> SHORT_TEXT_LEN:
            return self.text[:SHORT_TEXT_LEN]
        else:
            return self.text

class Service(models.Model):
    title = models.CharField(max_length=250, verbose_name='Наименование услуги')
    description = models.TextField(verbose_name='Описание')
    cost = models.CharField(max_length=150, verbose_name='Стоимость')
    documents = models.TextField(verbose_name='Перечень необходимых документов')
    count_of_documents = models.IntegerField(default=0, verbose_name='Кол-во необходимых документов')

    def __str__(self):
        return self.title

class Document(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название документа')
    picture = models.ImageField(null=False, blank=False, upload_to="documents/", verbose_name='Фото документа')
    date_of_adding = models.DateTimeField(blank=False, auto_now_add=True, verbose_name='Дата добавления')
    login = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.title

class Passport(models.Model):
    serial_number = models.PositiveIntegerField(unique=True, max_length= 10, verbose_name='Серийный номер')
    code = models.PositiveIntegerField(max_length=6, verbose_name='Код подразделения')
    surname = models.CharField(max_length=40, verbose_name='Фамилия')
    name = models.CharField(max_length=30, verbose_name='Имя')
    middle_name = models.CharField(max_length=35, verbose_name='Отчество')
    sex_choice = (('мужской', 'муж.'), ('женский', 'жен.'))
    sex = models.CharField(max_length=7, choices=sex_choice, default='мужской')
    date_of_birth = models.DateField(verbose_name='Дата рождения')
    place_of_birth = models.CharField(max_length=100, verbose_name='Место рождения')
    issued_by = models.CharField(max_length=100, verbose_name='Кем выдан')
    date_of_issue = models.DateField(verbose_name='Дата выдачи')
    place_of_registration = models.CharField(max_length=100, verbose_name='Место прописки')
    #photo = models.ImageField(null=False, blank=False, upload_to="documents/", verbose_name='Фото документа')
    login = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.surname
        return self.name

class PersonalInfo(models.Model):
    phone = models.PositiveIntegerField(max_length=11, blank=True, default=None, null=True, verbose_name='Номер телефона')
    post = models.EmailField(blank=True, default=None, null=True, verbose_name='Электронная почта')
    snils_number = models.CharField(unique=True, max_length=11, verbose_name='Номер СНИЛС')
    login = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.snils_number
        return self.login


