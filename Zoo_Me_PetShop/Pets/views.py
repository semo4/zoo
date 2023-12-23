from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Pet, Apply_adoption, Adoption_by_user
from django.contrib import messages
from .forms import Apply_adoption_form, AdoptionOfferForm


def home(request):
    template_name = ("home.html")
    user_name = request.user
    hide_user_name = False
    if user_name and not str(user_name) == 'AnonymousUser':
        hide_user_name = True
    return render(request, 'Pets/home.html', {'hide_user_name': hide_user_name, 'user_name': user_name})


def my_pets(request):
    user_name = request.user
    hide_user_name = False
    user_id = request.user.id
    if user_name and not str(user_name) == 'AnonymousUser':
        hide_user_name = True
        apply_adoptions = Apply_adoption.objects.filter(user_owner_id=user_id)
    return render(request, 'Pets/my_pets.html', {'hide_user_name': hide_user_name, 'user_name': user_name, 'apply_adoptions': apply_adoptions})


def main(request):
    menu = Pet.objects.all()
    user_name = request.user
    hide_user_name = False
    if user_name and not str(user_name) == 'AnonymousUser':
        hide_user_name = True
    return render(request, 'Pets/pets.html', {'menu': menu, 'hide_user_name': hide_user_name, 'user_name': user_name})


def pet_details(request, pk):
    pet = Pet.objects.filter(id=pk).values().get()
    user_name = request.user
    hide_user_name = False
    if user_name and not str(user_name) == 'AnonymousUser':
        hide_user_name = True
    return render(request, 'Pets/pet_details.html', {'pet': pet, 'hide_user_name': hide_user_name, 'user_name': user_name})


def adoption_user(request):
    user_name = request.user
    hide_user_name = False
    if user_name and not str(user_name) == 'AnonymousUser':
        hide_user_name = True
    return render(request, 'Pets/adoption_user.html', {'hide_user_name': hide_user_name, 'user_name': user_name})


def apply_adoption(request, pk):
    user_id = request.user.id
    print(pk, user_id)
    result = Apply_adoption.objects.filter(
        pet_id=pk, user_owner_id=user_id).count()
    if result > 0:
        messages.error(request, 'You already applied for this pet !')
    else:
        row = dict()
        row['pet_id'] = pk
        row['user_owner_id'] = user_id
        data = Apply_adoption_form(row)
        data.save()
        pet_adoption_count = Apply_adoption.objects.all().count()
        if pet_adoption_count > 0:
            messages.success(
                request, "Application for adoption added succesfully, we will contact you soon, check My Pets")

    return redirect('Pets:pets')


@login_required(login_url='usersManagement:login')
def offer_adoption(request):
    if request.method == 'POST':
        print('Poooooooooooooooooost')
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
    offer_adoption_count = Adoption_by_user.objects.all().count()
    if offer_adoption_count > 0:
        messages.success(
            request, "Application for Offering adoption added succesfully, we will contact you soon, check My Pets")
    return redirect('Pets:pets')


# def your_view(request):
#     if request.method == 'POST':
#         form = YourForm(request.POST)
#         if form.is_valid():
#             choice = form.cleaned_data['choice']
#             # Do something with the choice value, like save it with your model data
#             return HttpResponseRedirect('/success/')
#     else:
#         form = YourForm()
#     return render(request, 'your_template.html', {'form': form})


# @login_required
# def adopt_pet(request, pk):
#     if request.method == 'POST':
#         user_name = request.user
#         pet = Pets.objects.filter(id=pk).values().get()
#         row = dict()
#         row['owner'] = request.user
#         row['petName'] = pet['petName']
#         row['petBirthdate'] = pet['petBirthdate']
#         row['type'] = pet['type']
#         row['breed'] = pet['breed']
#         row['petImage'] = pet['petImage']
#         row['description'] = pet['description']
#         data = AdoptionForm(row)
#         data.save()
#         messages.success(request, 'You have successfully adopted a pet!')
#         return redirect('members:adopt_pet')
#     else:
#         return redirect('members:adopt_pet')

 # if request.method == 'POST':
    #     form = AdoptionOfferForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         messages.success(request, "Application for adoption added succesfully, we will contact you soon, check My Pets")
    #         return redirect('Pets:pets')
    # else:
    #     form = AdoptionOfferForm()
    # return redirect('Pets:pets')
    # return render(request, 'offer_adoption.html', {'form': form})
    # row = dict()
    # row['owner'] = pk
    # row['petName'] = user_id
    # data = AdoptionOfferForm(row)
    # data.save()
    # pet_adoption_count = Apply_adoption.objects.all().count()
    # if pet_adoption_count > 0:
    #     messages.success(request, "Application for adoption added succesfully, we will contact you soon, check My Pets")

# from django.shortcuts import render
# from django.http import HttpResponseRedirect
# from .forms import YourForm

# def your_view(request):
#     if request.method == 'POST':
#         form = YourForm(request.POST)
#         if form.is_valid():
#             user_id = form.cleaned_data['user_id']
#             # Do something with the user_id, like save it with your model data
#             return HttpResponseRedirect('/success/')
#     else:
#         form = YourForm()
#     return render(request, 'your_template.html', {'form': form})
