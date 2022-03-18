from django.shortcuts import render, redirect,  get_object_or_404
from .models import User, Article, Comment,CommentReply
from .forms import CommentForm, ReplyForm
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.


def post(request):
	post=Article.objects.all()
	context={'post':post}
	return render (request, 'blogs/index.html', context)

def post_detil (request, pk):
	#get all Article from the database
	post=Article.objects.all()
	#query the data base of a certain Article us it id
	detil=Article.objects.get(pk=pk)
	#we want to introduce comments to each of the Articles
	#the comments variable referes to comment already in the database
	comments=detil.comments.all()
	#new comment  referes to the comment the user is just about to input
	new_comment=None
	if request.method == 'POST':
		form=CommentForm(request.POST)
		if form.is_valid():
			new_comment=form.save(commit=False)
			new_comment.detil= detil
			new_comment.save()
			return HttpResponseRedirect(reverse('blogs:post_detil', args=[str(detil.pk)]))
	else:
		form=CommentForm()
	#count the number of comments 
	count=comments.count()
	context={'count':count, 'detil':detil, 'post':post, 'comments':comments, 'new_comment':new_comment, 'form':form}
	return render(request, 'blogs/post_detil.html',context)


def updatecomment(request, pk):
	#called the Article object(id) so i can pass the id into the redirect link after the updating of the comment. i.e it would go back to that aricle page from where i clicked edit to the update page before
	ss=Article.objects.get(pk=pk)
	detil=Comment.objects.get(pk=pk)
	form=CommentForm(instance=detil)
	context={'form': form}
	if request.method =='POST':
		form=CommentForm(request.POST, instance=detil)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('blogs:post_detil', args=[str(ss.pk)]))
	return render(request, 'blogs/post_detil.html', context)


def replycomment(request, pk):
	detil=Comment.objects.get(pk=pk)
	commentreply=detil.reply.all()
	new_reply=None
	if request.method == 'POST':
		form=ReplyForm(request.POST)
		if form.is_valid():
			new_reply=form.save(commit=False)
			new_reply.detil=detil
			new_reply.save()
			return HttpResponseRedirect(reverse('blogs:post_detil', args=[str(detil.pk)]))
	else:
		form=ReplyForm()
	replycount=commentreply.count()
	context={'detil':detil, 'commentreply':commentreply,'new_reply':new_reply, 'form':form, 'replycount':replycount}
	return render(request, 'blogs/comment_reply.html', context)



def deletecomment(request, pk):
	comment = get_object_or_404(Comment, pk=pk)
	post= comment.detil
	if request.method =='POST':
		comment.delete()
		return HttpResponseRedirect(reverse('blogs:post_detil', args=[post.pk, ]))
	context={'obj':comment}
	return render (request, 'blogs/delete.html', context)



def deletereply(request, pk):
	del_reply=get_object_or_404(CommentReply, pk=pk)
	post=del_reply.detil
	if request.method=='POST':
		del_reply.delete()
		return HttpResponseRedirect(reverse('blogs:post_detil', args=[post.pk, ]))
	context={'obj':del_reply}
	return render (request, 'blogs/delete.html', context)


# the update/edit reply view
def updatereply(request, pk):
	edit_reply=get_object_or_404(CommentReply, pk=pk)
	post=edit_reply.detil
	form=ReplyForm(instance=edit_reply)
	if request.method=='POST':
		form=ReplyForm(request.POST,instance=edit_reply)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(redirect('blogs:post_detil', args=[post.pk,]))
	context={'form': form, 'edit_reply':edit_reply, 'post':post}
	return render(request, 'blogs/edit_reply.html', context)




def about (request):

	return render(request, "blogs/about.html")



