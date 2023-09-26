document.querySelector("#btnConsult").addEventListener('click', consult)

function consult () {
    let id = document.getElementById("id").value
    let obj = {"id": id}
    fetch('/consult_user', {
        "method": "post",
        "headers": {"Content-Type":"application/json"},
        "body": JSON.stringify(obj)
    })
    .then(rta => rta.json())
    .then(data => showData(data))
    .catch(error => alert(error))
}

function showData(data) {
    let name = data[0][0]
    let lastname = data[0][1]
    let age = data[0][3]
    document.getElementById("txtData").value = name + "\n" + lastname + "\n" + age
}