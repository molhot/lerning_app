from django.urls import path
from tyoubo_app import views

app_name = 'tyoubo_app'
urlpatterns = [
    path('regist_item/', views.create_item, name='create_item'),  # 作成
    path('edit_item/<int:post_id>/', views.edit_item, name='edit_item'),  # 修正
    path('show_item/', views.read_item, name='show_item'),   # 一覧表示
    path('delete_item/<int:post_id>/', views.delete_item, name='delete_item'),   # 削除
]