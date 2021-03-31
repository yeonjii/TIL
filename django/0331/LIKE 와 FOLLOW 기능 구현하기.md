# LIKE 와 FOLLOW 기능 구현하기

> M:N 관계

<br>

## Like 좋아요 기능

**# User-Article  M:N관계 **

M:N 은 User와 Article 둘 중 어느곳이나 작성 가능. (Article이 이미 User를 참조하고 있어서 그냥 참조하고 있는 곳에 추가로 참조해줌)

<br>

📁articles

- models.py

|           1:N 관계시 manager 이름            |          M:N 관계시 manager 이름           |
| :------------------------------------------: | :----------------------------------------: |
|                article.user.                 |            article.like_users.             |
| user.article_set : 유저가 작성한 모든 게시글 | user.article_set : 좋아요 누른 모든 게시글 |

역참조시, `user.article_set` 의 역할이 다른데 related manager가 같아서 migration 작업 시 에러가 발생한다. -> `related_name='like_articles'` 설정해줌

```python
from django.db import models
from django.conf import settings

class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
```

migration 하고 나면 `articles_article_like_users (app_model_field)` 테이블이 자동으로 생성된다.

![image-1](https://user-images.githubusercontent.com/77573938/113204481-441f6000-92a8-11eb-9071-3452c0821347.png)

<br>

- urls.py

```python
from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('<int:article_pk>/likes/', views.likes, name='likes'),
]
```

<br>

- views.py

exists : 적어도 하나이상 존재하는지 판단할 때 DB query를 최적화할 수 있는 메소드. 굳이 전체 조회가 필요하지 않을 때 & 쿼리셋이 엄청 클 때 사용

in : 전체 조회

```python
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import Article

@require_POST
def likes(request, article_pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=article_pk)
        
        if article.like_users.filter(pk=request.user.pk).exists():
        # if request.user in article.like_users.all():
            article.like_users.remove(request.user)  # 좋아요 취소
        else:
            article.like_users.add(request.user)  # 좋아요 누름
        return redirect('articles:index')
    return redirect('accounts:login')
```

<br><br>

## 유저 프로필 페이지 만들기

📁accounts

- urls.py

```python
from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('<username>/', views.profile, name='profile'),
]
```

<br>

- views.py

user 라는 변수명을 사용하지 않는 것을 권장한다. 이미 템플릿에서 request, user 같은 애들은 기본적으로 쓸 수 있기 때문에 혼동을 막기 위해

```python
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model

def profile(request, username):
    # user 라는 변수명 사용 안하는 걸 권장 -> person 사용
    person = get_object_or_404(get_user_model(), username=username)
    context = {
        'person': person,
    }
    return render(request, 'accounts/profile.html', context)
```

<br>

- profile.html

```django
{% extends 'base.html' %}

{% block content %}
<h1>{{ person.username }}님의 프로필</h1>
<hr>

<h2>{{ person.username }}'s 게시글</h2>
{% for article in person.article_set.all %}
  <div>{{ article.title }}</div>
{% endfor %}
<hr>

<h2>{{ person.username }}'s 댓글</h2>
{% for comment in person.comment_set.all %}
  <div>{{ comment.content }}</div>
{% endfor %}
<hr>

<h2>{{ person.username }}'s likes</h2>
{% for article in person.like_articles.all %}
  <div>{{ article.title }}</div>
{% endfor %}
<hr>

<a href="{% url 'articles:index' %}">[back]</a>
{% endblock %}
```

<br><br>

## Follow 팔로우 기능

**# User-User  M:N관계**

⭐ User 모델을 수정해야 함 -> 그래서 항상 **장고 프로젝트 시작하기 전에 유저모델 먼저 만들고 시작**하라는 거임!!!

<br>

📁accounts

- models.py

자동으로 맞팔 안되도록 `symmetrical` 기능 비활성화. 그런데 이렇게 비활성화하면 역참조가 발생한다. -> related_name 필요

(대칭일때는 한명만 참조하면 같이 참조되기때문에 역참조가 만들어지지 않음)

모델에 변경사항 생겼으니까 잊지말고 migrations 작업을 해주자 !!

```python
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
```

ManyToManyField이기 때문에 중개테이블 생김

![image-2](https://user-images.githubusercontent.com/77573938/113204535-56999980-92a8-11eb-9638-5bd32aa0df26.png)

<br>

- urls.py

```python
from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('<int:user_pk>/follow/', views.follow, name='follow'),
]
```

<br>

- views.py

중개테이블에 데이터가 들어가기 때문에 GET 방식은 부적합 -> @require_POST

```python
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model

@require_POST
def follow(request, user_pk):
    if request.user.is_authenticated:
        you = get_object_or_404(get_user_model(), pk=user_pk)  # 내가 팔로우 할 대상
        me = request.user

        # 나 자신은 팔로우 할 수 없는 조건 설정
        if you != me:
            if you.followers.filter(pk=me.pk).exists():  # .get 쓰면 does not exist 에러 발생해서 filter 사용
            # if request.user in person.followers.all():
                you.followers.remove(me)  # 팔로우 끊음
            else:
                you.followers.add(me)  # 팔로우 신청
        return redirect('accounts:profile', you.username)
    return redirect('accounts:login')
```

<br>

- profile.html

하나의 템플릿 안에서 똑같은 변수가 반복되서 사용되는 경우 `{% with %}{% endwith %}` 태그 안에서 변수화해서 사용할 수 있음

```django
{% with followings=person.followings.all followers=person.followers.all %}
  <div>
    <div>
      팔로잉 : {{ followings|length }} | 팔로워 : {{ followers|length }}
    </div>
    {% if request.user != person %}
      <div>
        <form action="{% url 'accounts:follow' person.pk %}" method="POST">
          {% csrf_token %}
          {% if request.user in followers %}
            <button>언팔로우</button>
          {% else %}
            <button>팔로우</button>
          {% endif %}
        </form>
      </div>
    {% endif %}
  </div>
{% endwith %}
```

<br><br>

---

## [참고] 쿼리셋 효과적으로 사용하기

> https://docs.djangoproject.com/en/3.1/topics/db/queries/#querysets-are-lazy
>
> https://docs.djangoproject.com/en/3.1/ref/models/querysets/#when-querysets-are-evaluated
>
> https://docs.djangoproject.com/en/3.1/topics/db/queries/#caching-and-querysets

<br>

실제 쿼리셋을 만드는 작업에는 DB 작업이 포함되지 않음 (i.e. ORM -> DB로 아직 요청 안보냄)

- 요청은 언제 보냄? -> 평가할 때

- 평가는 언제 됨? -> 출력 or 조건문 or 반복문(Iteration) or Boolean

- **평가 : (1) 쿼리를 DB로 날린다.  (2) 쿼리셋 캐시를 만든다. (캐싱됨)**

```python
q = Entry.objects.filter(title__startswith="What")
q = q.filter(created_at__lte=datetime.date.today())
q = q.exclude(context__icontains="food")
print(q) # 여기서 평가 됨
```

그래서 chaining을 길게 해도 괜찮음

캐시는 처음 평가 될 때 만들어지고, 이후에는 다시 만드는게 아니라 재사용함

<br>

쿼리셋은 반복 가능하며 처음 반복할 때 데이터베이스 쿼리를 실행(평가)

```python
# Iteration
for e in Entry.objects.all():
    pass

# bool()
if Entry.objects.filter(title__'test'):
    pass
```

- 나쁜 예

동일한 쿼리를 2번 보냄

```python
print([e.headline for e in Entry.objects.all()]) # 평가
print([e.pub_date for e in Entry.objects.all()]) # 평가
```

- 좋은 예

```python
queryset = Entry.objects.all()  # 미리 쿼리셋을 변수화 하고 밑에서 재사용
print([p.headline for p in queryset]) # Evaluate the query set. (평가)
print([p.pub_date for p in queryset]) # Re-use the cache from the evaluation. (캐시에서 재사용)
```

<br>

- 캐시 되지않는 경우

쿼리셋의 특정요소(직접적인 인덱스)에 접근 하는 경우

```python
queryset = Entry.objects.all()
print(queryset[5]) # Queries the database
print(queryset[5]) # Queries the database again
```

- 위 상황을 방지하고 싶다면

인덱스로 접근하기 전에 애초에 전체를 평가함

```python
queryset = Entry.objects.all()
[entry for entry in queryset] # Queries the database (전체 쿼리셋을 평가 시켜버림)
print(queryset[5]) # Uses cache
print(queryset[5]) # Uses cache
```

<br><br>

### Example

우리의 LIKE 코드를 예시로 사용해보자



- 문제점 : 쿼리셋의 전체 결과가 필요하지 않은 상황임에도 ORM은 전체 결과를 가져옴.

Like에서 중요한건 전체 평가가 아니라 특정한게 있는지 없는지 확인이 중요 !

```python
like_set = article.like_users.filter(pk=request.user.pk)  # 쿼리셋 만듦 -> DB아직 모름
if like_set: # 평가
    article.like_users.remove(request.user)  # 문제점
```



- 개선 1 : `exists()` 사용

```python
# exists(): 쿼리셋 캐시를 만들지 않으면서 특정 레코드가 있는지 검사
if like_set.exists():
    # DB에서 가져온 레코드가 없다면 메모리를 절약할 수 있다
    article.like_users.remove(request.user)
```



- 만약 IF 문 안에서 반복문이 있다면?

if에서 평가 후 캐싱. 순회할때는 위에서 캐싱된 쿼리셋을 사용

```python
if like_set:
    for user in like_set:
        print(user.username)
```




- 만약 쿼리셋 자체가 너무너무 크다면?? ->  `interator()` 사용

데이터를 작은 덩어리로 쪼개서 가져오고, 이미 사용한 레코드는 메모리에서 지움

전체 레코드의 일부씩만 DB에서 가져오므로 메모리를 절약

```python
if like_set:
    for user in like_set.iterator():
```

그런데 쿼리셋이 너무너무 크다면 if 평가에서도 버거움 -> `exists()` 사용

```python
if like_set.exists():
    for user in like_set.iterator():
        pass
```

<br>

**But..... 안일한 최적화에 빠지면 안된다 !**

exist나 interator 메소드를 사용하면 메모리 사용은 최적화 할 수 있으나 쿼리셋 캐시는 생성되지 않기 때문에 DB query가 중복 될 수 있음.

위의 코드가 최종 단계가 아님!

