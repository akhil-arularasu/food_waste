from django.shortcuts import render
from foodwaste.models import CountryLevelWaste, PledgeInfo
from . import forms
import humanize
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,DeleteView,
                                UpdateView)
from django.db.models import Sum
from django.forms.utils import ErrorList

# # Create your views here.
# def index(request):
# 	return render(request,'foodwaste/home.html')
# def index(request):
# 	countries_list = CountryLevelWaste.objects.order_by('name')
# 	country_dict = {"country_records":countries_list}
# 	return render(request,'foodwaste/datascience.html',country_dict)

class IndexView(TemplateView):
	 template_name = 'foodwaste/country_list.html'

	 def get_context_data(self,**kwargs):
		 context  = super().get_context_data(**kwargs)
		 countries_list = CountryLevelWaste.objects.order_by('name')
		 context['country_records'] = countries_list
		 return context

class CountryLevelWasteView(ListView):
    # If you don't pass in this attribute,
    # Django will auto create a context name
    # for you with object_list!
    # Default would be 'school_list'

    # Example of making your own:
    # context_object_name = 'schools'
	context_object_name = 'country_records'
	model = CountryLevelWaste
	template_name = 'foodwaste/country_list.html'

class CountryChartView(TemplateView):
	template_name = 'foodwaste/country_chart.html'

	def get_context_data(self,**kwargs):
		context  = super().get_context_data(**kwargs)
		countries_list = CountryLevelWaste.objects.order_by('-total_waste')[:5]
		countries_list_all = CountryLevelWaste.objects.order_by('-total_waste')
		context['country_records'] = countries_list
		context['country_records_all'] = countries_list_all
		labels = []
		data = []
		for country in countries_list:
			labels.append(country.name)
			data.append(country.total_waste)

		context['labels'] = labels
		context['data'] = humanize.intword(data)
		return context

class CountryChartView(TemplateView):
	template_name = 'foodwaste/country_chart.html'

	def get_context_data(self,**kwargs):
		context  = super().get_context_data(**kwargs)
		countries_list = CountryLevelWaste.objects.order_by('-total_waste')[:5]
		countries_list_all = CountryLevelWaste.objects.order_by('-total_waste')
		context['country_records'] = countries_list
		context['country_records_all'] = countries_list_all
		labels = []
		data = []
		gdps = []
		wastes = []
		for country in countries_list:
			labels.append(country.name)
			data.append(country.total_waste)

		context['labels'] = labels
		context['data'] = humanize.intword(data)
		return context

class CountryDetailView(DetailView):
#    context_object_name = 'country_details'
    model = CountryLevelWaste
    template_name = 'foodwaste/country_detail.html'

    def get_context_data(self,**kwargs):
        context  = super().get_context_data(**kwargs)
        labels = []
        data = []
        labels.append("Organic Waste")
        labels.append("Other Waste")
        data.append(self.object.organic_waste_per_person)
        data.append(self.object.waste_per_person - self.object.organic_waste_per_person)
        context['country_details'] = self.object
        context['labels'] = labels
        context['data'] = humanize.intword(data)
        labels2 = []
        data2 = []
        labels2.append("Country Waste")
        labels2.append("Rest of World")
        all_waste = CountryLevelWaste.objects.aggregate(Sum('total_waste'))
        data2.append(self.object.total_waste)
        data2.append(all_waste.get('total_waste__sum') - self.object.total_waste)
        context['labels2'] = labels2
        context['data2'] = humanize.intword(data2)
        return context

class PledgeResultsView(TemplateView):
	 template_name = 'foodwaste/pledge-results.html'

	 def get_context_data(self,**kwargs):
		 context  = super().get_context_data(**kwargs)
		 pledged_reduction = PledgeInfo.objects.aggregate(Sum('pledged_reduction'))
		 context['pledged_reduction'] = pledged_reduction
		 return context

def compost(request):
	return render(request,'foodwaste/compost.html')

def about(request):
	return render(request,'foodwaste/about.html')

def press_coverage(request):
	return render(request,'foodwaste/press-coverage.html')

def compostdemo(request):
	return render(request,'foodwaste/compost-demo.html')

def compostschool(request):
	return render(request,'foodwaste/compost-school.html')

def milltownschool(request):
	return render(request,'foodwaste/milltown-school.html')

def foodwaste_report(request):
	return render(request,'foodwaste/foodwaste-report.html')

def Research_At_RVCC(request):
	return render(request,'foodwaste/Research_At_RVCC.html')


def pledge_info_view(request):
	form = forms.PledgeForm()

	if request.method == 'POST':
		form = forms.PledgeForm(request.POST)

		if form.is_valid():
			print('validation success')
			print( form.cleaned_data['zip_code'])
			form.save(commit=True)
			print(PledgeInfo.objects.aggregate(Sum('pledged_reduction')))
			pledged_reduction = PledgeInfo.objects.aggregate(Sum('pledged_reduction'))

			return render(request,'foodwaste/pledge_info_landing.html',{'pledged_reduction':pledged_reduction})
		else:
			print('ERROR invalid entry. Please review and resubmit')
			errors = form._errors.setdefault("pledged_reduction", ErrorList())
			errors.append(u'Please check and re-submit')
	return render(request,'foodwaste/pledge_info.html',{'form':form})
