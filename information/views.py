from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from information.models import *
from information.forms import *
from django.forms.models import inlineformset_factory
import json
from django.contrib.auth.decorators import login_required, user_passes_test
# from django.utils import simplejson
def is_member(user):
	if user.is_authenticated:
		return user.groups.filter(name='Administrators').exists()

# @user_passes_test(is_member, '/error/',redirect_field_name = '')
def welcome(request):
	if request.user.is_authenticated() and is_member(request.user):
		return HttpResponseRedirect('/')
	elif request.user.is_authenticated() and not is_member(request.user):
		return HttpResponseRedirect('/error/')
	else:
		return render(request, 'welcome.html')

def error(request):
	if is_member(request.user):
		return HttpResponseRedirect('/welcome/')
	else:
		return render(request, 'error.html')


# @user_passes_test(is_member, '/error/',redirect_field_name = '')
@user_passes_test(is_member, '/welcome/',redirect_field_name = '')
def home(request):
	form = Information.objects.all()
	# buildinglist = []
	# for i in form:
	# 	x=i.Building.upper()
	# 	# buildinglist = [x.upper() for x in buildinglist]
	# 	if x not in buildinglist:
	# 		buildinglist.append(x)
	# building_list = json.dumps(buildinglist)
	# print building_list
	building = Building.objects.all()
	return render(request, 'home.html', {'form': form, 'building': building})

@user_passes_test(is_member, '/error/',redirect_field_name = '')
def add_student(request):
	# BuildingFormSet = inlineformset_factory(Information, Building,form = BuildingForm, extra = 1, can_delete = True)
	if request.method == 'POST':
		form = InformationForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			i = form.save(commit = False)
			i.save()
			print i.Building_option, 'asdfafsasdfasfhkafskj h'
			# form.save_m2m()
			# print i.id, "ID let us see what this is after save"
			return HttpResponseRedirect('/details/'+str(i.id))
	else:
		i = Information()
		# build = BuildingFormSet(instance = i)
		form = InformationForm(instance = i)
		# print form.Start_Date
	return render(request, 'edit.html', {'form': form})


	# return HttpResponseRedirect('/edit/%s' % i.id)
@user_passes_test(is_member, '/error/',redirect_field_name = '')
def edit_student(request, form_id):
	i = get_object_or_404(Information, pk=form_id)
	# i = Information.objects.get(pk = form_id)
	print request.method, 'asdfasfae fde asd'
	# form = 1
	if request.method == "POST":
		form = InformationForm(request.POST, instance = i)
		if form.is_valid():
			cd = form.cleaned_data
			i.save()
			return HttpResponseRedirect('/details/'+form_id)
	else:
		form = InformationForm(instance = i)
	return render(request, 'edit.html', {'form': form, 'info': i})

@user_passes_test(is_member, '/error/',redirect_field_name = '')
def details(request, form_id):
	form = get_object_or_404(Information, pk=form_id)
	return render(request, 'details.html', {'form': form})

from tastypie.resources import ModelResource, Resource
from tastypie.paginator import Paginator
from tastypie.authorization import Authorization, ReadOnlyAuthorization
from tastypie.exceptions import Unauthorized
from tastypie.authentication import SessionAuthentication, ApiKeyAuthentication, MultiAuthentication, BasicAuthentication
from tastypie.cache import NoCache, SimpleCache
from tastypie.constants import ALL, ALL_WITH_RELATIONS
from tastypie.fields import CharField
from tastypie import fields

class UserPickAuthorization(Authorization):
	def authorize_user(self, bundle):
		print 'Authorize User'

class InformationResource(ModelResource):
	class Meta:
		queryset = Information.objects.all()
		resource_name = "Information"
		allowed_methods = ['get']
		authorization = UserPickAuthorization()
		authentication = MultiAuthentication(SessionAuthentication(), ApiKeyAuthentication())
		filtering = {'Building':ALL}
		cache = NoCache()

def obj_create(self, bundle, request = None, **kwargs):
	return super(DatabaseResource, self).obj_create(bundle, request, user=request.user)