from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import auth
from .models import Person, CountChicken, User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from operator import itemgetter

import json
# Create your views here.
def main(request):

  return render(request, 'main.html')

@login_required(login_url="/login/")
def fur(request):
  
  return render(request, 'fur.html')

@login_required(login_url="/login/")
def fried(request):
  current_user = request.user
  person = Person.objects.get(user=current_user)
  department = person.department

  CountChicken.objects.create(
    author = current_user,
    quantity = 1,
    department = department,
  )

  
  result = CountChicken.objects.all()
  count = len(result)
  return render(request, 'fried.html', {'count':count})

def mix(request):
  
  return render(request, 'mix.html')


@login_required(login_url="/login/")
def rank(request):
  hogi =  CountChicken.objects.filter(department='hogi')
  ingan = CountChicken.objects.filter(department='ingan')
  aeguk = CountChicken.objects.filter(department='aeguk')
  nokdu = CountChicken.objects.filter(department='nokdu')
  jajuLife = CountChicken.objects.filter(department='jajuLife')
  hoan = CountChicken.objects.filter(department='hoan')
  jajuSci = CountChicken.objects.filter(department='jajuSci')
  gangcheol = CountChicken.objects.filter(department='gangcheol')
  hohyeol = CountChicken.objects.filter(department='hohyeol')
  cheongnyeon = CountChicken.objects.filter(department='cheongnyeon')
  cheomdan = CountChicken.objects.filter(department='cheomdan')
  changjo = CountChicken.objects.filter(department='changjo')
  muhan = CountChicken.objects.filter(department='muhan')
  hoseong = CountChicken.objects.filter(department='hoseong')
  horim = CountChicken.objects.filter(department='horim')
  seodo = CountChicken.objects.filter(department='seodo')
  minjung = CountChicken.objects.filter(department='minjung')
  
  hogi_sum = len(hogi)
  ingan_sum = len(ingan)
  aeguk_sum = len(aeguk)
  nokdu_sum = len(nokdu)
  jajauLife_sum = len(jajuLife)
  hoan_sum = len(hoan)
  jajuSci_sum = len(jajuSci)
  gangcheol_sum = len(gangcheol)
  hohyeol_sum = len(hohyeol)
  cheongnyeon_sum = len(cheongnyeon)
  cheomdan_sum = len(cheomdan)
  changjo_sum = len(changjo)
  muhan_sum = len(muhan)
  hoseong_sum = len(hoseong)
  horim_sum = len(horim)
  seodo_sum = len(seodo)
  minjung_sum = len(minjung)

  #개인별 기록
  all_user = Person.objects.all()
  user_len = len(all_user)
  user_list = []
  for i in range(user_len):
    user_name = all_user[i].nickname
    user_id = all_user[i].id
    user_chicken = CountChicken.objects.filter(author=user_id)
    user_chicken_count = len(user_chicken)
    user_list.append({'username':user_name,
                      'count':user_chicken_count,})
    
  user_list = sorted(user_list, key=itemgetter('count'), reverse=True)

  #단과대별 기록
  dept_name = [
    '호기심리',
    '인간사랑',
    '애국경영',
    '녹두문대',
    '자주생명',
    '호안정대',
    '자주이과대',
    '강철공대',
    '호혈의대',
    '청년사대',
    '첨단정보',
    '창조조형',
    '무한국제',
    '호성미디어',
    '호림보과',
    '선도자전',
    '민중간호',
  ]

  dept_count = [
    hogi_sum,
    ingan_sum,
    aeguk_sum,
    nokdu_sum,
    jajauLife_sum,
    hoan_sum,
    jajuSci_sum,
    gangcheol_sum,
    hohyeol_sum,
    cheongnyeon_sum,
    cheomdan_sum,
    changjo_sum,
    muhan_sum,
    hoseong_sum,
    horim_sum,
    seodo_sum,
    minjung_sum,
  ]

  dept_list = []
  for i in range(17):

    dept_list.append({'department': dept_name[i],
                      'count': dept_count[i]})
  dept_list = sorted(dept_list, key=itemgetter('count'), reverse=True)
  results = CountChicken.objects.all()
  count = len(results)
  return render(request, 'rank.html', {'count':count,
                                       'results':results,
                                       'user_list':user_list,
                                       'dept_list':dept_list,
                                       })
                                      # 'hogi_sum':hogi_sum,
                                      #  'ingan_sum':ingan_sum,
                                      #  'aeguk_sum' : aeguk_sum,
                                      #  'nokdu_sum' : nokdu_sum,
                                      #  'jajuLife_sum' : jajauLife_sum,
                                      #  'hoan_sum' : hoan_sum,
                                      #  'jajuSci_sum' : jajuSci_sum,
                                      #  'gangcheol_sum' : gangcheol_sum,
                                      #  'hohyeol_sum' : hohyeol_sum,
                                      #  'cheongnyeon_sum' : cheongnyeon_sum,
                                      #  'cheomdan_sum' : cheomdan_sum,
                                      #  'changjo_sum' : changjo_sum,
                                      #  'muhan_sum' : muhan_sum,
                                      #  'hoseong_sum' : hoseong_sum,
                                      #  'horim_sum' : horim_sum,
                                      #  'seodo_sum' : seodo_sum,
                                      #  'minjung_sum' : minjung_sum,


def login(request):
  if request.method == 'POST':
    username = request.POST['userid']
    password = request.POST['userpw']
    # print(username, password)
    user = auth.authenticate(username=username, password=password)
    # print(user)
    if user is not None:
      auth.login(request, user)
      return redirect('main')
    error = '아이디 또는 비밀번호가 틀립니다.'
    return render(request, 'login.html', {'error':error})
  return render(request, 'login.html')

def logout(request):
  auth.logout(request)
  return redirect('main')

def signup(request):
    # departments = Department.objects.all()
    if request.method == 'POST':
      username = request.POST['userid']
      password = request.POST['userpw']
      department_name = request.POST['department']
      exist_user = User.objects.filter(username=username)

      if exist_user:
        error = "이미 존재하는 아이디입니다."
        return render(request, 'signup.html', {'error':error, 'departments': department_name})
      else:
        new_user = User.objects.create(username=username,)
        new_user.set_password(password)
        new_user.save()
        Person.objects.create(
          user = new_user,
          nickname = request.POST['usernickname'],
          department = department_name,
        )
        return redirect('login')
      
      # try:
      #   # 이미 존재하는 단과대인 경우
      #   existing_department = Department.objects.get(department_name=department_name)
      # except Department.DoesNotExist:
      #   # 존재하지 않는 단과대인 경우
      #   existing_department = None
      
      # if existing_department:
      #   # 이미 존재하는 단과대 사용
      #   new_user = User.objects.create(
      #     username = username,
      #   )
      #   new_user.set_password(password)
      #   new_user.save()
      #   Person.objects.create(
      #     user = new_user,
      #     nickname = request.POST['usernickname'],
      #     department = existing_department,
      #   )
      # else:
      #   # 새로운 단과대 생성
      #   new_user = User.objects.create(
      #     username = username,
      #   )
      #   new_user.set_password(password)
      #   new_user.save()
      #   new_department = Department.objects.create(
      #     department_name = department_name
      #   ) 
      #   Person.objects.create(
      #     user = new_user,
      #     nickname = request.POST['usernickname'],
      #     department = new_department,
      #   )

       
    return render(request, 'signup.html')

# def add_chicken(user, department):
#   # 기존 치킨 수량 가져오기
#   chicken = CountChicken.objects.get(user=user, department=department)
#   temp = chicken.quantity
#   temp += 1
#   chicken.quantity = temp
#   chicken.save()

# def create_chicken(user, department):
#   # 새로운 치킨 생성
#   chicken = CountChicken.objects.create(user=user, department=department, quantity=1)

# @csrf_exempt
# def count(request):
    
#     if request.method == 'POST':
#       request_body = json.loads(request.body)
#       # print('-------민기오빠세션', request_body)
    
   
#       # print("count 시작")
#     # 사용자와 부서 정보 가져오기
    
#       user_id = request_body["id"]
#       # print(user_id);
#       # print(request.user, '받아온 것')

#       person = Person.objects.get(pk = user_id)

#       department = person.department  

#       # 치킨 생성 또는 추가
#       try:
#           # print("치킨 있다")
#           # 이미 치킨이 있는 경우
#           add_chicken(person.user, department)
#       except CountChicken.DoesNotExist:
#           # print("치킨 없다")
#           # 치킨이 없는 경우
#           create_chicken(person.user, department)

#       return HttpResponse(json.dumps({'success': True}))