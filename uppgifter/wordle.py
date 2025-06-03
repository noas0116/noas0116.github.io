from nicegui import ui
import random 

# färgar bara
# ratt:
# typratt:
# fel:

with ui.column():
    gissa = ui.number(label='Gissa pinkod (4 siffror)', placeholder='0')

knapp = ui.button('Tryck mig för att gissa')

# def kolla_rod():
#   svar_status = 

# def kolla_gul():
#   svar_status = 

# def kolla_():gron():
#   svar_status = 

ui.label('🟩 Grön = Rätt siffra på rätt plats')
ui.label('🟨 Gul = Rätt siffra men på fel plats')
ui.label('🟥 Röd = Fel siffra')

ui.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQyBey6FoTN6rk9JpI6j74t7LJ2fP0WMIk4AA&s")

ui.run(native=True)