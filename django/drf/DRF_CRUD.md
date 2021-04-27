# Django REST Framework - 단일 모델

단일 모델의 data를 직렬화(Serialization)하여 JSON으로 변환하는 방법에 대한 학습 요청은 [Postman](https://www.postman.com/) 사용

<br>

- 가상 환경 구성

```bash
$ python -m venv venv
$ source venv/Scripts/activate
```

- 라이브러리 설치

```bash
$ pip install django django-seed djangorestframework django-extensions ipython
$ pip freeze > requirements.txt
```

- 프로젝트 생성

```bash
$ django-admin startproject my_api . 
$ python manage.py startapp articles
```

- settings.py 에 APP 등록

```python
INSTALLED_APPS = [
    'articles',
    'django_seed',
    'django_extensions',
    'rest_framework',
    ...,
]
```

- url 설정

```python
# my_api/urls.py

from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('articles.urls')),
]
```

- 모델링

```python
# articles/models.py

from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

DB(`models.py`) 수정 했으므로 migrations 작업 잊지말고 해주자

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

- **더미 데이터 생성 ([django_seed](https://github.com/Brobin/django-seed))**

```bash
$ python manage.py seed articles --number=20
```

데이터 베이스가 잘 생성되는지 확인!

<br>

## Model Serializer 활용

- Model의 필드를 어떻게 '직렬화'할 지 설정하는 것이 포인트
- Django에서 ModelForm의 필드를 설정하는 과정과 동일

```python
# articles/serializers.py

from rest_framework import serializers
from .models import Article


class ArticleListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('id', 'title',)
```

- 참고 (shell_plus)

```python
In [3]: serializer = ArticleListSerializer()  # 인스턴스 생성

In [4]: serializer
Out[4]: 
ArticleListSerializer():
    id = IntegerField(label='ID', read_only=True)
    title = CharField(max_length=100)

In [5]: article = Article.objects.get(pk=1)

In [6]: article
Out[6]: <Article: Article object (1)>

In [7]: serializer = ArticleListSerializer(article)  # 직렬화

In [8]: serializer
Out[8]:
ArticleListSerializer(<Article: Article object (1)>):
    id = IntegerField(label='ID', read_only=True)
    title = CharField(max_length=100)

In [9]: serializer.data
Out[9]: {'id': 1, 'title': 'Soon approach industry note country surface within.'}
```

<br>

## Article 전체 List 직렬화하기

```python
# articles/urls.py

urlpatterns = [
    path('articles/', views.article_list),
]
```

```python
# articles/views.py

from rest_framework.response import Response #3
from rest_framework.decorators import api_view #4
from django.shortcuts import render, get_list_or_404 #1
from .models import Article #1
from .serializers import ArticleListSerializer #2


@api_view(['GET']) #4
def article_list(request):
    articles = get_list_or_404(Article) #1 직렬화할 인스턴스 들고옴
    serializer = ArticleListSerializer(articles, many=True) #2(직렬화) articles는 여러개이므로 many=True 조건 추가
    return Response(serializer.data) #3
```

![image-20210427111712083](https://user-images.githubusercontent.com/77573938/116261705-de44cc00-a7b2-11eb-9332-12bae5f11e93.png)

![image-20210427111835104](https://user-images.githubusercontent.com/77573938/116261709-dedd6280-a7b2-11eb-82df-739ed910cd38.png)

<br>

✔ **Serializing multiple objects**

- 단일 객체 인스턴스 대신 쿼리셋 또는 객체 목록(여러 개)을 직렬화하려면 serializer를 인스턴스화 할 때 `many=True` 를 전달해야 함.

- `many=True` 옵션 사용 안 하고 그냥 직렬화하면 하나밖에 안됨

  ```python
  MySerializer(queryset, many=True)
  ```

- shell_plus

  ![image-20210427104935644](https://user-images.githubusercontent.com/77573938/116261645-d127dd00-a7b2-11eb-87c5-9379f095f02d.png)

<br>

## Article 1개 직렬화하기 - detail(GET)

List와 Detail을 구분하기 위해 추가적인 Serializer를 정의

```python
# articles/serializers.py

class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = '__all__'
```

<br>

```python
# articles/urls.py

urlpatterns = [
	 ...,
   path('articles/<int:article_pk>/', views.article_detail),
]
```

<br>

```python
# articles/views.py

from django.shortcuts import get_object_or_404
from .serializers import ArticleListSerializer, ArticleSerializer


@api_view(['GET'])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = ArticleSerializer(article)
    return Response(serializer.data)
```

- `https://127.0.0.1:8000/api/v1/articles/1/`  잘 동작하는지 확인!

![image-20210427112339318](https://user-images.githubusercontent.com/77573938/116261714-df75f900-a7b2-11eb-98eb-1afd8bce252c.png)

![image-20210427112408757](https://user-images.githubusercontent.com/77573938/116261717-df75f900-a7b2-11eb-9b23-9a06d5c116c3.png)

<br>

## API 서버에 생성 요청 처리하기 - CREATE(POST)

```python
# articles/views.py

from rest_framework import status


@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        articles = get_list_or_404(Article)
        serializer = ArticleListSerializer(articles, many=True) 
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

<br>

**Raising an exception on invalid data**

- `.is_valid()`는 유효성 검사 오류가 있는 경우 `serializers.ValidationError` 예외를 발생시키는 선택적 `raise_exception` 인자를 사용할 수 있음
- DRF에서 제공하는 기본 예외 처리기에 의해 자동으로 처리되며 기본적으로 HTTP 400 응답을 반환

```python
# 위의 POST 코드와 동일
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        # Return a 400 response if the data was invalid.
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
```

생성 잘 되는지 Postman으로 확인!

<br>

## API 서버에서 삭제 요청 처리하기 - DELETE

삭제 요청 처리 후 삭제가 잘 됐는지 응답으로 보내줌. 204 No Content 상태 코드 및 메시지 응답

```python
# articles/views.py

@api_view(['GET', 'DELETE'])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk) # 순서 변경
    
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        article.delete()
        data = {
            'delete': f'데이터 {article_pk}번이 삭제되었습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)
```

삭제 잘 되는지 Postman으로 확인!

<br>

## API 서버에서 수정 요청 처리하기 - Update(PUT)

```python
# articles/views.py

@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
	...

    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        # serializer = ArticleSerializer(instance=article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
```

