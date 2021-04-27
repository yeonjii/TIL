# DRF - yasg

> django restframework를 이용하여 API를 만들었을 때, 이것을 잘 설명할 수 있는 문서화를 자동으로 만드는 방법
>
> - 공식문서 : 
>
>   https://github.com/axnsan12/drf-yasg
>
>   https://drf-yasg.readthedocs.io/en/stable/readme.html

<br>

### 1. 설치

```sh
$ pip install -U drf-yasg
```

```python
# settings.py
INSTALLED_APPS = [
		...
    'drf_yasg',
		...
]
```

<br>

### 2. 프로젝트의 urls.py 변경

공식 문서에서 urlpatterns에 `url`로 되있는것을 `re_path`로 변경하면 된다. (import도 해주기)

```python
# my_api/urls.py

from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="<https://www.google.com/policies/terms/>",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
	...
    re_path('swagger(?P<format>\\.json|\\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path('swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path('redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
```

<br>

### 3. 서버 키고 접속

http://127.0.0.1:8000/swagger/

- `swagger` 에서는 API를 호출해 볼 수 있다. (문서화에는`redoc`이 확실히 깔끔함)
- 보통 테스트를 위해 사용 (postman 대신 사용)

![image-20210427152314608](https://user-images.githubusercontent.com/77573938/116265629-3e893d00-a7b6-11eb-84f4-9aa0695f7eb6.jpg)



http://127.0.0.1:8000/redoc/

- `redoc`은 문서화에 좀 더 충실한 페이지이므로 문서화 목적으로 보려면 알맞다.

![image-20210427152356196](https://user-images.githubusercontent.com/77573938/116265635-40530080-a7b6-11eb-9063-509a87788520.png)

<br>

### 4. 데이터 입력 칸 만들기

- 테스트를 하기 위해서는 `@swagger_auto_schema()` 데코레이터를 사용한다.

```python
# articles/views.py

from drf_yasg.utils import swagger_auto_schema

@swagger_auto_schema(methods=['POST'], request_body=CommentSerializer)
@api_view(['POST'])
def comment_create(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
```

<br>

### + get 요청시 메세지 보이도록 변경하기

```python
# articles/views.py

from drf_yasg import openapi

user_response = openapi.Response('article List를 요청했을 때', ArticleSerializer)

@swagger_auto_schema(method='GET', responses={200: user_response})
@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        articles = get_list_or_404(Article)
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)
```

