from django.http import JsonResponse
from user.models import UserProfile

def test_cors(request):
    # 对数据库中score字段进行+1操作
    u = UserProfile.objects.get(username="guoxiaonao")
    u.score += 1
    u.save()


    res = {'data':{},'code':200}
    return JsonResponse(res)