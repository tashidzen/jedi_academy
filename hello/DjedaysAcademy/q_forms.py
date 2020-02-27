from django import forms

class Q_UserForm(forms.Form):
    question_1 = forms.CharField(label="Вопрос 1", initial="Ты готов?",max_length=9)
    answer_1 = forms.BooleanField(label="Ответ 1")
    question_2 = forms.CharField(label="Вопрос 2", initial="Оно тебе надо?",max_length=15)
    answer_2 = forms.BooleanField(label="Ответ 2")
    question_3 = forms.CharField(label="Вопрос 3", initial="Выдержишь ли ты?",max_length=16)
    answer_3 = forms.BooleanField(label="Ответ 3")
