from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.students_form,name="student_insert"), #get and post request for insert operation
    path('<int:id>/',views.students_form,name="student_update"), #get and post request for update operation
    path('delete/<int:id>/',views.students_delete,name="student_delete"), #get and post request for delete operation
    path('list/',views.students_list,name="student_list"), #get and post request for display all record operation

]
