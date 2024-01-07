# views.py
from django.shortcuts import render, redirect
from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.contrib import messages
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import *
from .models import *


class YfcaseInline():
  form_class = YfcaseForm
  model = Yfcase
  template_name = "app/yfcase_create_or_update.html"

  def form_valid(self, form):
    named_formsets = self.get_named_formsets()
    if not all((x.is_valid() for x in named_formsets.values())):
      return self.render_to_response(self.get_context_data(form=form))
    self.object = form.save()

    for name, formset in named_formsets.items():
      formset_save_func = getattr(self, 'formset_{0}_valid'.format(name), None)
      if formset_save_func is not None:
        formset_save_func(formset)
      else:
        formset.save()
    return redirect('app:list_yfcases')


  def formset_lands_valid(self, formset):
    lands = formset.save(commit=False)  
    for obj in formset.deleted_objects:
      obj.delete()
    for land in lands:
      land.yfcase = self.object
      land.save()


  def formset_builds_valid(self, formset):
    builds = formset.save(commit=False)  
    for obj in formset.deleted_objects:
      obj.delete()
    for build in builds:
      build.yfcase = self.object
      build.save()

  def formset_people_valid(self, formset):
    people = formset.save(commit=False)  
    for obj in formset.deleted_objects:
      obj.delete()
    for person in people:
      person.yfcase = self.object
      person.save()

class YfcaseList(ListView):
    model = Yfcase
    template_name = "app/yfcase_list.html"
    context_object_name = "yfcases"


class YfcaseCreate(YfcaseInline, CreateView):
    def get_context_data(self, **kwargs):
        # 繼承父類的 get_context_data 方法，以獲取默認的上下文數據
        ctx = super(YfcaseCreate, self).get_context_data(**kwargs)
        
        # 將自定義的 named_formsets 數據添加到上下文中
        ctx['named_formsets'] = self.get_named_formsets()
        return ctx


    def get_named_formsets(self):
        # 判斷請求的方法是 GET 還是 POST
        if self.request.method == "GET":
            # 如果是 GET 請求，則返回一個包含預設值的字典
            return {
                'lands': LandFormSet(prefix='lands'),
                'builds': BuildFormSet(prefix='builds'),
                'people': PersonFormSet(prefix='people'),
            }
        else:
            # 如果是 POST 請求，則根據請求的內容和文件創建一個包含表單集的字典
            return {
                'lands': LandFormSet(
                    self.request.POST or None,
                    self.request.FILES or None,
                    prefix='lands'
                ),
                'builds': BuildFormSet(
                    self.request.POST or None,
                    self.request.FILES or None,
                    prefix='builds'
                ),
                'people': PersonFormSet(
                    self.request.POST or None,
                    self.request.FILES or None,
                    prefix='people'
                ),
            }

class YfcaseUpdate(YfcaseInline, UpdateView):
    def get_context_data(self, **kwargs):
        # 繼承父類的 get_context_data 方法，以獲取默認的上下文數據
        ctx = super(YfcaseUpdate, self).get_context_data(**kwargs)
        
        # 將自定義的 named_formsets 數據添加到上下文中
        ctx['named_formsets'] = self.get_named_formsets()
        return ctx


    def get_named_formsets(self):
        # 返回一個包含表單集的字典，用於在模板中使用
        return {
            'lands': LandFormSet(
                self.request.POST or None,
                self.request.FILES or None,
                instance=self.object,
                prefix='lands'
            ),
            'builds': BuildFormSet(
                self.request.POST or None,
                self.request.FILES or None,
                instance=self.object,
                prefix='builds'
            ),
            'people': PersonFormSet(
                self.request.POST or None,
                self.request.FILES or None,
                instance=self.object,
                prefix='people'
            ),
        }
    
# views.py
class YfcaseDelete(DeleteView):
  model = Yfcase
  template_name = 'app/yfcase_confirm_delete.html'
  success_url = reverse_lazy('app:list_yfcases')
  def get_success_url(self):
    messages.success(self.request, 'Product deleted successfully.')
    return super().get_success_url()

# views.py
def delete_land(request, pk):
  try:
    land = Land.objects.get(id=pk)
  except Land.DoesNotExist:
    messages.success(request, 'Object Does not exit')
    return redirect('app:update_yfcase', pk=land.yfcase.id)
  land.delete()
  messages.success(request, 'Image deleted successfully')
  return redirect('app:update_yfcase', pk=land.yfcase.id)

# views.py
def delete_build(request, pk):
  try:
    build = Build.objects.get(id=pk)
  except Build.DoesNotExist:
    messages.success(request, 'Object Does not exit')
    return redirect('app:update_yfcase', pk=build.yfcase.id)
  build.delete()
  messages.success(request, 'Variant deleted successfully')
  return redirect('app:update_yfcase', pk=build.yfcase.id)

# views.py
def delete_person(request, pk):
  try:
    person = Person.objects.get(id=pk)
  except Person.DoesNotExist:
    messages.success(request, 'Object Does not exit')
    return redirect('app:update_yfcase', pk=person.yfcase.id)
  person.delete()
  messages.success(request, 'Variant deleted successfully')
  return redirect('app:update_yfcase', pk=person.yfcase.id)



