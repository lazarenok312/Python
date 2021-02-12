from .models import Answer
from django import forms

class AnswerForm(forms.ModelForm):
	class Meta:
		model = Answer
		fields = ('body',)
		widgets = {'question': forms.HiddenInput()}

class LikeForm(forms.ModelForm):
	class Meta:
		model = Answer
		fields = ()

class DislikeForm(forms.ModelForm):
	class Meta:
		model = Answer
		fields = ()