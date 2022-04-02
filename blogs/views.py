from django.shortcuts import render, redirect,  get_object_or_404
from .models import User, Article, Comment,CommentReply, RoommateHelp
from .forms import CommentForm, ReplyForm, RoommateHelpForm
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.forms  import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from django.contrib.messages import get_messages

# Create your views here.





def loginPage(request):
	page='login'
	#Prevent the user from accessing the login page when the are already logged in
	if request.user.is_authenticated:
		return redirect('blogs:post')

	if request.method=='POST':
		username=request.POST.get('username')
		password=request.POST.get('password')
		try:
			user=User.objects.get(username=username)
		except:
			messages.error(request, 'User does not exits')

		user=authenticate(request, username= username, password=password)
		
		if user is not None:
			login(request, user)
			return redirect('blogs:post')
		else:

			messages.error(request, 'Username or password incorrect')

	context={'page':page}
	return render(request, 'blogs/login_register.html',context)


def logoutUser(request):
	logout(request)
	# return render(request, 'blogs/index.html')
	return redirect ("blogs:post")
 

def registerPage(request):
	form=UserCreationForm()
	if request.method=='POST':
		form=UserCreationForm(request.POST)
		if form.is_valid():
			user=form.save(commit=False)
			#make the username a lower case os it wont be case sensitive to user. i.e even if you enter upper case or lower case username, it would be made lower and allow you in.
			user.username= user.username.lower()
			user.save()
			messages.success(request, 'Congratulation, registration successful!!!')
			#After registering, login the user in automatically
			login(request, user)
			return redirect('blogs:post')
		else:
			messages.error(request,'')
	context={ 'form':form}
	return render(request, 'blogs/login_register.html',context)




#Working Perfectly
def post(request):
	post=Article.objects.all()
	context={'post':post}
	return render (request, 'blogs/index.html', context)




# def email_check(User): 
# 	return User.username.endswith('12g1')





#Working Perfectly
def updatecomment(request, pk):
	#called the Article object(id) so i can pass the id into the redirect link after the updating of the comment. i.e it would go back to that aricle page from where i clicked edit to the update page before
	# ss=Article.objects.get(pk=pk)
	detil=Comment.objects.get(pk=pk)
	#using this query(post) to back to the initial Article.
	post=detil.detil
	form=CommentForm(instance=detil)
	context={'form': form}
	if request.method =='POST':
		form=CommentForm(request.POST, instance=detil)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('blogs:post_detil', args=[str(post.pk)]))
	return render(request, 'blogs/post_detil.html', context)







#working perfectely
@login_required(login_url='blogs:login')
def replycomment(request, pk):
	detil=get_object_or_404(Comment, pk=pk)
	commentreply=detil.reply.all()
	new_reply=None
	if request.method == 'POST':
		comment_reply=CommentReply.objects.create(
			user=request.user,
			detil=detil,
			body=request.POST.get('body')
			)
		return HttpResponseRedirect(reverse('blogs:comment_reply', args=[str(detil.pk)]))

	else:
		form=ReplyForm()
	replycount=commentreply.count()
	context={'detil':detil, 'commentreply':commentreply,'new_reply':new_reply, 'form':form, 'replycount':replycount}
	return render(request, 'blogs/comment_reply.html', context)








# Working Perfectly
@login_required(login_url='blogs:login')
def deletecomment(request, pk):
	comment = get_object_or_404(Comment, pk=pk)
	post= comment.detil
	if request.method =='POST':
		comment.delete()
		return HttpResponseRedirect(reverse('blogs:post_detil', args=[post.pk, ]))
	context={'obj':comment}
	return render (request, 'blogs/delete.html', context)








#Working Perfectely
@login_required(login_url='blogs:login')
def deletereply(request, pk):
	del_reply=get_object_or_404(CommentReply, pk=pk)
	post=del_reply.detil
	if request.method=='POST':
		del_reply.delete()
		return HttpResponseRedirect(reverse('blogs:comment_reply', args=[post.pk, ]))
	context={'obj':del_reply}
	return render (request, 'blogs/delete.html', context)






# the update/edit reply view: The Changes are saving to the database, but the reverse is not returning to the comment reply pages i.e from where it came from 
def updatereply(request, pk):
	edit_reply=get_object_or_404(CommentReply, pk=pk)
	post=edit_reply.detil.pk
	form=ReplyForm(instance=edit_reply)
	if request.method=='POST':
		form=ReplyForm(request.POST,instance=edit_reply)
		if form.is_valid():
			form.save()
			print(edit_reply, edit_reply.pk)
			return redirect('blogs:comment_reply', pk=post)
			# return HttpResponseRedirect(redirect('blogs:comment_reply', args=[post]))
	context={'form': form, 'edit_reply':edit_reply, 'post':post}
	return render(request, 'blogs/edit_reply.html', context)








#Working perfectly
def about (request):
	return render(request, "blogs/about.html")

# @user_passes_test(email_check, login_url="blogs:login")
def post_detil (request, pk):
	post=Article.objects.all()
	detil=Article.objects.get(pk=pk)
	comments=detil.comments.all()
	new_comment=None
	if request.method == 'POST':
		comment=Comment.objects.create(
			user=request.user,
			detil=detil,
			body=request.POST.get('body'),
			)
		
		return HttpResponseRedirect(reverse('blogs:post_detil', args=[str(detil.pk)]))
	else:
		form=CommentForm()
	#count the number of comments 
	count=comments.count()
	context={'count':count, 'detil':detil, 'post':post, 'comments':comments, 
	'new_comment':new_comment, 'form':form, }
	return render(request, 'blogs/post_detil.html',context)
# EduBlog Help Section
def roomMate(request):
	roommate=RoommateHelp.objects.all()
	form=RoommateHelpForm()
	if request.method=='POST':
		form=RoommateHelp.objects.create(
			user=request.user,
			message=request.POST.get('message')
			)
		return redirect('blogs:Edu-help')
	context={'roommate':roommate, 'form':form}
	return render( request, 'blogs/roommate-help.html', context)

def roommateDelete(request, pk):
	roommatepost=RoommateHelp.objects.get(pk=pk)
	if request.method=='POST':
		roommatepost.delete()
		messages.success(request, 'Post deleted successful!!!')
		return redirect('blogs:Edu-help')
	context={'obj':roommatepost}
	return render (request, 'blogs/delete.html',context)

def editroommatePost(request, pk):
	roommatepost=RoommateHelp.objects.get(pk=pk)
	form=RoommateHelpForm(instance=roommatepost)
	if request.method=='POST':
		form=RoommateHelpForm(request.POST,instance=roommatepost)
		if form.is_valid():
			form.save()
			return redirect('blogs:Edu-help')
	context={'form':form}
	return render(request, 'blogs/roommate-help.html', context)