from django.shortcuts import render, get_object_or_404, redirect
from django.forms import ModelForm
from tyoubo_app.models import ItemModel


def create_post(request):
    """
    新たなデータを作成する
    """
    post = ItemModel()
    if request.method == 'GET':
        form = RegistItemForm(instance=post)
        return render(request, 'tyoubo_app/tyoubo_page.html', {'form': form})
    if request.method == 'POST':
        form = RegistItemForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
        return redirect('tyoubo_app:read_post')

def read_post(request):
    """
    データの一覧を表示する
    """
    # 全オブジェクトを取得
    items = ItemModel.objects.all().order_by('id')
    return render(request,'tyoubo_app/tyoubo_page.html', {'items': items})  # Template に渡すデータ

def edit_post(request, post_id):
    """
    対象のデータを編集する
    """
    post = get_object_or_404(ItemModel, pk=post_id)
    if request.method == 'GET':
        form = RegistItemForm(instance=post)
        return render(request, 'tyoubo_app/item_regist_page.html', {'form': form, 'post_id': post_id})  # Template に渡すデータ
    elif request.method == 'POST':
        form = RegistItemForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
        return redirect('tyoubo_app:tyoubo_page.html')

def delete_post(request, post_id):
    post = get_object_or_404(ItemModel, pk=post_id)
    post.delete()
    return redirect('tyoubo_app:tyoubo_page.html')

class RegistItemForm(ModelForm):
    """
    フォーム定義
    """
    class Meta:
        model = ItemModel
        fields = ('name', 'price', 'type', 'date')
