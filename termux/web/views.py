from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.contrib.auth.models import User
from django.http.response import JsonResponse
from json.encoder import JSONEncoder
from django.utils.crypto import get_random_string
from django.shortcuts import get_object_or_404
from .models import call_log, Token, sms_list, clipboard, contact_list
from .termux_api import InsertIntoDb
# Create your views here.

THIS_USER_TOKEN = None

@csrf_exempt
def register(request):
    global THIS_USER_TOKEN
    if 'password' in request.POST:
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        if not User.objects.filter(username = username).exists():
            if not User.objects.filter(email=email).exists():
                this_user = User.objects.create(username=username, password=make_password(password), email=email)
                this_token = get_random_string(length=48)
                THIS_USER_TOKEN = this_token
                Token.objects.create(user = this_user, token = this_token)
                InsertIntoDb(THIS_USER_TOKEN)
                return JsonResponse({'status' : 200, 'token' : this_token}, encoder=JSONEncoder)
            else:
                return JsonResponse({'status': "this email, already exists!"}, encoder=JSONEncoder)
        else:
            return JsonResponse({'status': "this user, already exists!"}, encoder=JSONEncoder)
    else:
        return render(request, 'register.html')

@csrf_exempt
def updatedb(request):
    InsertIntoDb(THIS_USER_TOKEN)
    return JsonResponse({'status': 200}, encoder=JSONEncoder)

@csrf_exempt
@require_POST
def getToken(request):

    try:
        password = request.POST['password']
        username = request.POST['username']
    except:
        return JsonResponse({'status': 404}, encoder=JSONEncoder)

    this_user  = get_object_or_404(User, username = username)
    if check_password(password, this_user.password):
        this_token = get_object_or_404(Token, user=this_user)
        token = this_token.token
        return JsonResponse({'status': 200, 'token': token}, encoder=JSONEncoder)
    else:
        return JsonResponse({'status': 404}, encoder=JSONEncoder)

@csrf_exempt
@require_POST
def setToken(request):

    try:
        username = request.POST['username']
        token = request.POST['token']
    except:
        return JsonResponse({'status': 404}, encoder=JSONEncoder)

    this_user  = get_object_or_404(User, username = username)
    Token.objects.create(user = this_user, token=token)
    return JsonResponse({'status': 200, 'token': token}, encoder=JSONEncoder)

@csrf_exempt
@require_POST
def s_call_log(request):
    try:
        token = request.POST['token']
        name = request.POST['name']
        phone_number = request.POST['phone_number']
        type = request.POST['type']
        date = request.POST['date']
        duration = request.POST['duration']
    except:
        return JsonResponse({'status': 404}, encoder=JSONEncoder)

    this_user = get_object_or_404(Token, token=token).user
    try:
        if not call_log.objects.filter(date = date).exists():
            call_log.objects.create(user = this_user, name = name, phone_number = phone_number, type = type, date = date, duration = duration)
            return JsonResponse({'status': 200, 'user_name': this_user.username}, encoder=JSONEncoder)
        else:
            return JsonResponse({'status': 404}, encoder=JSONEncoder)
    except:
        return JsonResponse({'status': 404}, encoder=JSONEncoder)


@csrf_exempt
@require_POST
def s_sms_list(request):
    try:
        token = request.POST['token']
        body = request.POST['body']
        phone_number = request.POST['phone_number']
        received = request.POST['received']
        type = request.POST['type']
        read = request.POST['read']
    except:
        return JsonResponse({'status': 404}, encoder=JSONEncoder)
    this_user = get_object_or_404(Token, token=token).user
    try:
        if not sms_list.objects.filter(received = received).exists():
            sms_list.objects.create(user = this_user, body = body, phone_number = phone_number, type = type, received = received, read = read)
            return JsonResponse({'status': 200, 'user_name': this_user.username}, encoder=JSONEncoder)
        else:
            return JsonResponse({'status': 404}, encoder=JSONEncoder)
    except:
        return JsonResponse({'status': 404}, encoder=JSONEncoder)


@csrf_exempt
@require_POST
def s_contact(request):
    try:
        token = request.POST['token']
        name = request.POST['name']
        phone_number = request.POST['phone_number']
    except:
        return JsonResponse({'status': 404}, encoder=JSONEncoder)
    this_user = get_object_or_404(Token, token=token).user
    try:
        if not contact_list.objects.filter(name = name).exists():
            contact_list.objects.create(user = this_user, phone_number = phone_number, name = name)
            return JsonResponse({'status': 200, 'user_name': this_user.username}, encoder=JSONEncoder)
        else:
            return JsonResponse({'status': 404}, encoder=JSONEncoder)
    except:
        return JsonResponse({'status': 404}, encoder=JSONEncoder)


@csrf_exempt
@require_POST
def s_clipboard(request):
    try:
        token = request.POST['token']
        text = request.POST['text']

    except:
        return JsonResponse({'status': 404}, encoder=JSONEncoder)
    this_user = get_object_or_404(Token, token=token).user
    try:
        if not clipboard.objects.filter(text = text).exists():
            clipboard.objects.create(user = this_user, text = text)
            return JsonResponse({'status': 200, 'user_name': this_user.username}, encoder=JSONEncoder)
        else:
            return JsonResponse({'status': 404}, encoder=JSONEncoder)
    except:
        return JsonResponse({'status': 404}, encoder=JSONEncoder)
