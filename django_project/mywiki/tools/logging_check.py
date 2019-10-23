import jwt
from django.http import JsonResponse
from user.models import UserProfile

TOKEN_KEY = '123456'

def logging_check(*methods):
    def _logging_check(func):
        def wrapper(request, *args , **kwargs):
            #逻辑
            token = request.META.get('HTTP_AUTHORIZATION')
            if not methods:
                #没传参数 不检查
                return func(request, *args, **kwargs)
            else:
                #@logging_check('PUT', 'POST')
                if request.method not in methods:
                    return func(request, *args, **kwargs)
                #检查token
                #1,检查有没有token
                if not token:
                    result = {'code': 10206, 'error': 'Please login'}
                    return JsonResponse(result)


                try:
                    res = jwt.decode(token, TOKEN_KEY)
                except Exception as e:
                    print(e)
                    result = {'code': 10207, 'error': 'Please login !'}
                    return JsonResponse(result)

                username = res['username']
                try:
                    user = UserProfile.objects.get(username=username)
                except Exception as e:
                    print('--get error--')
                    print(e)
                    result = {'code': 10208, 'error': 'Please login !!'}
                    return JsonResponse(result)
                request.user = user

            return func(request, *args, **kwargs)
        return wrapper
    return _logging_check


def get_user_by_request(request):

    token = request.META.get('HTTP_AUTHORIZATION')
    if not token:
        return None

    try:
        res = jwt.decode(token, TOKEN_KEY)
    except Exception as e:
        print('---get_user jwt decode error---')
        print(e)
        return None

    username = res['username']
    try:
        user = UserProfile.objects.get(username=username)
    except Exception as e:
        print('get user error')
        print(e)
        return None
    return user











