from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from sigedb.contractors.forms import ContractorForm


def contractor(request):
    if request.method == 'POST':
        #form = ContractorForm(request.POST)

        #if form.is_valid():
        #    form.cleaned_data

            # context = dict(contractor='Timor-Timor Lda', director='João do Timor', address='R. Jacinto, 233',
            #              telephone='670-7777-1234', email='timortimor@gmail.com')

            return HttpResponseRedirect('/contractor/')

        #else:
        #    context = {'form': ContractorForm()}
        #    return render(request, 'contractors/contractor_form.html', context)

    else:
        context = {'form': ContractorForm()}
        return render(request, 'contractors/contractor_form.html', context)