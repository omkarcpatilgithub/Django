
from django.urls import path
from .views import article_list, article_detail, raw_input, clear_duplicates, after_duplicate_remove

urlpatterns = [
    path('rooms/', article_list),
    path('detail/<int:pk>', article_detail),
    path('allbooked',raw_input),
    path('clear_dup',clear_duplicates),
    path('after_dup_remove',after_duplicate_remove)


]