from django.conf.urls import url
from ToDoApp import views,classViews


urlpatterns = [
    url(r'lists/',view = views.todolistView, name="todolistView"),
    url(r'items/(?P<id>[0-9]*)/$',view = views.perListView,name = "perListView"),


    #these are the custom Class Based Views
    url(r'create/$',view=classViews.ListCreateView.as_view(),name="ToDoListCreateView"),
    url(r'Delete/(?P<pk>[0-9]+)/$',view = classViews.ListDeleteView.as_view(),name = "ToDoListDeleteView"),
    url(r'Update/(?P<pk>[0-9]+)/$',view = classViews.ListUpdateView.as_view(),name = "ToDoListUpdateView"),
    url(r'listview/$',view=classViews.ListListView.as_view(),name = "ToDoListListView"),
    url(r'Detailview/(?P<id>[0-9]+)/',view = classViews.ListDetailView.as_view(),name = "ToDoListDetailView")
]