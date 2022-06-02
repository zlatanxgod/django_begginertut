from django.contrib import admin
from django.urls import path,include

from bookreview.views import AuthorView
from bookreview.views import AuthorInstanceView
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('authors/', AuthorView.as_view()),
    path('authors/<int:pk>', AuthorInstanceView.as_view(), name='author-instance')
]