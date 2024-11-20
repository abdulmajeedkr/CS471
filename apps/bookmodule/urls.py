from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="books.index"),
    path('list_books/', views.list_books, name="books.list_books"),
    path('simple/query/', views.simple_query, name="books.simple_query"),
    path('complex/query/', views.complex_query, name="books.complex_query"),
    path('html5/listing/', views.listing, name="books.listing"),
    path('search/', views.search, name="books.search"),
    path('html5/tables/', views.tables, name="books.tables"),
    path('html5/text/formatting/', views.formatting, name="books.formatting"),
    path('html5/links/', views.links, name="books.links"),
    path('<int:bookId>/', views.viewbook, name="books.view_one_book"),
    path('aboutus/', views.aboutus, name="books.aboutus"),
    path('index2/<int:val1>/', views.index2),
    path('<int:bookId>', views.viewbook),
    path('lab8/task1', views.task1),
    path('lab8/task2', views.task2),
    path('lab8/task3', views.task3),
    path('lab8/task4', views.task4),
    path('lab8/task5', views.task5),
    path('lab8/task7', views.task7),

    path('lab9_part1/listbooks', views.listbooks, name="listbooks"),
    path('lab9_part1/addbook', views.addbook, name="addbook"),
    path('lab9_part1/editbook/<int:id>/', views.editbook, name="editbook"),
    path('lab9_part1/deletebook/<int:id>', views.deletebook, name="deletebook"),

    path('lab9_part2/listbooks', views.listbooksform, name="listbooksform"),
    path('lab9_part2/addbook', views.addbookform, name="addbookform"),
    path('lab9_part2/editbook/<int:id>/', views.editbookform, name="editbookform"),
]
