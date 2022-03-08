from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path("stories",views.home ,name='app-home'),
    path("create_new",views.manageTodo ,name='app-create-form'),
    path("manage_todo",views.manageTodo ,name='app-update-form'),
    path("save_todo",views.save_todo ,name='app-save-todo'),
    path("remove_todo",views.delete_todo ,name='app-delete_todo'),
    path("donation",views.donate ,name='app-donation'),
    # path("stories", views.stories, name='stories'),
    path("counsellors", views.counsellors, name='counsellors'),
    path("report", views.reports, name='reports'),
    path("addNewStory", views.createStory, name='add_new_story'),
    path("saveStory", views.save_story, name='save_story'),
    path("awareness", views.awareness, name='awareness'),
]