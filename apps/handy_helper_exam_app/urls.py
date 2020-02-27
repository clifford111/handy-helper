from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^dashboard$', views.all_jobs),
    url(r'^dashboard/addJob$', views.add_job),
    url(r'^dashboard/create$', views.create_job),
    url(r'^dashboard/view/(?P<job_id>\d+)$', views.display_job),
    url(r'^dashboard/edit/(?P<job_id>\d+)$', views.edit_job),
    url(r'^dashboard/update/(?P<job_id>\d+)$', views.update_job),
    url(r'^dashboard/delete/(?P<job_id>\d+)$', views.delete_job),
]