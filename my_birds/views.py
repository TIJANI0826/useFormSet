from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.shortcuts import render,get_object_or_404
# Create your views here.
# views.py
from django.views.generic import ListView,TemplateView
from .models import Bird
from .forms import BirdFormSet


class AjaxTemplateMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if not hasattr(self, 'ajax_template_name'):
            split = self.template_name.split('.html')
            split[-1] = '_inner'
            split.append('.html')
            self.ajax_template_name = ''.join(split)
        if request.is_ajax():
            self.template_name = self.ajax_template_name
        return super(AjaxTemplateMixin, self).dispatch(request, *args, **kwargs)

class BirdListView(ListView):
    model = Bird
    template_name = "bird_list.html"

class BirdDetail(DetailView,AjaxTemplateMixin):
    model = Bird

class BirdDelete(DeleteView,AjaxTemplateMixin):
    model = Bird
    success_url = reverse_lazy('bird_list')

class EditBird(UpdateView,AjaxTemplateMixin):
    model = Bird 
    fields = '__all__'
    success_url = reverse_lazy('bird_list')

class BirdAddView(TemplateView,AjaxTemplateMixin):
    template_name = "add_bird.html"

    # Define method to handle GET request
    def get(self, *args, **kwargs):
        # Create an instance of the formset
        formset = BirdFormSet(queryset=Bird.objects.none())
        return self.render_to_response({'bird_formset': formset})
    # Define method to handle POST request
    def post(self, *args, **kwargs):

        formset = BirdFormSet(data=self.request.POST)

        # Check if submitted forms are valid
        if formset.is_valid():
            formset.save()
            return redirect(reverse_lazy("bird_list"))

        return self.render_to_response({'bird_formset': formset})
from django.http import JsonResponse

def ajax_get_view(request): # May include more arguments depending on URL parameters
    # Get data from the database - Ex. Model.object.get(...)
    data = {
            'my_data':data_to_display
    }
    return JsonResponse(data)