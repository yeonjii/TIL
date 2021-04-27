# Django REST Framework - 1:N Relation

1:N 관계에서의 모델 data를 직렬화(Serialization)하여 JSON으로 변환하는 방법

<br>

## Comment 기능 구현

- 모델링

```python
# models.py

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

- migration 전 db 삭제 후 새로 migration 작업 수행

```bash
$ python manage.py makemigrations
$ python manage.py migrate

$ python manage.py seed articles --number=20
Seeding 20 Articles
Seeding 20 Comments
```

데이터 잘 생성 되는지 확인 !

<br>

## 댓글 1개 가져오기 - Detail (GET)

```python
# urls.py

urlpatterns = [
    ...,
    path('comments/<int:comment_pk>/', views.comment_detail),
]
```

```python
# views.py

@api_view(['GET'])
def comment_detail(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    serializer = CommentSerializer(comment)
    return Response(serializer.data)
```

http://127.0.0.1:8000/api/v1/comments/1  GET, POST 확인 !

<br>

## 댓글 생성하기 - CREATE (POST)

Article 생성과 달리 Create는 생성시 모델관계 객체가 필요하다.

```python
# urls.py

urlpatterns = [
    ...,
    path('<int:article_pk>/comments/', views.comment_create),
]
```

**읽기 전용 필드 설정**

- form 데이터를 입력 받는게 아니면 `read_only = True` 를  설정해줘야한다.

```python
# serializers.py

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article',)
```

<br>

✔ **`.save()`에 추가 속성 전달**

- `save()` 메서드는 특정 Serializer 인스턴스를 저장하는 과정에서 추가적인 데이터를 받을 수 있다.
- `CommentSerializer`를 통해 Serializing되는 과정에서 Query String Parameter로 넘어온 `article_pk`에 해당하는 article 객체를 추가적인 데이터를 넘겨 저장한다.
- 그러면 어떤 게시글에 속하는 데이터인지 명시하여 데이터 요청을 하지 않아도 댓글 작성이 가능하다.

```python
# views.py

@api_view(['POST'])
def comment_create(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = CommentSerializer(data=request.data) 
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article)  # 추가 속성 전달
        return Response(serializer.data, status=status.HTTP_201_CREATED)
```

<br>

## 댓글 수정 및 삭제 - DELETE & PUT

```python
# views.py

@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)

    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        comment.delete()
        data = {
            'delete': f'댓글 {comment_pk}번이 삭제되었습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
```

