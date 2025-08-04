const pubChart = document.getElementById('graficoPublicaciones');
new Chart(pubChart, {
    type: 'doughnut',
    data: {
        labels: ['Publicadas', 'Borradores'],
        datasets: [{
            data: [pubChart.dataset.publicadas, pubChart.dataset.borradores],
            backgroundColor: ['#28a745', '#ffc107'],
        }]
    }
});

const viewsChart = document.getElementById('graficoVistas');
new Chart(viewsChart, {
    type: 'bar',
    data: {
        labels: JSON.parse(viewsChart.dataset.labels),
        datasets: [{
            label: 'Vistas',
            data: JSON.parse(viewsChart.dataset.views),
            backgroundColor: '#17a2b8'
        }]
    }
});
