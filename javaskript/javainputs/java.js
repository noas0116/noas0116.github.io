console.log("tja mannen välkommen till console log");

let name = "fargen"

function setText() {
    let input1 = document.getElementById("input1")
    let input2 = document.getElementById("input2")
    let input3 = document.getElementById("input3")

    let text = document.getElementById("text")


    text.innerHTML = input1.value + "." + input2.value + "@" + input3.value + ".com"
    
    let red = Math.floor(Math.random() *256)
    let green = Math.floor(Math.random() *256)
    let blue = Math.floor(Math.random() *256)

    document.body.style.backgroundColor = `rgb(${red}, ${green}, ${blue})`
}

