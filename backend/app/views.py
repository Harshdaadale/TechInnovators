from django.shortcuts import render, redirect

def retailer_signup(request):
    if request.method == "POST":
        # Process form data here (save to database, validate, etc.)
        
        return redirect("aboutus")  # Redirect to "About Us" page
    return render(request, "retailer-signup.html")
