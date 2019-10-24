from django.contrib import admin
from django.urls import path, include
import demo.views

urlpatterns = [
    path('helloWorld', demo.views.hello_world),
    path('index/', demo.views.index),
    path('dataAdd/', demo.views.data_add),
    path('delete/', demo.views.data_delete),
    path('update/', demo.views.update),
    path('select/', demo.views.select)
]
