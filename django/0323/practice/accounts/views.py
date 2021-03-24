from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth import login as auth_login, logout as auth_logout, update_session_auth_hash
from .forms import CustomUserChangeForm

# Create your views here.
def login(request):
    # 로그인이 이미 되어있으면 접근 못하도록 분기처리
    if request.user.is_authenticated:
        return redirect('articles:index')
    
    # POST -> 사용자가 맞으면 세션 생성
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()  # 인증이 끝난 유저 인스턴스 반환
            auth_login(request, user)  # 세션 생성

            # 돌아가야할 주소가 파라미터로 들어온 경우(쿼리스트링), next뒤의 경로를 추출해서 보내줌
            next_url = request.GET.get('next')
            return redirect(next_url or 'articles:index')

    # GET -> 비어있는 폼 주기
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/form.html', context)


@require_POST
def logout(request):
    auth_logout(request)
    return redirect('articles:index')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # UserCreationForm의 반환값은 새롭게 생성된 User 인스턴스
            auth_login(request, user)  # 세션 생성
            return redirect('articles:index')
    else:
        form = UserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/form.html', context)


@require_POST
def delete(request):
    # 로그인한 유저만 삭제가 가능하도록
    if request.user.is_authenticated:
        request.user.delete()
        auth_logout(request)  # 세션 삭제
    return redirect('articles:index')
    


def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/form.html', context)


def update_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user) # 세션에 있는 로그인 정보 해쉬를 업데이트하는 메서드 사용
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/form.html', context)