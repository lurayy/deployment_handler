import json 
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate, login, logout
from django.views import View
from django.utils.decorators import method_decorator
from django.middleware.csrf import get_token
from django.shortcuts import render
from user_handler.models import Profile, UserBase
from django.views.decorators.csrf import ensure_csrf_cookie
from django.core.files.base import ContentFile
import base64
from commerce.utils import for_logged_in, for_everyone, for_mods_only    
from rest_framework_jwt.settings import api_settings
from django.core.mail import send_mail
from django.conf import settings


class UserBaseView(View):

    @method_decorator(for_logged_in())
    def get(self,request):
        res = JsonResponse({'status':True, 'user_info' : self.get_user_details(request.user)})
        return res
    
    @method_decorator(for_everyone())
    def post(self,request):
        if not request.user:
            json_str = request.body.decode(encoding='UTF-8')
            data_json = json.loads(json_str)
            user = authenticate(username = str(data_json['username']), password = str(data_json['password']))
            if user == None:
                return JsonResponse({'status' : False, 'msg': 'Username or password incorrect.'}, status=401)
            jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
            jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
            payload = jwt_payload_handler(user)
            token = jwt_encode_handler(payload)
            return JsonResponse({'status':True, 'user_info' : self.get_user_details(user), 'token' : token })
        else:
            return JsonResponse({'status':True, 'user_info' : self.get_user_details(request.user)})
    
    def get_user_details(self, user):
        if user.is_authenticated:
            data = {
                'username' : user.username,
                'email' : user.email,
                'address' : user.profile.address,
                'phone_number' : user.profile.phone_number,
                'phone_number2' : user.profile.phone_number2,
                'profile_image' : str(user.profile.profile_image),
                'post' : user.profile.post,
                'is_verified' : user.is_verified,
                'first_name' : user.first_name,
                'last_name' : user.last_name
            }
        else:
            data = {
                'user' : 'None'
            }
        return data
    
    @method_decorator(for_logged_in())
    def delete(self, request):
        if not request.user.is_authenticated:
            return JsonResponse({'status': False, 'msg':'Not logged in as any user.'}, status='400')
        user = request.user 
        user.is_active = False
        user.save()
        return JsonResponse({'status': True} )

    @method_decorator(for_logged_in())
    def patch(self, request):
        res = {'status' : False}
        if request.user.is_authenticated:
            json_str = request.body.decode(encoding='UTF-8')
            data_json = json.loads(json_str)
            user = request.user
            if data_json['first_name']:
                user.first_name = str(data_json['first_name'])
            if data_json['last_name']:
                user.last_name = str(data_json['last_name'])
            if data_json['profile']['address']:
                user.profile.address = str(data_json['profile']['address'])
                
            if data_json['profile']['phone_number']:
                user.profile.phone_number = str(data_json['profile']['phone_number'])
            if data_json['profile']['phone_number2']:
                user.profile.phone_number2 = str(data_json['profile']['phone_number2'])
            if data_json['profile']['post']:
                user.profile.post = str(data_json['profile']['post'])
            if data_json['profile']['profile_image']:
                if data_json['profile']['profile_image'] == 'None':
                    user.profile.profile_image = None
                else:
                    data = data_json['profile']['profile_image']
                    format, imgstr = data.split(';base64,') 
                    ext = format.split('/')[-1] 
                    data = ContentFile(base64.b64decode(imgstr), name='profile_img.' + ext)
                    user.profile.profile_image = data
                    user.profile.save()
            user.profile.save()
            user.save()
            res = {
                'status' : True,
                'user' : self.get_user_details(user)
            }            
        return JsonResponse(res)

@require_http_methods(['POST'])
@for_everyone()
def register_new_user(request):
    json_str = request.body.decode(encoding='UTF-8')
    data_json = json.loads(json_str)
    new_user = UserBase.objects.create_user(str(data_json['username']), str(data_json['email']), str(data_json['password']))
    new_user.first_name = str(data_json['first_name'])
    new_user.last_name = str(data_json['last_name'])
    Profile.objects.create(
        user = new_user,
        address = data_json['profile']['address'],
        phone_number = data_json['profile']['phone_number'],
        phone_number2 = data_json['profile']['phone_number2'],
        post = data_json['profile']['post'],
    )
    if data_json['profile']['profile_image']:
        if data_json['profile']['profile_image'] == 'None':
            new_user.profile.profile_image = None
        else:
            data = data_json['profile']['profile_image']
            format, imgstr = data.split(';base64,') 
            ext = format.split('/')[-1] 
            data = ContentFile(base64.b64decode(imgstr), name='profile_img.' + ext)
            new_user.profile.profile_image = data
            new_user.profile.save()
    new_user.profile.save()
    new_user.save()
    return JsonResponse({'status' : True})


@ensure_csrf_cookie
def f404(request):
    return render(request,'404.html')
@ensure_csrf_cookie
def test(request):
    return render(request, 'test.html')