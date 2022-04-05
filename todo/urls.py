from django.conf.urls  import url
from todo.views import about,contact,todoadd,todolist,tododelete,todoedit

urlpatterns=[
    url(r'^$',todolist,name='todolist'),
    url(r'^about/$',about,name='about'),
    url(r'^contact/$',contact,name='contact'),
    url(r'^add/$',todoadd,name='todoadd'),
    url(r'^edit/(?P<pk>\d+)$',todoedit,name='todoedit'),
    url(r'^delte/(?P<pk>\d+)$',tododelete,name='tododelete'),
    ]
