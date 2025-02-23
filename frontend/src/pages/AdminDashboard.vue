<template>
  <div :class="themeClass" class="min-h-screen flex flex-col transition-colors duration-300">
    <!-- Navbar -->
    <Navbar :theme="theme" :isLoggedIn="isLoggedIn" @toggle-theme="toggleTheme" />
    
    <div class="pt-20 px-6 w-full">

      <!-- Stats Section -->
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 mt-6 gap-6 text-center">
        <Card v-for="(stat, key) in stats" 
              :key="key" 
              :class="cardClass" 
              class="p-8 shadow-lg">
          
          <!-- Wrapper for Proper Stacking -->
          <div class="flex flex-col items-center justify-center space-y-4">
            <!-- Title on Top -->
            <CardTitle :class="textClass" class="text-3xl font-bold">
              {{ stat.label }}
            </CardTitle>
            
            <!-- Count Below -->
            <CardContent :class="textClass" class="text-6xl font-extrabold">
              {{ stat.value }}
            </CardContent>
          </div>

        </Card>
      </div>

      <!-- Graphs Section -->
      <div class="grid grid-cols-1 md:grid-cols-3 mt-10 gap-8 w-full">
        <LineChart class="w-full" :data="contributorData" title="Contributor Proposals Submitted vs Time" :theme="theme" />
        <LineChart class="w-full" :data="projectsData" title="Projects Submitted by Organization vs Time" :theme="theme" />
        <LineChart class="w-full" :data="organizationsData" title="Organizations Registered vs Time" :theme="theme" />
      </div>

      <!-- Organization Approvals -->
      <div class="mt-14">
        <h2 :class="textClass" class="text-4xl font-extrabold mb-8 text-center">Organization Approvals</h2>
        
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          <Card v-for="org in organizations" :key="org.id" :class="cardClass" class="p-8 space-y-6 shadow-lg">
            <CardHeader>
              <CardTitle :class="textClass" class="text-2xl font-semibold text-center">
                {{ org.name }}
              </CardTitle>
              <CardDescription :class="textClass + ' opacity-80 text-center'">
                {{ org.description }}
              </CardDescription>
            </CardHeader>
            <CardContent :class="textClass + ' opacity-90 space-y-3'">
              <p><span class="font-semibold">Head:</span> {{ org.head }}</p>
              <p><span class="font-semibold">Founded:</span> {{ org.founded }}</p>
              <p><span class="font-semibold">Location:</span> {{ org.location }}</p>
            </CardContent>
            <CardFooter class="flex gap-4 mt-6 justify-center">
              <Button class="bg-blue-500 hover:bg-blue-400 text-white px-6 py-3 text-lg rounded" @click="viewOrganization(org.id)">View</Button>
              <Button class="bg-green-500 hover:bg-green-400 text-white px-6 py-3 text-lg rounded" @click="approveOrganization(org.id)">Approve</Button>
              <Button class="bg-red-600 hover:bg-red-400 text-white px-6 py-3 text-lg rounded" @click="declineOrganization(org.id)">Decline</Button>
            </CardFooter>
          </Card>
        </div>
      </div>
    </div>

    <!-- Footer -->
    <Footer :theme="theme" />
  </div>
</template>


<script setup>
import { ref, computed, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import Navbar from '@/components/Navbar.vue';
import Footer from '@/components/Footer.vue';
import LineChart from '@/components/LineChart.vue';

const router = useRouter();
const theme = ref(localStorage.getItem("theme") || "light");

const organizations = ref([
  { id: 1, name: "Python Software Foundation", head: "Guido van Rossum", founded: "2001", location: "USA", description: "Manages the Python language.", approved: false, declined: false },
  { id: 2, name: "OpenAI", head: "Sam Altman", founded: "2015", location: "USA", description: "AI research and deployment company.", approved: true, declined: false },
  { id: 3, name: "Linux Foundation", head: "Linus Torvalds", founded: "2007", location: "USA", description: "Supports open-source development.", approved: false, declined: true }
]);

const stats = computed(() => {
  return {
    pending: { label: "Pending", value: organizations.value.filter(o => !o.approved && !o.declined).length },
    approved: { label: "Approved", value: organizations.value.filter(o => o.approved).length },
    declined: { label: "Declined", value: organizations.value.filter(o => o.declined).length },
    total: { label: "Total", value: organizations.value.length }
  };
});

const contributorData = ref([
  { date: "2024-01-01", value: 5 },
  { date: "2024-01-02", value: 8 },
  { date: "2024-01-03", value: 12 },
  { date: "2024-01-04", value: 15 },
  { date: "2024-01-05", value: 17 },
  { date: "2024-01-06", value: 22 },
  { date: "2024-01-07", value: 25 },
  { date: "2024-01-08", value: 30 },
  { date: "2024-01-09", value: 34 },
  { date: "2024-01-10", value: 40 },
  { date: "2024-01-11", value: 42 },
  { date: "2024-01-12", value: 50 },
  { date: "2024-01-13", value: 58 },
  { date: "2024-01-14", value: 65 },
  { date: "2024-01-15", value: 73 },
  { date: "2024-01-16", value: 80 },
  { date: "2024-01-17", value: 85 },
  { date: "2024-01-18", value: 92 },
  { date: "2024-01-19", value: 98 },
  { date: "2024-01-20", value: 105 },
  { date: "2024-01-21", value: 112 },
  { date: "2024-01-22", value: 120 },
  { date: "2024-01-23", value: 130 },
  { date: "2024-01-24", value: 140 },
  { date: "2024-01-25", value: 150 },
  { date: "2024-01-26", value: 160 },
  { date: "2024-01-27", value: 175 },
  { date: "2024-01-28", value: 190 },
  { date: "2024-01-29", value: 205 },
  { date: "2024-01-30", value: 220 },
  { date: "2024-01-31", value: 230 }
]);

const projectsData = ref([
  { date: "2024-01-01", value: 2 },
  { date: "2024-01-02", value: 3 },
  { date: "2024-01-03", value: 7 },
  { date: "2024-01-04", value: 9 },
  { date: "2024-01-05", value: 12 },
  { date: "2024-01-06", value: 14 },
  { date: "2024-01-07", value: 16 },
  { date: "2024-01-08", value: 19 },
  { date: "2024-01-09", value: 21 },
  { date: "2024-01-10", value: 24 },
  { date: "2024-01-11", value: 27 },
  { date: "2024-01-12", value: 30 },
  { date: "2024-01-13", value: 33 },
  { date: "2024-01-14", value: 38 },
  { date: "2024-01-15", value: 42 },
  { date: "2024-01-16", value: 47 },
  { date: "2024-01-17", value: 51 },
  { date: "2024-01-18", value: 55 },
  { date: "2024-01-19", value: 60 },
  { date: "2024-01-20", value: 65 },
  { date: "2024-01-21", value: 70 },
  { date: "2024-01-22", value: 75 },
  { date: "2024-01-23", value: 80 },
  { date: "2024-01-24", value: 85 },
  { date: "2024-01-25", value: 90 },
  { date: "2024-01-26", value: 95 },
  { date: "2024-01-27", value: 100 },
  { date: "2024-01-28", value: 105 },
  { date: "2024-01-29", value: 110 },
  { date: "2024-01-30", value: 115 },
  { date: "2024-01-31", value: 120 }
]);

const organizationsData = ref([
  { date: "2024-01-01", value: 1 },
  { date: "2024-01-02", value: 4 },
  { date: "2024-01-03", value: 6 },
  { date: "2024-01-04", value: 9 },
  { date: "2024-01-05", value: 11 },
  { date: "2024-01-06", value: 13 },
  { date: "2024-01-07", value: 16 },
  { date: "2024-01-08", value: 20 },
  { date: "2024-01-09", value: 23 },
  { date: "2024-01-10", value: 27 },
  { date: "2024-01-11", value: 30 },
  { date: "2024-01-12", value: 34 },
  { date: "2024-01-13", value: 38 },
  { date: "2024-01-14", value: 42 },
  { date: "2024-01-15", value: 46 },
  { date: "2024-01-16", value: 51 },
  { date: "2024-01-17", value: 55 },
  { date: "2024-01-18", value: 60 },
  { date: "2024-01-19", value: 65 },
  { date: "2024-01-20", value: 70 },
  { date: "2024-01-21", value: 75 },
  { date: "2024-01-22", value: 80 },
  { date: "2024-01-23", value: 85 },
  { date: "2024-01-24", value: 90 },
  { date: "2024-01-25", value: 95 },
  { date: "2024-01-26", value: 100 },
  { date: "2024-01-27", value: 105 },
  { date: "2024-01-28", value: 110 },
  { date: "2024-01-29", value: 115 },
  { date: "2024-01-30", value: 120 },
  { date: "2024-01-31", value: 125 }
]);

const themeClass = computed(() => 
  theme.value === "dark" ? "bg-gray-900 text-white" : "bg-white text-black"
);

const cardClass = computed(() => 
  theme.value === "dark" ? "bg-gray-800 text-white shadow-lg" : "bg-white text-black shadow-lg"
);

const textClass = computed(() => 
  theme.value === "dark" ? "text-gray-100" : "text-gray-900"
);

const buttonClass = computed(() => 
  theme.value === "dark" ? "bg-gray-700 hover:bg-gray-600 text-white" : "bg-gray-200 hover:bg-gray-300 text-black"
);

const borderClass = computed(() =>
  theme.value === "dark" ? "border-gray-700" : "border-gray-300"
);

const toggleTheme = () => {
  theme.value = theme.value === "dark" ? "light" : "dark";
  localStorage.setItem("theme", theme.value);
};

const viewOrganization = (id) => { router.push(`/organization/${id}`); };
const approveOrganization = (id) => { console.log(`Approved ${id}`); };
const declineOrganization = (id) => { console.log(`Declined ${id}`); };
</script>

<style scoped>
.pt-20 {
  padding-top: 5rem;
}
.grid-cols-4 {
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
}
.card {
  transition: all 0.3s ease-in-out;
}
</style>
