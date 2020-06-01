from django.shortcuts import render
from django.utils import timezone
from .models import Transaction


def index(request):
    incoming_list = [
        100000000002,
        100000000001,
        100000000004,
        100000000000,
    ]
    var_list = []
    final_list = []
    for incoming_id in incoming_list:
        temp = Transaction.objects.filter(aadhaar_info__aadhaar_id=incoming_id)
        var_list.append(temp) if temp else final_list.append((incoming_id, True))
    for i in var_list:
        for j in range(len(i)):
            temp_timestamp = float(str(timezone.now() - i[j].timestamp).split()[0])
            final_list.append((i[j].aadhaar_info.aadhaar_id, True)) if temp_timestamp > i[j].state_info.time_limit else final_list.append((i[j].aadhaar_info.aadhaar_id, False))

    context = {
        'final_list': final_list
    }
    return render(request, 'liquor_management_system/index.html', context)
