# -*- coding : utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Entries


# Create your views here.
def index(request, page=1):
    per_page = 5
    start_pos = (page-1)*5
    end_pos = start_pos + per_page
    entries = Entries.objects.all().order_by(' -created ')[start_pos:end_pos]
    page_title = '블로그 글 목록 화면'
    return HttpResponse('Hello Universe. Your [%s] post is your first post.' % entries[0].Title.encode('utf-8'))