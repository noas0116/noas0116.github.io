from nicegui import ui

def do_stuff():
    title.text = "lingaguliguliguli wata lingagu"
    title.update()

with ui.row():
    ui.button("klicka på mig bror", on_click=lambda: do_stuff())

ui.image('https://media1.tenor.com/m/z5o8ATj1KYwAAAAd/dancing-guy-don-pollo-dancing.gif')

ui.run(native=True)
