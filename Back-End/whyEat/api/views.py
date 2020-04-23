<<<<<<< HEAD
from .serializers import UserSerializer, HistorySerializer
from .models import User, User_history
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status

=======
from rest_framework import viewsets
from .serializers import UserSerializer, HistroySerializer, UserCreationSerializer
from .models import User, User_history
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView, ListAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.db.models import Sum
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

from django.conf import settings
from django.contrib.auth import login, logout
from rest_framework import views, generics, response, permissions, authentication
from .serializers import UserSerializer
>>>>>>> ace7afa67e125cbcf281697ddaaf0c174066cddc

# class UserView(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     # permission_classes = (permissions.IsAuthenticated, )
#     # queryset = ''
#     # def perform_create(self, serializer):
#     #     serializer.save(user=self.request.user)


class MultipleFieldLookupMixin(object):
    """
    Apply this mixin to any view or viewset to get multiple field filtering
    based on a `lookup_fields` attribute, instead of the default single field filtering.
    """

    def get_object(self):
        queryset = self.get_queryset()             # Get the base queryset
        queryset = self.filter_queryset(queryset)  # Apply any filter backends
        filter = {}
        for field in self.lookup_fields:
            if self.kwargs[field]:  # Ignore empty fields.
                filter[field] = self.kwargs[field]
        return get_object_or_404(queryset, **filter)


# class UserView(ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


@api_view(['GET','POST'])
def user_list(request):
    if request.method == 'GET':
        qs = User.objects.all()
        serializer = UserSerializer(qs, many=True)
        return Response(serializer.data)
    else:
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET','PUT','DELETE'])
def user_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# class UserViewCreate(CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# class UserViewDetail(RetrieveAPIView):
#     lookup_field = 'id'
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     authentication_classes = (SessionAuthentication, BasicAuthentication)
#     permission_classes = (IsAuthenticated,)


# class UserViewUpdate(UpdateAPIView):
#     lookup_field = 'id'
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     authentication_classes = (SessionAuthentication, BasicAuthentication)
#     permission_classes = (IsAuthenticated,)


# class UserViewDelete(DestroyAPIView):
#     lookup_field = 'id'
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     authentication_classes = (SessionAuthentication, BasicAuthentication)
#     permission_classes = (IsAuthenticated,)


@api_view(['GET','POST'])
def history_list(request):
    if request.method == 'GET':
        qs = User_history.objects.all()
        serializer = HistorySerializer(qs, many=True)
        return Response(serializer.data)
    else:
        serializer = HistorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET','PUT','DELETE'])
def history_detail(request, pk, history_pk):
    # history = User_history.objects.select_related('user').filter(user=pk)
    user = get_object_or_404(User, pk=pk)
    history = User_history.objects.get(pk=history_pk)
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data['history'])
    # user = get_object_or_404(User, pk=pk)
    # if request.method == 'GET':
    #     serializer = UserSerializer(user)
    #     return Response(serializer.data['history'])

    # user = get_object_or_404(User, pk=pk)
    # if request.method == 'GET':
    #     serializer = UserSerializer(user)
    #     return Response(serializer.data['history'])
    
    # elif request.method == 'PUT':
    #     history = User_history.objects.get(pk=history_pk)
    #     serializer = HistorySerializer(history, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # else:
    #     history = get_object_or_404(User_history, pk=history_pk)
    #     history.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

# class HistroyViewCreate(CreateAPIView):
#     lookup_fields = 'user_id'
#     queryset = User_history.objects.all()
#     serializer_class = HistroySerializer


# class RankView(ListAPIView):
#     lookup_field = 'id'
#     # queryset = User_history.objects.all().order_by('total_paid')[:5]
#     queryset = User_history.objects.extra(
#     select={'fieldsum':'user_lunch + user_dinner + user_breakfast'},
#     order_by=('fieldsum',)
#     )[:5]
#     serializer_class = HistroySerializer
    

# class HistroyView(ListAPIView):
#     lookup_field = 'user_id'
#     queryset = User_history.objects.all()
#     serializer_class = HistroySerializer
#     def get_queryset(self):
#         return User_history.objects.filter(user_id=self.kwargs['user_id'])


# class HistoryViewDetail(RetrieveAPIView):
#     lookup_field = 'id'
#     queryset = User_history.objects.all()
#     serializer_class = HistroySerializer
#     def get_queryset(self):
#         return User_history.objects.filter(id=self.kwargs['id'])
        


# class HistoryViewUpdate(UpdateAPIView):
#     lookup_field = 'user_id'
#     queryset = User_history.objects.all()
#     serializer_class = HistroySerializer
#     def get_queryset(self):
#         return User_history.objects.filter(id=self.kwargs['id'], user_id=self.kwargs['user_id'])

# class HistroyViewDelete(DestroyAPIView):
#     lookup_field = 'user_id'
#     queryset = User_history.objects.all()
#     serializer_class = HistroySerializer
#     def get_queryset(self):
#         return User_history.objects.filter(id=self.kwargs['id'] ,user_id=self.kwargs['user_id'])
