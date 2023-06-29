from django.urls import path
from .views import (
    RestaurantListCreateView,
    MenuListCreateView,
    MenuItemListCreateView,
    EmployeeListCreateView,
    CurrentMenuRetrieveView,
    CurrentResultsRetrieveView,
)

urlpatterns = [
    path(
        "restaurants/",
        RestaurantListCreateView.as_view(),
        name="restaurant-list-create",
    ),
    path("menus/", MenuListCreateView.as_view(), name="menu-list-create"),
    path("menu-items/", MenuItemListCreateView.as_view(), name="menu-item-list-create"),
    path("employees/", EmployeeListCreateView.as_view(), name="employee-list-create"),
    path(
        "current-menu/", CurrentMenuRetrieveView.as_view(), name="current-menu-retrieve"
    ),
    path(
        "current-results/",
        CurrentResultsRetrieveView.as_view(),
        name="current-results-retrieve",
    ),
]
