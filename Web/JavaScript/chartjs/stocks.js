var url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=EUR&apikey=demo';
var timerid;
var chart;
var labels;
var dataPoints;
var lasttime;

apiData = [];

function getStock() {
  return fetch(url)
          .then(res => res.json());
}

// function createChart() {
//   new Chart(ctx, {
//     type: 'line',
//     data {}
//   })
// }

function getData() {
  // url+=document.getElementById("apikey").value
  // console.log(url)
  getStock().then( data => {
    // apiData.push(data);
    addNewData(data);
  })

  console.log(apiData)
}

function startData() {
  if ( timerid == undefined ) {
    console.log("Starting data collection");
    timerid = setInterval(getData,5000);
    makeGraph();
  } else {
    console.log("Collection already started");
  }
}

function stopData() {
  clearInterval(timerid);
  console.log("Stopped data collection");
}

function addNewData(apiObject) {
  const rate = parseFloat(
    apiObject["Realtime Currency Exchange Rate"]["5. Exchange Rate"]
  );

  const time = apiObject["Realtime Currency Exchange Rate"]["6. Last Refreshed"];
  if ( lasttime !== time ) {
    labels.push(time);
    dataPoints.push(rate);
    lasttime = time;
  } else {
    console.log(`${lasttime} === ${time}`)
  }

  if ( lasttime == undefined ) {
    console.log(`Setting lasttime: ${lasttime}`)
    lasttime = time;
  }

  chart.update();
}

function makeGraph() {
  // Extract values
  labels = apiData.map(item =>
    item["Realtime Currency Exchange Rate"]["6. Last Refreshed"]
  );

  dataPoints = apiData.map(item =>
    parseFloat(item["Realtime Currency Exchange Rate"]["5. Exchange Rate"])
  );

  const ctx = document.getElementById("myChart").getContext("2d");

  chart = new Chart(ctx, {
    type: "line",
    data: {
      labels: labels,
      datasets: [{
        label: "BTC → EUR Exchange Rate",
        data: dataPoints,
        borderColor: "rgba(75, 192, 192, 1)",
        backgroundColor: "rgba(75, 192, 192, 0.2)",
        borderWidth: 2,
        tension: 0.2,
        pointRadius: 3
      }]
    },
    options: {
      responsive: true,
      scales: {
        x: {
          ticks: { maxRotation: 45, minRotation: 45 }
        },
        y: {
          beginAtZero: false
        }
      }
    }
  });

}