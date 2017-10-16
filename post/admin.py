from django.contrib import admin

# Register your models here.
from post.models import Post

#admin panelini özelleştirme çabaları..

class PostAdmin(admin.ModelAdmin):
    list_display = ['person', 'publishDate'] # admin panelinde ki tabloya sutun ekledik...
    list_display_links = ['publishDate'] # listedeki elementlere link verdik...
    list_filter = ['publishDate'] #tarihe göre filtreleme yaptık
    search_fields = ['person', 'content'] # kişi adına ve içeriğe göre arama yaptık...
    list_editable = ['person'] #üzerinde değiştirebilme özelliği fakat link olmadıgından emin olmamız lazım...

    class Meta:
        model = Post
admin.site.register(Post, PostAdmin)