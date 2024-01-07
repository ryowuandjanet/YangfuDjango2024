from django import forms
from .models import *
from django.forms.models import inlineformset_factory

COMPANY_LIST = [
  ("",""),
  ("揚富開發有限公司","揚富開發有限公司"),
  ("鉅鈦開發有限公司","鉅鈦開發有限公司"),
]

CASESTATUS_CHOICES = [
  ("在途","在途"),
  ("結案","結案"),
]

BUILD_TYPE_USE= [
  ("",""),
  ("公設","公設"),
  ("公寓-5樓含以下無電梯","公寓-5樓含以下無電梯"),
  ("透天厝","透天厝"),
  ("店面-店舖","店面-店舖"),
  ("辦公商業大樓","辦公商業大樓"),
  ("住宅大樓-11層含以上有電梯","住宅大樓-11層含以上有電梯"),
  ("華廈-10層含以下有電梯","華廈-10層含以下有電梯"),
  ("套房","套房"),
  ("農舍","農舍"),
  ("增建-持分後坪數打對折","增建-持分後坪數打對折")
]

AREA_LIST = [
  ("",""),
  ("第一種住宅區","第一種住宅區"),
  ("第二種住宅區","第二種住宅區"),
  ("第三種住宅區","第三種住宅區"),
  ("第四種住宅區","第四種住宅區"),
  ("第五種住宅區","第五種住宅區"),
  ("第一種商業區","第一種商業區"),
  ("第二種商業區","第二種商業區"),
  ("第三種商業區","第三種商業區"),
  ("第四種商業區","第四種商業區"),
  ("第二種工業區","第二種工業區"),
  ("第三種工業區","第三種工業區"),
  ("行政區","行政區"),
  ("文教區","文教區"),
  ("倉庫區","倉庫區"),
  ("風景區","風景區"),
  ("農業區","農業區"),
  ("保護區","保護區"),
  ("行水區","行水區"),
  ("保存區","保存區"),
  ("特定專用區","特定專用區")
]

class YfcaseForm(forms.ModelForm):
  yfcaseCompany = forms.ChoiceField(label="所屬公司",choices=COMPANY_LIST, widget=forms.Select(attrs={'class': 'form-select'}))
  yfcaseCaseStatus = forms.ChoiceField(label="案件狀態",choices=CASESTATUS_CHOICES)

  class Meta:
    model=Yfcase
    fields ='__all__'

class LandForm(forms.ModelForm):
  yfcase = forms.ModelChoiceField(Yfcase.objects.all(), widget=forms.HiddenInput())

  class Meta:
    model=Land
    fields ='__all__'

class BuildForm(forms.ModelForm):
  yfcase = forms.ModelChoiceField(Yfcase.objects.all(), widget=forms.HiddenInput())
  buildTypeUse = forms.ChoiceField(label="建物型",choices=BUILD_TYPE_USE, required=False)
  buildUsePartition = forms.ChoiceField(label="使用分區",choices=AREA_LIST, required=False)

  class Meta:
    model=Build
    fields ='__all__'

class PersonForm(forms.ModelForm):
  class Meta:
    model = Person
    fields = '__all__'


LandFormSet = inlineformset_factory(
  Yfcase, Land, form=LandForm,
  extra=1, can_delete=True, can_delete_extra=True
)

BuildFormSet = inlineformset_factory(
  Yfcase, Build, form=BuildForm,
  extra=1, can_delete=True, can_delete_extra=True
)
    
PersonFormSet = inlineformset_factory(
  Yfcase, Person, form=PersonForm,
  extra=1, can_delete=True, can_delete_extra=True
)
   