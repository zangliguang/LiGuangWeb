# LiGuangWeb
###BaseService
#####创建项目:

```
python manage.py startapp BaseService

＃setting中instqall_app中添加：
'BaseService.apps.BaseserviceConfig',
```
#####设置国际化:
######apps 中设置config

```
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

class BaseserviceConfig(AppConfig):
    name = 'BaseService'
    verbose_name = _("BaseService")
    verbose_name_plural = _("BaseService List")
```

######init 中设置config

```
default_app_config = 'BaseService.apps.BaseserviceConfig'
```

#####设置汉语,生成po，mo

```
＃生成po
python manage.py makemessages -l zh_hans
＃编辑po文件后，重新编译，生成mo文件
python manage.py compilemessages
```

#####在model中创建module,admin中注册，迁移刷新数据 
```
python manage.py makemigrations
python manage.py migrate
```