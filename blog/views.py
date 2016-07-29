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
    all_pos = Entries.objects.count()
    if all_pos % 5 == 0:
        all_page = int(all_pos/5)
    else:
        all_page = str(int(all_pos/5) + 1)
    print(all_page, all_pos)

    tpl = loader.get_template('list.html')
    ctx = Context({
        'page_title': page_title,
        'entries': entries,
        'current_page': page,
        'all_page': all_page
    })
    return HttpResponse(tpl.render(ctx))


def read(request, entry_id=None):
    page_title = '글 읽기 화면'
    current_entry = Entries.objects.get(id=int(entry_id))
    pre_entry = current_entry.get_previous_by_created()
    nxt_entry = current_entry.get_next_by_created()
    return HttpResponse(page_title)
