async function getClock() {
    const url = "http://127.0.0.1:5000/clock";
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

function loadClock() {

    data = getClock().then((data) => {
        const clockdiv = document.getElementById("clock");
        clockdiv.innerHTML = `<h1>${data.date}<br /><hr />${data.time}</h1>`
    });
}

setInterval(loadClock,1000);