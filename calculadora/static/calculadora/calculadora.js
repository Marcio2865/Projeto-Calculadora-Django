const display = document.querySelector("#display")
const um = document.querySelector("#um")
const dois = document.querySelector("#dois")
const tres = document.querySelector("#tres")
const quatro = document.querySelector("#quatro")
const cinco = document.querySelector("#cinco")
const seis = document.querySelector("#seis")
const sete = document.querySelector("#sete")
const oito = document.querySelector("#oito")
const nove = document.querySelector("#nove")
const zero = document.querySelector("#zero")
const apagar = document.querySelector("#apagar")
const soma = document.querySelector("#soma")
const sub = document.querySelector("#sub")
const mult = document.querySelector("#mult")
const div = document.querySelector("#div")
const pot = document.querySelector("#pot")
const rad = document.querySelector("#rad")
const igual = document.querySelector("#igual")
const virgula = document.querySelector("#virgula")
const erase = document.querySelector("#erase")


let primeiroNumero
let segundoNumero
let operador
let resultado


console.log(um)

zero.addEventListener("click", function () {

    if(display.textContent === "0"){
        display.textContent = 0
    }else {
        display.textContent += 0
    }
})


console.log(um)

um.addEventListener("click", function () {

    if(display.textContent === "0"){
        display.textContent = 1
    }else {
        display.textContent += 1
    }
})


console.log(dois)

dois.addEventListener("click", function () {

    if(display.textContent === "0"){
        display.textContent = 2
    }else {
        display.textContent += 2
    }
})


console.log(tres)

tres.addEventListener("click", function () {

    if(display.textContent === "0"){
        display.textContent = 3
    }else {
        display.textContent += 3
    }
})


console.log(quatro)

quatro.addEventListener("click", function () {

    if(display.textContent === "0"){
        display.textContent = 4
    }else {
        display.textContent += 4
    }
})


console.log(cinco)

cinco.addEventListener("click", function () {

    if(display.textContent === "0"){
        display.textContent = 5
    }else {
        display.textContent += 5
    }
})


console.log(seis)

seis.addEventListener("click", function () {

    if(display.textContent === "0"){
        display.textContent = 6
    }else {
        display.textContent += 6
    }
})


console.log(sete)

sete.addEventListener("click", function () {

    if(display.textContent === "0"){
        display.textContent = 7
    }else {
        display.textContent += 7
    }
})


console.log(oito)

oito.addEventListener("click", function () {

    if(display.textContent === "0"){
        display.textContent = 8
    }else {
        display.textContent += 8
    }
})


console.log(nove)

nove.addEventListener("click", function () {

    if(display.textContent === "0"){
        display.textContent = 9
    }else {
        display.textContent += 9
    }
})


console.log(virgula)

virgula.addEventListener("click", function () {

    if (display.textContent.includes(",")) {
        return
    }

    if(display.textContent === "0"){
        display.textContent = "0,"
    }else {
        display.textContent += ","
    }
})

apagar.addEventListener("click", function () {
    display.textContent = 0
})


erase.addEventListener("click", function () {

    display.textContent = display.textContent.slice(0, -1)

    if (display.textContent === "") {
        display.textContent = "0"
    }

})


soma.addEventListener("click", function () {

    primeiroNumero = display.textContent

    operador = "+"

    display.textContent = "0"

})


sub.addEventListener("click", function () {

    primeiroNumero = display.textContent

    operador = "-"

    display.textContent = "0"

})


mult.addEventListener("click", function () {

    primeiroNumero = display.textContent

    operador = "*"

    display.textContent = "0"

})


div.addEventListener("click", function () {

    primeiroNumero = display.textContent

    operador = "/"

    display.textContent = "0"

})


pot.addEventListener("click", function () {

    primeiroNumero = display.textContent

    operador = "^"

    display.textContent = "0"

})


rad.addEventListener("click", function () {

    primeiroNumero = display.textContent

    operador = "√"

    display.textContent = "0"

})


igual.addEventListener("click", function () {

    segundoNumero = display.textContent

    const numero1 = Number(primeiroNumero.replace(",", "."))
    const numero2 = Number(segundoNumero.replace(",", "."))

    let resultado = 0

    if (operador === "+") {
        resultado = numero1 + numero2
    }
    else if (operador === "-") {
        resultado = numero1 - numero2
    }
    else if (operador === "*") {
        resultado = numero1 * numero2
    }
    else if (operador === "/") {
        resultado = numero1 / numero2
    }
    else if (operador === "^") {
        resultado = numero1 ** numero2
    }
    else if (operador === "√") {
        resultado = numero1 * numero1
    }

    display.textContent = resultado
})