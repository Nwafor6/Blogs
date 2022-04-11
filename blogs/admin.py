from django.contrib import admin
from .models import  Article, Comment, CommentReply, RoommateHelp,Carousel

# Register your models here.
class AminArticle(admin.ModelAdmin):
	prepopulated_fields ={'slug':('headline',)}


admin.site.register(Article, AminArticle)
admin.site.register(Comment)
admin.site.register(CommentReply)
admin.site.register(RoommateHelp)
admin.site.register(Carousel)