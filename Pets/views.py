from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Pet, Apply_adoption, Adoption_by_user
from .forms import Apply_adoption_form, AdoptionOfferForm


def home(request):
    user_name = request.user
    hide_user_name = False
    if user_name and not str(user_name) == 'AnonymousUser':
        hide_user_name = True
    return render(request, 'Pets/home.html', {'hide_user_name': hide_user_name, 'user_name': user_name})


def about(request):
    user_name = request.user
    hide_user_name = False
    if user_name and not str(user_name) == 'AnonymousUser':
        hide_user_name = True
    return render(request, 'Pets/about.html', {'hide_user_name': hide_user_name, 'user_name': user_name})


def my_pets(request):
    user_name = request.user
    hide_user_name = False
    user_id = request.user.id
    print(user_name)
    if user_name and not str(user_name) == 'AnonymousUser':
        hide_user_name = True
        try:
            apply_adoptions = get_list_or_404(
                Apply_adoption, user_owner_id=user_id)
            print(apply_adoptions)
        except Exception as e:
            print(e)
            apply_adoptions = []
        try:
            adaption_by_user = get_list_or_404(Adoption_by_user, owner=user_id)
            print(adaption_by_user)
        except Exception as e:
            print(e)
            adaption_by_user = []
    return render(request, 'Pets/my_pets.html', {'hide_user_name': hide_user_name, 'user_name': user_name, 'apply_adoptions': apply_adoptions, 'adaption_by_user': adaption_by_user})


def main(request):
    menu = Pet.objects.all()
    print(menu)
    user_name = request.user
    hide_user_name = False
    if user_name and not str(user_name) == 'AnonymousUser':
        hide_user_name = True
    return render(request, 'Pets/pets.html', {'menu': menu, 'hide_user_name': hide_user_name, 'user_name': user_name})


def pet_details(request, pk):
    pet = Pet.objects.filter(id=pk).values().get()
    user_name = request.user
    user_id = request.user.id
    hide_user_name = False
    if user_name and not str(user_name) == 'AnonymousUser':
        hide_user_name = True
        try:
            res = get_object_or_404(
                Apply_adoption, pet_id=pk, user_owner_id=user_id)
            if res.user_owner_id.id == user_id and res.pet_id.id == pk:
                exist_pet = "You already applied for this pet !"
        except Exception as e:
            print(e)
            exist_pet = ''
    return render(request, 'Pets/pet_details.html', {'pet': pet, 'hide_user_name': hide_user_name, 'user_name': user_name, 'exist_pet': exist_pet})


def adoption_user(request):
    user_name = request.user
    hide_user_name = False
    if user_name and not str(user_name) == 'AnonymousUser':
        hide_user_name = True
    return render(request, 'Pets/adoption_user.html', {'hide_user_name': hide_user_name, 'user_name': user_name})


def apply_adoption(request, pk):
    user_id = request.user.id
    row = dict()
    row['pet_id'] = pk
    row['user_owner_id'] = user_id
    data = Apply_adoption_form(row)
    data.save()
    return redirect('Pets:pets')


@login_required(login_url='usersManagement:login')
def offer_adoption(request):
    if request.method == 'POST':
        row = dict()
        row['owner'] = request.user.id
        row['petName'] = request.POST.get('petName')
        row['petBirthdate'] = request.POST.get('petBirthdate')
        row['type'] = request.POST.get('inlineRadioOptions')
        row['breed'] = request.POST.get('breed')
        row['petImage'] = request.POST.get('petImage')
        row['description'] = request.POST.get('description')
        data = AdoptionOfferForm(row)
        data.save()
    return redirect('Pets:pets')
