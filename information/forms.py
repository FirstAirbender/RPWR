from django.forms import *
from information.models import *
from django.contrib.admin import widgets 



class InformationForm(ModelForm):
	class Meta:
		model = Information
		fields = ['Index', 'Building_option', 'Room', 'Desk', 'Extension', 'UWID', 'Email', 'Last_Name', 'First_Name', 'Status', 'First_Supervisor', 'Second_Supervisor', 'Third_Supervisor', 'Start_Date', 'End_Date', 'FOB', 'FOB_pu', 'Added_to_existing_FOB']
		Building_option = MultipleChoiceField(
			choices = Building,
			required = True
			)
	def __init__(self, *args, **kwargs):
		super(InformationForm, self).__init__(*args, **kwargs)
		for field_name, field in self.fields.items():
			field.widget.attrs['class'] = 'form-control'
		# self.fields['Building_option'].choice = Building.objects.all().values_list('Building_Name', 'Building_Name')
		self.fields['Start_Date'].widget.attrs['class'] = 'form-control datepicker'
		self.fields['End_Date'].widget.attrs['class'] = 'form-control datepicker'
		# self.fields['Building_option'].widget.attrs['class'] = 'form-control'
		# self.fields['Building_option'].widget.attrs.pop('multiple', False) 
		# self.fields['Building_option'].widget.attrs['multiple']

# class BuildingForm(ModelForm):
# 	class Meta:
# 		model = Building
# 		fields = ['Building_Name']

	# buildingnames = ModelMultipleChoiceField(queryset = Information.objects.all())

# 	def __init__(self, *args, **kwargs):
# 		super(BuildingForm, self).__init__(*args, **kwargs)
# 		self.fields['Building_Name'].choice = Information.objects.all().values_list('Building_Name', 'Building_Name')