from django.shortcuts import render
from .models import Province, City, County
from pip._vendor import requests
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import os, urllib.parse, urllib.request, requests
# from snippets.models import Snippet
# from snippets.serializers import SnippetSerializer


# Create your views here.
def index(request):
    
    url = 'http://apis.data.go.kr/1360000/AsosDalyInfoService/getWthrDataList'
    params = {'serviceKey': '%2F08lfq3dASI1JUoPSrf2ic37mWQvgiER75rZmxvz8TYXj5w9uMkVM%2BgxyVFYI7WYjzG20CtdJ0FYUDtJEYVxQg%3D%3D',
    'numOfRows': '10', 'pageNo': '1', 'dataType': 'JSON', 'dataCd': 'ASOS',
    'dateCd': 'DAY', 'startDt': '20200101', 'endDt': '20200102', 'stnIds': '108'}
    res = requests.get(url, params)
    print(res.request)
    provinces = Province.objects.all()
    cities = City.objects.all()
    counties = County.objects.all()
    return render(
        request,
        'show_info/index.html',
        {
            'provinces': provinces,
            'cities': cities,
            'counties': counties,
        },

    )
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