from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Article, Comment
from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer

# Create your views here.
@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':  # READ
        articles = get_list_or_404(Article)  # 직렬화할 인스턴스 들고옴
        serializer = ArticleListSerializer(articles, many=True)  # 직렬화. articles는 여러개이므로 many=True 조건 추가
        return Response(serializer.data)
    elif request.method == 'POST':  # CREATE
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():  # 유효성 검사 후 저장
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # 상태도 같이 보냄
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'GET':  # READ
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    elif request.method == 'DELETE':  # DELETE
        article.delete()
        data = {
            'delete': f'데이터 {article_pk}번이 삭제되었습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':  # UPDATE
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)


@api_view(['GET'])
def comment_list(request):
    comments = get_list_or_404(Comment)
    serializer = CommentSerializer(comments, many=True)  # comments를 CommentSerializer를 통해 직렬화
    return Response(serializer.data)


@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'GET':  # READ
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    elif request.method == 'DELETE':  # DELETE
        comment.delete()
        data = {
            'delete': f'댓글 {comment_pk}번이 삭제되었습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':  # UPDATE
        serializer = CommentSerializer(insatnce=comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)


@swagger_auto_schema(methods=['POST'], request_body=CommentSerializer)
@api_view(['POST'])
def comment_create(request, article_pk):  # CREATE
    article = get_object_or_404(Article, pk=article_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article)
        return Response(serializer.data, status=status.HTTP_201_CREATED)