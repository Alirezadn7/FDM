from django.shortcuts import render,redirect
from .forms import PlayerForm , StatsForm
from .models import Player , Stats


# Create your views here.

#crete
def PlayerFormView(request):
    form = PlayerForm()
    
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    template_name = 'players/player.html'
    context = {'form':form}
        
    return render(request , template_name , context)
    
def StatsFormView(request):
    form = StatsForm()
    
    if request.method == 'POST':
        form = StatsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    template_name = "players/stats.html"
    context = {'form':form}
       
    return render(request , template_name , context)
#read    
def showView(request):
    players = Player.objects.all()
    stats = Stats.objects.all()
    template_name = 'players/show.html'
    context = {'players' : players,
               'stats' : stats
               }
    return render(request , template_name , context)
    
#update
def PlayersUpdateView(request , f_pid):
    obj = Player.objects.get(pid=f_pid)
    form = PlayerForm(instance=obj)
    if request.method == 'POST':
        form = PlayerForm(request.POST , instance=obj)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    template_name = 'players/player.html'
    context = {'form': form}
        
    return render(request , template_name , context)
    
def StatsUpdateView(request , stat_id):
    obj = Stats.objects.get(id=stat_id)
    form = StatsForm(instance=obj)
    if request.method == 'POST':
        form = StatsForm(request.POST , instance=obj)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    template_name = 'players/stats.html'
    context = {'form': form}
        
    return render(request , template_name , context)
    
#delete
def PlayerDeleteView(request , f_pid):
    obj = Player.objects.get(pid=f_pid)
    if request.method == 'POST':
        obj.delete()
        return redirect('show_url')
    template_name = 'players/confirmation.html'
    context = {'obj' : obj}
    
    return render(request , template_name , context)

def StatsDeleteView(request , stat_id):
    obj = Stats.objects.get(id=stat_id)
    if request.method == 'POST':
        obj.delete()
        return redirect('show_url')
    template_name = 'players/confirmation.html'
    context = {'obj': obj}
    return render(request, template_name, context)       
        
    
    
    