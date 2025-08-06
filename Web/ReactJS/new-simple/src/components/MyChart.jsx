import { useEffect, useRef } from 'react';
import { Chart } from 'chart.js/auto';

export function MyChart() {
    const chartRef = useRef(null);

    useEffect(() => {
        let chartInstance;

        fetch('https://dummyjson.com/products')
            .then(response => response.json())
            .then(data => {
                const minOrderQuantities = data.products.map(product => product.minimumOrderQuantity);
                const labels = data.products.map(product => product.title);

                const ctx = chartRef.current.getContext('2d');
                chartInstance = new Chart(ctx, {
                    type: 'bar',
                    data: {
                        labels: labels,
                        datasets: [{
                            label: 'Minimum Order Quantity',
                            data: minOrderQuantities,
                            borderWidth: 1
                        }]
                    },
                    options: {
                        scales: {
                            y: {
                                beginAtZero: true
                            }
                        }
                    }
                });
            })
            .catch(error => console.error('Error fetching data:', error));

        // Cleanup chart on component unmount
        return () => {
            if (chartInstance) {
                chartInstance.destroy();
            }
        };
    }, []);

    return (
        <>
            <canvas ref={chartRef} id="myChart" width="1000"/>
        </>
    );
}