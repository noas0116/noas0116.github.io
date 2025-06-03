from nicegui import ui

def addition():
    result.text = num_1.value + num_2.value

def minus():
    result.text = num_1.value - num_2.value

def delat():
    result.text = num_1.value / num_2.value

def ganger():
    result.text = num_1.value * num_2.value

with ui.column():
    num_1 = ui.number(label='Skriv in ett nummer..', placeholder='0')
    num_2 = ui.number(label='Skriv in ett nummer..', placeholder='0')

with ui.row():
    ui.button('+', on_click= lambda : addition())
    ui.button('/', on_click= lambda : delat())
    ui.button('-', on_click= lambda : minus())
    ui.button('x', on_click= lambda : ganger())

with ui.column():
    ui.label('resultat: ')
    result = ui.label("")

ui.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQyBey6FoTN6rk9JpI6j74t7LJ2fP0WMIk4AA&s")

ui.run()