__author__ = 'hulk'


import re
import time
import json
import logging
import hashlib
import base64
import asyncio
from coroweb import post, get
from models import User, Comment, Blog, next_id


@get('/')
def index(request):
    # summary = 'Summary'
    blogs = [
        Blog(id='1', name='first blog',
             summary='first summary dsfklasjdf lajsdlfkj alsdjf klasd ', create_at=time.time()-120),
        Blog(id='2', name='second blog',
             summary='second summary asdf asdfjkljsdfjowqiejr89uwfasdj ', create_at=time.time()-3600),
        Blog(id='3', name='third blog',
             summary='third summary saf asdfnkjdak ajksdhfkj alh8eyhr98rashdf ', create_at=time.time()-4500)
    ]
    return {
        '__template__': 'blogs.html',
        'blogs': blogs
    }