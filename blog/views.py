# -*- coding : utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
from blog.models import Entries


# Create your views here.
def index(request, page=1):
    per_page = 5
    start_pos = (int(page)-1)*5
    end_pos = start_pos + per_page
    entries = Entries.objects.all().order_by('-created')[start_pos:end_pos]
    page_title = '블로그 글 목록 화면'
    tpl = loader.get_template('list.html')
    ctx = Context({
        'page_title': page_title,
        'entries': entries,
        'current_page': page
    })
    return HttpResponse(tpl.render(ctx))


def read(request, entry_id=None):
    page_title = '글 읽기 화면'
    current_entry = Entries.objects.get(id=int(entry_id))
    prev_entry = current_entry.get_previous_by_created()
    next_entry = current_entry.get_next_by_created()


    return HttpResponse('Hello Universe. [%d]nd Post is [%s]!! :)' %
                        (current_entry.id, current_entry.Title.encode('utf-8')))
