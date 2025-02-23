<script setup>
import { ref, onMounted } from "vue";
import { Chart as ChartJS, Title, Tooltip, Legend, LineElement, PointElement, CategoryScale, LinearScale } from "chart.js";
import { Line } from "vue-chartjs";

ChartJS.register(Title, Tooltip, Legend, LineElement, PointElement, CategoryScale, LinearScale);

const chartData = ref(null);
const chartOptions = ref({
  responsive: true,
  plugins: {
    legend: {
      position: "top"
    }
  }
});

onMounted(async () => {
  try {
    const response = await fetch("/api/method/psoc.api.contributor.get_admin_chats");
    const data = await response.json();
    const selectedChart = data.message;

    if (selectedChart && selectedChart.labels && selectedChart.values) {
      chartData.value = {
        labels: selectedChart.labels,
        datasets: [
          {
            label: selectedChart.chart_name,
            data: selectedChart.values,
            borderColor: selectedChart.color || "#000",
            backgroundColor: selectedChart.color ? selectedChart.color + "33" : "#00000033",
            fill: true,
            tension: 0.3,
            pointRadius: 5
          }
        ]
      };
    }
  } catch (error) {
    console.error("Error fetching chart data:", error);
  }
});
</script>

<template>
  <div class="p-6">
    <h1 class="text-2xl font-bold mb-4">📈 {{ chartData?.datasets[0]?.label || "Chart" }} (Line Chart)</h1>
    <Line v-if="chartData" :data="chartData" :options="chartOptions" />
    <p v-else class="text-gray-500">No chart data found...</p>
  </div>
</template>
