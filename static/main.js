document.addEventListener('DOMContentLoaded', function() {
    const ctx = document.getElementById('creditChart').getContext('2d');

    new Chart(ctx, {
      type: 'line',
      data: {
        labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
        datasets: [{
          label: 'Amount of Credits',
          data: [5000, 10000, 7500, 20000, 15000, 30000],
          borderColor: 'rgb(75, 192, 192)',
          tension: 0.3,
          fill: false
        }]
      },
      options: {
        scales: {
          y: { beginAtZero: true }
        }
      }
    });
});
