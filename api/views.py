import datetime
from rest_framework import generics
from .models import Restaurant, Menu, MenuItem, Employee, Vote
from .serializers import (
    RestaurantSerializer,
    MenuSerializer,
    MenuItemSerializer,
    EmployeeSerializer,
    VoteSerializer,
)


class RestaurantListCreateView(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class MenuListCreateView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class MenuItemListCreateView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class CurrentMenuRetrieveView(generics.RetrieveAPIView):
    serializer_class = MenuSerializer

    def get_object(self):
        today = datetime.date.today()
        return Menu.objects.filter(date=today).first()


class CurrentResultsRetrieveView(generics.RetrieveAPIView):
    serializer_class = VoteSerializer

    def get_object(self):
        today = datetime.date.today()
        menu = Menu.objects.filter(date=today).first()
        votes = Vote.objects.filter(menu=menu)
        most_voted_menu_item = votes.order_by("-votes").first()
        return most_voted_menu_item
