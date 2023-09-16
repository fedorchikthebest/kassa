const $grafica = document.querySelector("#chart");
let response = await fetch("/charts/data");
let response_data = await response.json()
const tags = response_data.tags
const dataSales = {
    label: "Количество проданных товаров",
    data: response_data.data,
    backgroundColor: 'rgba(54, 162, 235, 0.2)',
    borderColor: 'rgba(54, 162, 235, 1)',
    borderWidth: 1,
};
let chart = new Chart($grafica, {
    type: 'bar',
    data: {
        labels: tags,
        datasets: [
            dataSales,
        ]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }],
        },
    }
});


async function charts_updater(){
    let response = await fetch("/charts/data");
    let response_data = await response.json()
    chart.data.labels = response_data.tags
    chart.data.datasets[0].data = response_data.data
    chart.update()
}


let timerId = setInterval(charts_updater, 5000);