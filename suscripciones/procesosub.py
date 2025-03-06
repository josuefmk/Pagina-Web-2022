def totalpagosub(request):  
    totalsub = 0

    if request.user.is_authenticated:
        if "suscripcionesMant" in request.session.keys():
            for key, value in request.session["suscripcionesMant"].items():
                totalsub += int(value["preciofinal"])
                print(totalsub)
    return {"totalpagosub": totalsub}