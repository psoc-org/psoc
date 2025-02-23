<template>
    <div :class="themeClass" class="w-full p-4 rounded-lg shadow-md">
      <h2 class="text-xl font-bold text-center mb-4">{{ title }}</h2>
      <canvas :id="chartId"></canvas>
    </div>
  </template>
  
  <script setup>
  import { onMounted, defineProps, ref, watch, computed } from 'vue';
  import { Chart, registerables } from 'chart.js';
  
  Chart.register(...registerables);
  
  const props = defineProps({
    title: String,
    data: Array,
    theme: String
  });
  
  const chartId = ref(`chart-${Math.random().toString(36).substr(2, 9)}`);
  const chartInstance = ref(null);
  
  const themeClass = computed(() => 
    props.theme === "dark" ? "bg-gray-900 text-white" : "bg-white text-black"
  );
  
  const createChart = () => {
    const ctx = document.getElementById(chartId.value)?.getContext('2d');
    if (!ctx) return;
  
    if (chartInstance.value) {
      chartInstance.value.destroy();
    }
  
    chartInstance.value = new Chart(ctx, {
      type: 'line',
      data: {
        labels: props.data.map(d => d.date),
        datasets: [{
          label: props.title,
          data: props.data.map(d => d.value),
          borderColor: props.theme === "dark" ? 'rgba(255, 255, 255, 1)' : 'rgba(75, 192, 192, 1)',
          backgroundColor: props.theme === "dark" ? 'rgba(255, 255, 255, 0.2)' : 'rgba(75, 192, 192, 0.2)',
          borderWidth: 2,
          tension: 0.3
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
          x: { grid: { color: props.theme === "dark" ? 'rgba(255, 255, 255, 0.2)' : 'rgba(200, 200, 200, 0.2)' } },
          y: { grid: { color: props.theme === "dark" ? 'rgba(255, 255, 255, 0.2)' : 'rgba(200, 200, 200, 0.2)' }, beginAtZero: true }
        }
      }
    });
  };
  
  onMounted(() => {
    createChart();
  });
  
  watch(() => props.theme, () => {
    createChart();
  });
  </script>
  
  <style scoped>
  canvas {
    width: 100% !important;
    height: 300px !important;
  }
  </style>
  