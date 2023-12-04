手順

1. projectのファイル編集
   1. settings.py
      1. TIME_ZONE
         1. "Asia/Tokyo" に変更
      2. LANGUAGE_CODE
         1. "ja"に変更
      3. INSTALLED_APPS
         1. startappのapps.pyのclass名を追加。"hello.apps.HelloConfig"
   2. urls.py
      1. from django.urls にincludeをimportする
      2. project管理しているurlsに各appのurlsを追加
         1.  ```path("hello/", include("hello.urls")),```
2. hello app
   1. urls.pyを作成
      1. 追記
         1. 下記 ※1
   2. views.py を作成
   3. templatesフォルダ作成
   4. helloフォルダ作成
   5. index.html作成


※1
```
from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"), 
]
```