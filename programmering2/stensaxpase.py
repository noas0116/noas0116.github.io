import random

val = ["sten", "sax", "påse"]
dator_poäng = 0
spelar_poäng = 0
while dator_poäng < 3 and spelar_poäng < 3: 

    mitt_val = input("välj mellan sten,sax eller påse bror ")
    datorns_val = random.choice(val) 
 
    print("ditt val:", mitt_val)
    print("motsåndarens val:", datorns_val)

    if mitt_val == "sten" and datorns_val == "sax":
        spelar_poäng +=1

    if mitt_val == "påse" and datorns_val == "sten":
        spelar_poäng +=1

    if mitt_val == "sax" and datorns_val == "påse":
        spelar_poäng +=1      

if spelar_poäng == 3:
    print("ez win du vann!!!1")

if dator_poäng == 3:
    print("L bozo du förlora")