<template>
  <div :class="themeClass" class="min-h-screen transition-colors duration-300">
    
    <Navbar :theme="theme" :isLoggedIn="isLoggedIn" @toggle-theme="toggleTheme"/>

    <!-- Page Header -->
    <header :class="cardClass" class="text-center py-10 mt-16">
      <h2 class="text-[2rem] font-bold">View Organizations</h2>
      <p class="text-lg mt-3">Explore organizations participating in PSoC</p>
    </header>

    <!-- Filters Section -->
    <section :class="dropClass, cardClass" class="p-8 flex flex-wrap gap-6 justify-center rounded-xl shadow-md mx-12 my-12">
      <input v-model="searchQuery" type="text" placeholder="Search by organization name" class="p-2 border rounded-md" />
      <select v-model="selectedDomain" class="p-2 border rounded-md">
        <option value="">All Domains</option>
        <option v-for="domain in uniqueDomains" :key="domain" :value="domain">{{ domain }}</option>
      </select>
      <input v-model.number="minProjects" type="number" placeholder="Min. no. of Projects" class="p-2 border rounded-md" />
      <input v-model.number="minYears" type="number" placeholder="Min. no. of Years" class="p-2 border rounded-md" />
    </section>

    <!-- Organizations Grid -->
    <section class="grid md:grid-cols-3 gap-8 px-12">
      <div v-for="org in filteredOrganizations" :key="org.id" 
      class="p-6 rounded-lg shadow-md hover:shadow-lg transition space-y-4"
      :class="cardClass">
        <h3 class="text-3xl font-bold">{{ org.name }}</h3>
        <p class="text-lg mt-2"><b>Domain:</b> {{ org.domain }}</p>
        <p class="text-lg mt-2"><b>About:</b> {{ org.about }}</p>
        <p class="text-lg mt-2"><b>Projects:</b> {{ org.projects }}</p>
        <p class="text-lg mt-2"><b>Years in PSoC:</b> {{ org.years }}</p>
        <div class="mt-5 flex space-x-4">
          <a v-if="org.website" :href="org.website" target="_blank" class="text-blue-500 hover:underline">Website</a>
          <a v-if="org.github" :href="org.github" target="_blank" class="text-blue-500 hover:underline">GitHub</a>
          <a v-if="org.linkedin" :href="org.linkedin" target="_blank" class="text-blue-500 hover:underline">LinkedIn</a>
        </div>
        <router-link :to="`/viewprojects?org=${org.name}`">
          <button class="mt-4 px-5 py-2 rounded-lg shadow transition" :class="buttonClass">View Projects</button>
        </router-link>
      </div>
    </section>

    <Footer :theme="theme" />
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from "vue";
import Navbar from '@/components/Navbar.vue';
import Footer from '@/components/Footer.vue';

const theme = ref("light");
const searchQuery = ref("");
const selectedDomain = ref("");
const minProjects = ref("");
const minYears = ref("");

const organizations = ref([
  { id: 1, name: "AI Innovators", domain: "AI", about: "Pioneering AI Research", projects: 12, years: 5, website: "#", github: "#", linkedin: "#" },
  { id: 2, name: "Blockchain Builders", domain: "Blockchain", about: "Decentralized Solutions", projects: 8, years: 4, website: "#", github: "#", linkedin: "#" },
  { id: 3, name: "CyberSec Defenders", domain: "Cybersecurity", about: "Protecting Digital Assets", projects: 6, years: 3, website: "#", github: "#", linkedin: "#" },
  { id: 4, name: "Quantum Leap", domain: "Quantum Computing", about: "Exploring Quantum Tech", projects: 5, years: 2, website: "#", github: "#", linkedin: "#" },
  { id: 5, name: "EcoTech Solutions", domain: "Sustainability", about: "Green Tech Innovations", projects: 7, years: 4, website: "#", github: "#", linkedin: "#" },
  { id: 6, name: "MedTech Pioneers", domain: "Healthcare", about: "AI in Medicine", projects: 9, years: 5, website: "#", github: "#", linkedin: "#" },
  { id: 7, name: "EduFuture", domain: "EdTech", about: "Revolutionizing Learning", projects: 11, years: 6, website: "#", github: "#", linkedin: "#" },
  { id: 8, name: "FinTech Gurus", domain: "Finance", about: "Modernizing Payments", projects: 10, years: 4, website: "#", github: "#", linkedin: "#" },
  { id: 9, name: "RoboWorks", domain: "Robotics", about: "Building Next-Gen Robots", projects: 8, years: 3, website: "#", github: "#", linkedin: "#" },
  { id: 10, name: "Cloud Nexus", domain: "Cloud Computing", about: "Scalable Cloud Solutions", projects: 13, years: 7, website: "#", github: "#", linkedin: "#" }
]);

const themeClass = computed(() => (theme.value === "light" ? "bg-light-background text-light-text" : "bg-dark-background text-dark-text"));
const navClass = computed(() => (theme.value === "light" ? "bg-light-navBackground text-light-navText" : "bg-dark-navBackground text-dark-navText"));
const linkClass = computed(() => (theme.value === "light" ? "text-light-link" : "text-dark-link"));
const buttonClass = computed(() => (theme.value === "light" ? "bg-light-buttonBackground text-light-buttonText" : "bg-dark-buttonBackground text-dark-buttonText"));
const cardClass = computed(() => (theme.value === "light" ? "bg-light-cardBackground text-light-text" : "bg-dark-cardBackground text-dark-text"));
const dropClass= computed(()=>theme.value=== "light" ? "text-light-text" : "text-light-text")
const uniqueDomains = computed(() => [...new Set(organizations.value.map(org => org.domain))]);
const filteredOrganizations = computed(() =>
  organizations.value.filter(org =>
    (!searchQuery.value || org.name.toLowerCase().includes(searchQuery.value.toLowerCase())) &&
    (!selectedDomain.value || org.domain === selectedDomain.value) &&
    (!minProjects.value || org.projects >= minProjects.value) &&
    (!minYears.value || org.years >= minYears.value)
  )
);

const toggleTheme = () => {
  theme.value = theme.value === "light" ? "dark" : "light";
  localStorage.setItem("theme", theme.value);
};

onMounted(() => {
  theme.value = localStorage.getItem("theme") || "light";
});
</script>
