from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import render, redirect,get_object_or_404
from django.views.generic import DetailView, DeleteView, UpdateView, ListView, CreateView
from . models import Contact
from . forms import ContactUploadForm
from django.db.models import Q

# Create your views here.




class ContactCreateView(CreateView):
    model = Contact
    success_url = "/"
    template_name = 'contact/contact_create.html'
    fields = ["first_name","last_name", "surname","phone","email"]


class ContactListView(ListView):
 model = Contact
 template_name = 'contact/contact_list.html'  # Specify your template name
 context_object_name = 'contacts'  # Name of the context object to use in the template

def search(request):
    if request.method == "POST":
        query = request.POST.get('surname', None)
        if query:
            results = Contact.objects.filter(
                Q(surname__icontains=query) |
                Q(first_name__icontains=query) |
                Q(last_name__icontains=query)
            )
            return render(request, 'contact/search.html', {'contacts': results})
    
    return render(request, 'contact/search.html')

def contact_update(request, pk):
    obj = get_object_or_404(Contact, pk=pk)
    form = ContactUploadForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/')
    context = {
        'form':form
    }
    return render(request, 'contact/contact_update.html',context)



class ContactDeleteView(DeleteView):
    template_name = "contact/contact_delete.html"
    success_url = "/"
    model = Contact

class ContactDetailView(DetailView):
    template_name = "contact/contact_detail.html"
    model = Contact

