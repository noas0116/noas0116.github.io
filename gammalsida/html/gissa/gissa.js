const slumptal = Math.floor(Math.random() * 9) + 1
let antalgissningar = 0


slump = Math.random()

function gissaTal() {
    console.log(slump = (slumptal))
    let textfelt_gissa = document.getElementById("gissa").value
    let gissa_int = Number(textfelt_gissa)
    let vinn = false
    let p_svar = document.getElementById("p_svar")

    if (antalgissningar < 3) {

        if (slumptal === gissa_int) {
            console.log("Rätt Svar")
            vinn = true
            p_svar.innerHTML = "DU VANN!!!!"


        }
        else {
            console.log("fel svar!!!!")
            if (antalgissningar === 2) {
                p_svar.innerHTML = "Loserr!!!!"

            }
            else {
                p_svar.innerHTML = `Fel Svar! ${gissa_int}`

                // tömmer text fältet så använder sliupper sudda
                document.getElementById("gissa").value = ""
                document.getElementById("gissa").focus()
            }
        }

        antalgissningar++

    }
    else {


        p_svar.innerHTML = "Fel! Ladda om sidan igen"
    }

    if (vinn) {
        var sound = new Audio('correct.mp3');
        sound.play();
     } else {
        var sound_i = new Audio('buzzer.mp3');
        sound_i.play();
     }

}


