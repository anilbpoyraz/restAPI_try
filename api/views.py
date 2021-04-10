# from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# from rest_framework.parsers import JSONParser
from .models import Article
from .serializers import Article_Serializer
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from django.shortcuts import get_object_or_404


class ArticleModalViewSet(viewsets.ModelViewSet):
    serializer_class = Article_Serializer
    queryset = Article.objects.all()


class ArticleGenericViewSet(viewsets.GenericViewSet, mixins.ListModelMixin,
                            mixins.CreateModelMixin, mixins.UpdateModelMixin,
                            mixins.RetrieveModelMixin):
    serializer_class = Article_Serializer
    queryset = Article.objects.all()


class ArticleViewSet(viewsets.ViewSet):

    def list(self, request):
        articles = Article.objects.all()
        serializer = Article_Serializer(articles, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = Article_Serializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = Article.objects.all()
        article = get_object_or_404(queryset, pk=pk)
        serializer = Article_Serializer(article)
        return Response(serializer.data)

    def update(self, request, pk=None):
        article = Article.objects.get(pk=pk)
        serializer = Article_Serializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GenericAPIView(generics.GenericAPIView, mixins.ListModelMixin,
                     mixins.CreateModelMixin, mixins.UpdateModelMixin,
                     mixins.RetrieveModelMixin, mixins.DestroyModelMixin
                     ):
    lookup_field = 'pk'

    serializer_class = Article_Serializer
    queryset = Article.objects.all()
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None):
        if pk:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, pk=None):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)


class ArticleView(APIView):  # class based views API

    def get(self, request):
        articles = Article.objects.all()
        serializer = Article_Serializer(articles, many=True)
        return HttpResponse(serializer.data)

    def post(self, request):
        serializer = Article_Serializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleDetails(APIView):

    def get_object(self, pk):
        try:
            return Article.objects.get(pk=pk)

        except Article.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        article = self.get_object(pk)
        serializer = Article_Serializer(article)
        return Response(serializer.data)

    def put(self, request, pk):
        article = self.get_object(pk)
        serializer = Article_Serializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        article = self.get_object(pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# @api_view(['GET', 'POST'])  # function based views
# def article_list(request):
#    if request.method == 'GET':
#        articles = Article.objects.all()
#        serializer = Article_Serializer(articles, many=True)
#        return Response(serializer.data)
#
#    elif request.method == 'POST':
#        serializer = Article_Serializer(data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data, status=status.HTTP_201_CREATED)
#        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'DELETE'])
# def article_detail(request, pk):
#    try:
#        article = Article.objects.get(pk=pk)
#    except Article.DoesNotExist:
#        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

#    if request.method == 'GET':
#        serializer = Article_Serializer(article)
#        return Response(serializer.data)

#    elif request.method == 'PUT':
#        serializer = Article_Serializer(article, data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#    elif request.method == 'DELETE':
#        article.delete()
#        return Response(status=status.HTTP_204_NO_CONTENT)

# @csrf_exempt       #function based view
# def article_list(request):

#    if request.method == 'GET':
#        articles = Article.objects.all()
#        serializer = Article_Serializer(articles, many=True)
#        return JsonResponse(serializer.data, safe=False)

#    elif request.method == 'POST':
#        data = JSONParser().parse(request)
#        serializer = Article_Serializer(data=data)

#        if serializer.is_valid():
#            serializer.save()
#            return JsonResponse(serializer.data, status=201)
#        else:
#            return JsonResponse(serializer.errors, status=400)

# @csrf_exempt
# def article_detail(request, pk):
#    try:
#        article = Article.objects.get(pk=pk)
#
#    except Article.DoesNotExist:
#        return HttpResponse(status=404)

#    if request.method == 'GET':
#        serializer = Article_Serializer(article)
#        return JsonResponse(serializer.data)
#    elif request.method == 'PUT':
#        data = JSONParser().parse(request)
#        serializer = Article_Serializer(article, data=data)
#        if serializer.is_valid():
#            serializer.save()
#            return JsonResponse(serializer.data)
#        return JsonResponse(serializer.errors, status=400)

#    elif request.method == 'DELETE':
#        article.delete()
#        return HttpResponse(status=204)
