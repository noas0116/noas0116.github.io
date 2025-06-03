from nicegui import ui

target = input('Skriv ett namn som du vill ta bort: ')

def rensa_namn():
    new_f = open("ny konversation.txt", "w", encoding='utf-8')
    f = open("konversation.txt", "r", encoding='utf-8')

    for line in f:
    name = line.split(":")[0]

    if target != name: 
    new_f.write(line)
 
ui.label("Välj en person att ta bort meddelanden från:")

namn_input = ui.input("Skriv namnet du vill ta bort")
ui.button("Ta bort", on_click=rensa_namn)
ui.run(native=True) 
