from django.shortcuts import render,get_object_or_404,redirect
from .models import Turlar,Gullar
from .forms import TurForm,GulForm


# Create your views here.
def turlar_list(request):
    turlar = Turlar.objects.all()
    content = {'turlar':turlar}
    return render(request,'turlar_list.html',content)

def gullar_list(request):
    gullar = Gullar.objects.all()
    content = {'gullar':gullar}
    return render(request,'gullar_list.html',content)

def tur_by_gullar(request,tur_id):
    turi = get_object_or_404(Turlar,pk = tur_id)
    gullar = Gullar.objects.filter(turi=turi)
    return render(request,'tur_by_gullar.html',{'tur':turi,'gullar':gullar})

def gul_detail(request,gul_id):
    gul = get_object_or_404(Gullar,pk = gul_id)
    return render(request,'gul_detail.html',{'gul':gul})
def add_tur(request):
    if request.method == 'POST':
        form = TurForm(request.POST)
        if form.is_valid():
            Turlar.objects.create(
                name=form.cleaned_data['name'],
                description=form.cleaned_data['description']
            ) 
            return redirect('/')  
    else:
        form = TurForm()  

    return render(request, 'add_tur.html', {'form': form})


def add_gul(request):
    if request.method == 'POST':
        form = GulForm(request.POST)
        if form.is_valid():
            turi = form.cleaned_data['turi']
            Gullar.objects.create(
                name=form.cleaned_data['name'],
                description=form.cleaned_data['description'],
                price=form.cleaned_data['price'],
                turi=turi 
            )
            return redirect('/')  
    else:
        form = GulForm() 
   
    return render(request, 'add_gul.html', {'form': form})

def update_tur(request, tur_id):
    tur = get_object_or_404(Turlar, pk=tur_id)

    if request.method == 'POST':
        form = TurForm(request.POST)
        if form.is_valid():
            tur.name = form.cleaned_data['name']
            tur.description = form.cleaned_data['description']
            tur.save()  
            return redirect('/')  
    else:
        form = TurForm(initial={'name': tur.name, 'description': tur.description})

    return render(request, 'add_tur.html', {'form': form})

def update_gul(request, gul_id):
    gul = get_object_or_404(Gullar, pk=gul_id)

    if request.method == 'POST':
        form = GulForm(request.POST)
        if form.is_valid():
            gul.name = form.cleaned_data['name']
            gul.description = form.cleaned_data['description']
            gul.price = form.cleaned_data['price']
            tur_id = form.cleaned_data['turi']
            gul.turi = Turlar.objects.get(id=tur_id) 
            gul.save() 
            return redirect('/')
    else:
        form = GulForm(initial={
            'name': gul.name,
            'description': gul.description,
            'price': gul.price,
            'turi': gul.turi.id
        })

    return render(request, 'add_gul.html', {'form': form})

 
def delete_tur(request, tur_id):
    tur = get_object_or_404(Turlar, pk=tur_id) 
    if request.method == 'POST':
        tur.delete() 
        return redirect('/')  
    return render(request, 'delete_tur.html', {'tur': tur})

def delete_gul(request, gul_id):
    gul = get_object_or_404(Gullar, pk=gul_id)
    if request.method == 'POST':
        gul.delete() 
        return redirect('/')
    return render(request, 'delete_gul.html', {'gul': gul})


