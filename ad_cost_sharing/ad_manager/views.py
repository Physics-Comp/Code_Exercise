from django.shortcuts import render, get_object_or_404, redirect
from .models import AdRecord
from .forms import AdRecordForm
from django.db.models import Sum

def ad_record(request):
    if request.method == 'POST':
        form = AdRecordForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = AdRecordForm()

    ad_records = AdRecord.objects.all()
    total_cost_sharing = ad_records.aggregate(Sum('cost_sharing'))['cost_sharing__sum']
    total_reimbursement = ad_records.aggregate(Sum('reimbursement'))['reimbursement__sum']

    context = {
        'form': form,
        'ad_records': ad_records,
        'total_cost_sharing': total_cost_sharing,
        'total_reimbursement': total_reimbursement,
    }
    return render(request, 'ad_manager/ad_record.html', context)

def delete_ad_record(request, pk):
    # Get the AdRecord object to be deleted
    ad_record = get_object_or_404(AdRecord, pk=pk)
    if request.method == 'POST':
        # If the request method is POST, confirm and delete the object
        ad_record.delete()
        return redirect('ad_record')  # Redirect to a different view after deletion
    
    # Render a confirmation page (optional)
    return render(request, 'ad_manager/delete_ad_record.html', {'ad_record': ad_record})


