from django import forms
from .models import Article


# Article 관련 데이터를 처리할 수 있는 Django Form
class ArticleForm(forms.Form):
    # REGION_A = 'seoul'
    # REGION_B = 'gwangju'
    # REGION_C = 'gumi'
    # REGION_D = 'daejeon'
    # REGIONS_CHOICES = [
    #     (REGION_A, '서울'),
    #     (REGION_B, '광주'),
    #     (REGION_C, '구미'),
    #     (REGION_D, '대전'),
    # ]

    title = forms.CharField(max_length=10)
    content = forms.CharField(widget=forms.Textarea)
    # region = forms.ChoiceField(choices=REGIONS_CHOICES, widget=forms.RadioSelect)

class ArticleForm(forms.ModelForm): 
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class': 'my-title',
                'placeholder': '제목을 입력해주세요.',
            }
        ),
        error_messages={
            'required': '오류나면 발생하는 메세지 !',
        }
    )
    # Content 필드 바꿔보기 -> Textarea Widget 활용
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class': 'my-content',
                'placeholder': '내용을 입력해주세요.',
            }
        )
    )

    class Meta:
        model = Article
        fields = '__all__'
        # exclude = ('title',)
