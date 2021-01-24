import sys
import os
import jqdatasdk 
from diskcache import FanoutCache
from functools import partial
cache = FanoutCache()


@cache.memoize(typed=True, expire=604800, tag='jqdata1week')
def cache1week(name,**kw):
    result = getattr(jqdatasdk, name)(**kw)
    return result

@cache.memoize(typed=True, expire=86400, tag='jqdata1day')
def cache1day(name,**kw):
    result = getattr(jqdatasdk, name)(**kw)
    return result

@cache.memoize(typed=True, expire=3600, tag='jqdata1hour')
def cache1hour(name,**kw):
    result = getattr(jqdatasdk, name)(**kw)
    return result

class JQDataCache1Week(object):
     def __getattr__(self, name):
         return partial(cache1week,name)
     
class JQDataCache1Day(object):
     def __getattr__(self, name):
         return partial(cache1day,name)

class JQDataCache1Hour(object):
     def __getattr__(self, name):
         return partial(cache1hour,name)
     
jqdata1week=JQDataCache1Week()
jqdata1day=JQDataCache1Day()
jqdata1hour=JQDataCache1Hour()

import shutil
def clean_all_cache():
    try:
        shutil.rmtree(cache.directory)
    except OSError:  # Windows wonkiness
        print("清理失败,请手动删除目录 {dir}".format(dir=cache.directory))
         


__all__ = ['jqdata1week','jqdata1day','jqdata1hour','clean_all_cache']



