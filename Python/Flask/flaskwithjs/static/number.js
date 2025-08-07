async function getNumber() {
    const url = "http://127.0.0.1:5000/number";
    try {
        const response = await fetch(url);
        if (!response.ok) {
        throw new Error(`Response status: ${response.status}`);
        }

        const json = await response.json();
        console.log(json);
        return json;
        // return json;
    } catch (error) {
        console.error(error.message);
    }
}

function loadNumber() {

    data = getNumber().then((data) => {
        const numberdiv = document.getElementById("number");
        numberdiv.innerHTML = `<h1>${data}</h1>`
    });
}

setInterval(loadNumber,3000);