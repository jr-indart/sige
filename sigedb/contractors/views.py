from django.shortcuts import render
from sigedb.contractors.forms import ContractorForm


def contractor(request):
    context = {'form': ContractorForm()}
    return render(request, 'contractors/contractor_form.html', context)