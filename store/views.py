from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PurchaseRegistrationForm

@login_required
def register_purchase(request):
    if request.method == "POST":
        form = PurchaseRegistrationForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect("purchase_success")
    else:
        form = PurchaseRegistrationForm()

    return render(request, "store/register_purchase.html", {"form": form})

@login_required
def purchase_success(request):
    return render(request, "store/purchase_success.html")
