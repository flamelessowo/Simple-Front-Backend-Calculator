input = document.getElementById('myInput')
output = document.getElementById('myOutput')


function addToExpression(literal){
    input.value += literal
}
function clearExpression(){
    input.value = ''
}

async function sendInput(){
    let json = JSON.stringify({"expression": input.value})
    console.log(json)
    const response = await fetch('http://localhost:8000/calculate', {
        method: "POST",
        mode: 'cors',
        headers: {'Content-Type': 'application/json'},
        body: json
    })
    const unwrap = await response.json()
    output.value = unwrap.result

}