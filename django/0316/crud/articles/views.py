from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    articles = Article.objects.order_by('-pk')
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def create(request):
    '''
    사용자가 /articles/create/로 요청을 보낸 경우,
    1) GET : 비어있는 ModelForm을 던진다.
    2) POST : 데이터를 받아서 DB에 저장한다.


    [그냥 Form 썼을 때]
    - Model 정보가 없기 때문에, Model 인스턴스를 만들어서 Save 하는 절차가 필요함.
    form = ArticleForm(request.POST)
    title = form.cleaned_data['title']
    content = form.cleaned_data['content']

    article = Article(title=title, content=content)
    article.save()

    [ModelFrom 썼을 때]
    - ModelForm에는 Model 정보가 있고 save 메서드를 지원하고 있기 때문에,
    - Model 인스턴스를 따로 만들 필요가 없음.
    form = ArticleForm(request.POST)
    if form.is_valid():
        form.save()
    '''

    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    
    # form에 들어올 수 있는 데이터 형태
    # 1) GET 요청 : 사용자가 데이터를 입력할 수 있는 비어있는 form
    # 2) POST 요청
    #    - 사용자가 입력한 데이터가 유효성 검사에서 실패한 경우
    #    - 에러 메시지를 포함한 form
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


def delete(request, pk):
    # 삭제할 게시글 조회
    article = Article.objects.get(pk=pk)
    # 삭제 요청이 POST면 삭제, POST가 아니라면 DETAIL 페이지로 redirect
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
    return redirect('articles:detail', article.pk)


def update(request, pk):
    # 수정할 Article 인스턴스 가져오기
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        # 수정할 데이터와 수정 대상 인스턴스를 건네준다.
        form = ArticleForm(request.POST, instance=article)
        # 유효성 검사를 실시한다.
        if form.is_valid():
            # DB에 반영한다. (인스턴스를 받았기 때문에, UPDATE 기능이 수행된다)
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)

    context = {
        'form': form,
        'article': article,
    }
    return render(request, 'articles/update.html', context)
