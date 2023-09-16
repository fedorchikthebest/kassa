const $grafica = document.querySelector("#chart");
let response = await fetch("/charts/data");
let response_data = await response.json()
const tags = response_data.tags
const dataSales2020 = {
    label: "Количество проданных товаров",
    data: response_data.data,
    backgroundColor: 'rgba(54, 162, 235, 0.2)',
    borderColor: 'rgba(54, 162, 235, 1)',
    borderWidth: 1,
};
new Chart($grafica, {
    type: 'bar',
    data: {
        labels: tags,
        datasets: [
            dataSales2020,
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