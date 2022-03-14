from django import forms
from .models import Comment,CommentReply


class CommentForm(forms.ModelForm):
	commenter= forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class':'form-control', 'Placeholder':'Your name' }))
	body=forms.CharField(max_length=100, widget=forms.Textarea(attrs={'class':'form-control','Placeholder':'Comment here','rows':3}))
	class Meta:
		model=Comment
		fields=['commenter','body']
		
class ReplyForm(forms.ModelForm):
	commenter= forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class':'form-control', 'Placeholder':'Your name' }))
	body=forms.CharField(max_length=100, widget=forms.Textarea(attrs={'class':'form-control','Placeholder':'Comment here','rows':3}))
	class Meta:
		model=CommentReply
		fields=['commenter','body']
		