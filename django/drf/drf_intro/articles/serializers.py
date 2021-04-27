from rest_framework import serializers
from .models import Article, Comment

# 모든 게시글 정보를 반환하기 위한 Serializer
class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title',)


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article',)  # 데이터를 주고 받는게 아닌 읽기전용이라고 설정해줘야 댓글이 작성됨


# 상세 게시글 정보를 반환 및 생성하기 위한 Serializer
class ArticleSerializer(serializers.ModelSerializer):
    # comment_set은 정해진거라 바꾸면 작동안됨. 바꾸고 싶으면 modles.py에서 related_name 설정하면 됨
    # comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)  # 각 게시글마다 달린 댓글 번호가 나옴
    comment_set = CommentSerializer(many=True, read_only=True)  # 댓글 내용도 같이 나옴
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)  # 각 게시글마다 달린 댓글 수
    # comment_first = serializers.CharField(source='comment_set.first', read_only=True)  # object로 나옴
    comment_first = CommentSerializer(source='comment_set.first', read_only=True)  # 내용으로 나옴
    comment_filter = serializers.SerializerMethodField('less_7')  # 7번이하 게시글의 댓글을 가져옴

    def less_7(self, article):
        qs = Comment.objects.filter(pk__lte=7, article=article)
        serializer = CommentSerializer(instance=qs, many=True)
        return serializers.data

    class Meta:
        model = Article
        fields = '__all__'