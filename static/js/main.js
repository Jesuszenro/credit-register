let chart; // Global variable to hold the chart instance

function loadChart(type) {
    let url = '';
    let chartType = 'bar';

    if (type === 'client') {
        url = '/api/credit_by_client';
        chartType = 'line';
    } else if (type === 'total') {
        url = '/api/total_credit';
        chartType = 'line';
    } else if (type === 'range') {
        url = '/api/credit_by_range';
        chartType = 'pie';  
    }

    fetch(url)
        .then(response => response.json())
        .then(data => {
            const ctx = document.getElementById('creditChart').getContext('2d');

            // Destroy the previous chart if it exists
            if (chart) {
                chart.destroy();
            }

            chart = new Chart(ctx, {
                type: chartType,
                data: {
                    labels: data.labels,
                    datasets: [{
                        label: 'Amount',
                        data: data.amounts,
                        backgroundColor: [
                            '#262626',
                            '#404040',
                            '#696969',
                            '#808080',
                            '#a9a9a9',
                            '#d3d3d3',
                            '#f5f5f5',
                        ],
                        borderColor: 'rgba(0, 0, 0, 1)',
                        borderWidth: 1
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    scales: {
                        y: {
                            beginAtZero: true,
                            display: chartType === 'bar'
                        }
                    }
                }
            });
        })
        .catch(error => console.error('Error loading chart:', error));
}

// Check if the chart element exists before adding the event listener
document.addEventListener('DOMContentLoaded', () => {
    loadChart('client');
});


