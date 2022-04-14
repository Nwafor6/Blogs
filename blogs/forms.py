from django import forms
from .models import Comment,CommentReply, RoommateHelp , Market


class CommentForm(forms.ModelForm):
	# user= forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class':'form-control', 'Placeholder':'Enter Username' }))
	body=forms.CharField(max_length=100, widget=forms.Textarea(attrs={'class':'form-control','Placeholder':'Comment here','rows':3}))
	class Meta:
		model=Comment
		comment_image= forms.ImageField(required=False)
		fields=[ 'body','comment_image']
		
class ReplyForm(forms.ModelForm):
	# user= forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class':'form-control', 'Placeholder':'Enter Username' }))
	body=forms.CharField(max_length=100, widget=forms.Textarea(attrs={'class':'form-control','Placeholder':'Enter reply here...','rows':3}))
	class Meta:
		model=CommentReply
		fields=[ 'body']
		
class RoommateHelpForm(forms.ModelForm):
	message=forms.CharField(max_length=1000, widget=forms.Textarea(attrs={'class':'form-control','Placeholder':'Enter Enter message here...','rows':3}))
	class Meta:
		model=RoommateHelp
		fields=['message']


class ContactForm(forms.Form):

	message=forms.CharField(max_length=1000, widget=forms.Textarea(attrs={'class':'form-control','Placeholder':'Enter Enter message here...','rows':3}))

class SellForm(forms.ModelForm):

	class Meta:

		model=Market
		fields= ['category', 'product_name', 'product_price', 'product_image', 'contact_details']

		