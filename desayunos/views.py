from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import login, authenticate
from rest_framework import viewsets
from desayunos.serializers import *
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from desayunos.forms import *
from django.http import request


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

    #Devuelve los datos del usuario registrado
    def get_queryset(self):
        if self.request.user.id != None:
            queryset = User.objects.all().filter(pk=self.request.user.id)
            return queryset
        else:
            queryset = User.objects.all()
            return queryset


class BarViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Bar.objects.all()
    serializer_class = BarSerializer


class GroupViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    #Devuelve los grupos al que pertenece el usuario
    def get_queryset(self):
        if self.request.user.id != None:
            queryset = Group.objects.all().filter(user=self.request.user.id)
            return queryset
        else:
            queryset = Group.objects.all()
            return queryset


class ProductTypeViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer


class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class MenuViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class ModifierViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Modifier.objects.all()
    serializer_class = ModifierSerializer


class PivotModifierProductViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = PivotModifierProduct.objects.all()
    serializer_class = PivotModifierProductSerializer


class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


# Registro_de_usuario
def user_register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect('/api/v1/User/')
    else:
        form = UserForm()
    return render(request, 'register.html', {'form': form})