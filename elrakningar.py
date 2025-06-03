import datetime

def elkostnad():
    start_datum = int(input("ange start datum bror "))
    slut_datum = int(input("ange slut datum bror "))

    start_mätaren = int(input("ange mätarinställningen vid startdatumet bror "))
    slut_mätaren = int(input("ange också mätarinställningen vid slutdatumet ")) 

    kostnad_kwh = int(input("ange kosntad peröre/kwh mannen "))
    daglig_avgift = int(input("ange daglig stående avgift i öre ")) 

    total_kostnad = ((dagar_diff * daglig_avgift) + (mätinställning_diff * kostnad_kwh)) * 1,25


start_datum = datetime.datetime(2024, 6, 17)
slut_datum = datetime.datetime(2024, 6, 17)


total_kostnad =





# länkar:
# https://www.w3schools.com/python/python_datetime.asp
# https://www.youtube.com/watch?v=eirjjyP2qcQ
# https://docs.python.org/3/library/datetime.html
