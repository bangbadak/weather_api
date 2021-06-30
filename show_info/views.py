from django.shortcuts import render
from rest_framework import serializers
from .models import Weather
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import WeatherSerializer
import xml.etree.ElementTree as elemTree
from xml.etree.ElementTree import Element, dump, ElementTree
from xml.etree import ElementTree
import requests
# from snippets.models import Snippet
# from snippets.serializers import SnippetSerializer


# Create your views here.
@api_view(['GET'])
def index(request):
   
    # URL = "http://apis.data.go.kr/1360000/AsosDalyInfoService/getWthrDataList"
    # params = {'serviceKey': '%2F08lfq3dASI1JUoPSrf2ic37mWQvgiER75rZmxvz8TYXj5w9uMkVM%2BgxyVFYI7WYjzG20CtdJ0FYUDtJEYVxQg%3D%3D',
    # 'numOfRows': '10', 'pageNo': '1', 'dataType': 'JSON', 'dataCd': 'ASOS',
    # 'dateCd': 'DAY', 'startDt': '20200101', 'endDt': '20200102', 'stnIds': '108'}
    # response = requests.get(URL, params=params)
    response = requests.get("http://apis.data.go.kr/1360000/AsosDalyInfoService/getWthrDataList?serviceKey=%2F08lfq3dASI1JUoPSrf2ic37mWQvgiER75rZmxvz8TYXj5w9uMkVM%2BgxyVFYI7WYjzG20CtdJ0FYUDtJEYVxQg%3D%3D&numOfRows=10&pageNo=1&dataCd=ASOS&dateCd=DAY&startDt=20100101&endDt=20100101&stnIds=" + str(108))
    root = ElementTree.fromstring(response.content)
    # arr = []
    # cnt = 0
    # for i in range(0, 205):
    #     a = ElementTree.fromstring(requests.get("http://apis.data.go.kr/1360000/AsosDalyInfoService/getWthrDataList?serviceKey=%2F08lfq3dASI1JUoPSrf2ic37mWQvgiER75rZmxvz8TYXj5w9uMkVM%2BgxyVFYI7WYjzG20CtdJ0FYUDtJEYVxQg%3D%3D&numOfRows=10&pageNo=1&dataCd=ASOS&dateCd=DAY&startDt=20100101&endDt=20100101&stnIds=" + str(i + 90)).content)
    #     if  a[0][1].text == "NO_DATA":
    #         continue
    #     elif a[0][1].text == "NORMAL_SERVICE":
    #         arr[cnt] = a[1][1][0][1]
    #         cnt += 1
    #     else:
    #         continue



    # for i in range(0, 205):
    #     a = ElementTree.fromstring(requests.get("http://apis.data.go.kr/1360000/AsosDalyInfoService/getWthrDataList?serviceKey=%2F08lfq3dASI1JUoPSrf2ic37mWQvgiER75rZmxvz8TYXj5w9uMkVM%2BgxyVFYI7WYjzG20CtdJ0FYUDtJEYVxQg%3D%3D&numOfRows=10&pageNo=1&dataCd=ASOS&dateCd=DAY&startDt=20100101&endDt=20100101&stnIds=" + str(i + 90)).content)
    #     if a == None:
    #         cnt += 1
    #         continue
    #     arr[i-cnt] = a[1][1][0][1]
    for avg in root[1][1][0]:
        print(avg.tag, avg.text)

    return render(
        request, 
        'show_info/index.html',
        {
            'data': {
                root[1][1][0][1],
                "&nbsp",
                root[1][1][0][3],
            }
        },
    )

    # provinces = Province.objects.all()
    # cities = City.objects.all()
    # counties = County.objects.all()
    # return render(
    #     request,
    #     'show_info/index.html',
    #     {
    #         'provinces': provinces,
    #         'cities': cities,
    #         'counties': counties,
    #     },

    # )


    # request = Request("http://apis.data.go.kr/1360000/AsosDalyInfoService/getWthrDataList?serviceKey=%2F08lfq3dASI1JUoPSrf2ic37mWQvgiER75rZmxvz8TYXj5w9uMkVM%2BgxyVFYI7WYjzG20CtdJ0FYUDtJEYVxQg%3D%3D&numOfRows=1&pageNo=1&dataCd=ASOS&dateCd=DAY&startDt=20200101&endDt=20200102&stnIds=108"
    # + queryParams)
    # response_body = urlopen(request).read()

    # response = requests.get("http://apis.data.go.kr/1360000/AsosDalyInfoService/getWthrDataList?serviceKey=%2F08lfq3dASI1JUoPSrf2ic37mWQvgiER75rZmxvz8TYXj5w9uMkVM%2BgxyVFYI7WYjzG20CtdJ0FYUDtJEYVxQg%3D%3D&numOfRows=1&pageNo=1&dataCd=ASOS&dateCd=DAY&startDt=20200101&endDt=20200102&stnIds=108")
    # geodata = response.json()
    # return render(request, 'show_info/index.html', {
    #     'avgTA': geodata['avgTA'],
    # })




    # provinces = Province.objects.all()
    # cities = City.objects.all()
    # counties = County.objects.all()
    # return render(
    #     request,
    #     'show_info/index.html',
    #     {
    #         'provinces': provinces,
    #         'cities': cities,
    #         'counties': counties,
    #     },

    # )