# jqdata_cache 聚宽API缓存
## 安装
```python
pip install git+https://github.com/chenjiajia/jqdata_cache.git --upgrade
```
## 使用

直接在聚宽api前面增加jqdata1day. 前缀，表示缓存1天
```python
from jqdata_cache import jqdata1day,jqdata1hour,jqdata1week,clean_all_cache

jqdata1hour.get_all_securities() #缓存1小时

jqdata1day.get_all_securities() #缓存1天

jqdata1week.get_all_securities() #缓存1周

clean_all_cache() #删除全部缓存，删除失败，手工删除缓存目录即可
```