from django import forms
from django.contrib import auth
from django.forms import DateField, DateInput, Textarea


from .models import Passport, Service, Request, Document, PersonalInfo


class Passport_Editing_Form(forms.ModelForm):
    class Meta:
        model = Passport
        fields = ['serial_number', 'code', 'surname', 'name', 'middle_name', 'date_of_birth', 'place_of_birth',
                  'issued_by', 'date_of_issue', 'place_of_registration', 'sex']

class Personal_Info_Form(forms.ModelForm):
    class Meta:
        model = PersonalInfo
        fields = ['phone', 'post', 'snils_number']

class Order_Service_Form(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['participant_one', 'participant_two', 'participant_three', 'participant_four', 'participant_five',
                  'participant_six', 'participant_seven', 'participant_eight', 'participant_nine', 'participant_ten']

   # def __init__(self, *args, **kwargs):
     #   if 'document' in kwargs and kwargs['document'] is not None:
     #       document = kwargs.pop('document')
    #    super(Order_Service_Form, self).__init__(*args, **kwargs)
    #    self.fields['participant_one'].queryset = document



class Add_Document_Form(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['title', 'picture']

class Document_Rename_Form(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['title', 'picture']

class Document_Delete_Form(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['title', 'picture']