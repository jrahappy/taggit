from django.urls import path

from .views import index, page_create, page_update, page_delete, page_detail, page_search, about, index_filter

app_name = "pages"
urlpatterns = [
    path("", index, name="index"),
    path("filter/<slug:tag>/", index_filter, name="filter"),
    path("create/", page_create, name="create"),
    path("update/<int:pk>/", page_update, name="update"),
    path("delete/<int:pk>/", page_delete, name="delete"),
    path("detail/<int:pk>/", page_detail, name="detail"),
    path("search/", page_search, name="search"),
    path("about/", about, name="about"),
]
