## 중첩 관계 (Nested Relationships)

Serializer는 기존 필드를 override 하거나 추가적인 필드를 구성할 수 있음

<br>

### 1️⃣ 게시글마다 달린 댓글 pk 확인하기

**PrimaryKeyRelatedField**

- pk를 사용하여 관계된 대상을 나타냄
- PrimaryKeyRelatedFields는 `read_only=True` 가 필수다.
- 필드가 to many relationship을 나타내는 데 사용되는 경우 `many=True` 속성이 필요
- 역참조 시 생성되는 `comment_set`을 override. 장고에서 기본으로 comment_set을 사용하기 때문에 변수명을 다른걸로 바꾸면 안된다!
- `comment_set` 필드 값을 form-data로 받지 않으므로 (form에서 입력하는게 아니니까) `read_only=True` 필요

```python
class ArticleSerializer(serializers.ModelSerializer):
    # 각 게시글마다 달린 댓글 번호가 나옴
    comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta():
        model = Article
        fields = '__all__'
```

- model에서 `comment_set` 이름은  `related_name='원하는 이름'` 을 통해 이름 변경 가능

```python
# models.py

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
```

<br>

### 2️⃣ 게시글의 모든 댓글 정보 확인하기

- 모델 관계 상으로 참조 된 대상은 참조하는 대상의 표현에 포함되거나 중첩(nested)될 수 있다.
- 이러한 **중첩된 관계는 Serializers를 필드로 사용하여 표현 할 수 있다.**
- 만약 여러개를 들고 오고 싶다면 `many=True` 를 해줘야 한다.

```python
class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article',)

        
class ArticleSerializer(serializers.ModelSerializer):
    # 댓글 내용도 같이 나옴
    comment_set = CommentSerializer(many=True, read_only=True)  #  Serializers를 필드로 사용하여 중첩된 관계 표현

    class Meta:
        model = Article
        fields = '__all__'
```

⭐⭐ **두 모델 CommentSerializer 와 ArticleSerializer의 순서가 중요하다 !**

파이썬 인터프리터는 위에서부터 아래로 실행되기 때문에 `comment_set = CommentSerializer(many=True, read_only=True)` 가 실행되기 위해서는 CommentSerializer 아래에 있어야 한다. 순서 바꾸면 에러 남.

<br><br>

## 추가 필드 작성

💡 **`source` (serializers field's argument)**

- 필드를 채우는 데 사용할 속성의 이름
- 점 표기법(dotted notation)을 사용하여 속성을 탐색 할 수 있다

<br>

### 3️⃣ 댓글 갯수 확인하기

- `comment_count`의 경우 자동으로 구성되는 필드가 아니기 때문에 직접 필드를 추가해서 구성해야 함
- `comment_set`이라는 필드에 `.` 을 통해 전체 댓글의 개수 확인(`.count()`는 built-in queryset API 중 하나)
- 결과: `"comment_count": 4,`

```python
class ArticleSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
```

<br>

### 4️⃣ 첫 번째 댓글 가져오기

- object로 나온다.

```python
class ArticleSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True, read_only=True)
	comment_first = serializers.CharField(source='comment_set.first', read_only=True)
```

<br>

### 5️⃣ 첫 번째 댓글의 모든 정보 가져오기

- 내용으로 나온다.

```python
class ArticleSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True, read_only=True)
	comment_first = CommentSerializer(source='comment_set.first', read_only=True)
```

<br>

### 6️⃣ 댓글 중에 id 값이 7 이하인 댓글 찾기

이런식으로 원하는 정보를 가공해서 인자로 넘겨준 다음에 API 요청이 오면 응답으로 뿌려주면 된다.

```python
class ArticleSerializer(serializers.ModelSerializer):
    comment_filter = serializers.SerializerMethodField('less_7')

    def less_7(self, article):  # 이 article은 views.py에서 `serializer = ArticleSerializer(article)` 이때 넘겨준 것이다
        qs = Comment.objects.filter(pk__lte=7, article=article)
        serializer = CommentSerializer(instance=qs, many=True)
        return serializer.data
```

<br><br>

## 👉 serializers.py


```python
from rest_framework import serializers
from .models import Article, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article',)  # 데이터를 주고 받는게 아닌 읽기전용이라고 설정해줘야 댓글이 작성됨


# 상세 게시글 정보를 반환 및 생성하기 위한 Serializer
class ArticleSerializer(serializers.ModelSerializer):
    # comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)  #1️⃣
    comment_set = CommentSerializer(many=True, read_only=True)  #2️⃣
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)  #3️⃣
    # comment_first = serializers.CharField(source='comment_set.first', read_only=True)  #4️⃣
    comment_first = CommentSerializer(source='comment_set.first', read_only=True)  #5️⃣
    comment_filter = serializers.SerializerMethodField('less_7')  #6️⃣

    def less_7(self, article):
        qs = Comment.objects.filter(pk__lte=7, article=article)
        serializer = CommentSerializer(instance=qs, many=True)
        return serializers.data

    class Meta:
        model = Article
        fields = '__all__'
```

