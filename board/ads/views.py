from django.shortcuts import render, get_object_or_404, redirect
from .models import Ad
from .forms import AdForm


def ad_list(request):
    """
    Отображает список всех объявлений.
    """
    ads = Ad.objects.all()
    return render(request, 'ads/ad_list.html', {'ads': ads})


def ad_detail(request, ad_id):
    """
    Отображает детали конкретного объявления по его ID.

    Args:
        ad_id (int): ID объявления.
    """
    ad = get_object_or_404(Ad, id=ad_id)
    return render(request, 'ads/ad_detail.html', {'ad': ad})


def ad_create(request):
    """
    Создает новое объявление.

    Если запрос POST, сохраняет форму и перенаправляет на список объявлений.
    В противном случае отображает пустую форму.
    """
    if request.method == 'POST':
        form = AdForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ad_list')
    else:
        form = AdForm()

    return render(request, 'ads/ad_form.html', {'form': form})


def ad_update(request, ad_id):
    """
    Обновляет существующее объявление по его ID.

    Args:
        ad_id (int): ID объявления.

    Если запрос POST, сохраняет обновленную форму и перенаправляет на список объявлений.
    В противном случае отображает текущие данные в форме.
    """
    ad = get_object_or_404(Ad, id=ad_id)

    if request.method == 'POST':
        form = AdForm(request.POST, instance=ad)
        if form.is_valid():
            form.save()
            return redirect('ad_detail', ad_id=ad.id)
    else:
        form = AdForm(instance=ad)

    return render(request, 'ads/ad_form.html', {'form': form})


def ad_delete(request, ad_id):
    """
    Удаляет существующее объявление по его ID.

    Args:
        ad_id (int): ID объявления.

    Если запрос POST, удаляет объявление и перенаправляет на список объявлений.
    В противном случае отображает страницу подтверждения удаления.
    """
    ad = get_object_or_404(Ad, id=ad_id)

    if request.method == 'POST':
        ad.delete()
        return redirect('ad_list')

    return render(request, 'ads/ad_confirm_delete.html', {'ad': ad})
