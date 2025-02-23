<template>
  <div :class="themeClass" class="min-h-screen transition-colors duration-300">
    
    <Navbar :theme="theme" :isLoggedIn="isLoggedIn" @toggle-theme="toggleTheme"/>

    <!-- Page Header -->
    <header :class="cardClass" class="text-center py-10 mt-16">
      <h2 class="text-[2rem] font-bold">View Projects</h2>
      <p class="text-lg mt-3">Explore projects under different organizations in PSoC</p>
    </header>

    <!-- Filters Section -->
    <section :class="dropClass, cardClass" class="p-8 flex flex-wrap gap-6 justify-center rounded-xl shadow-md mx-12 my-12">
      <input v-model="searchQuery" type="text" placeholder="Search by project name" class="p-2 border rounded-md" />
      <select v-model="selectedDomain" class="p-2 border rounded-md">
        <option value="">All Domains</option>
        <option v-for="domain in uniqueDomains" :key="domain" :value="domain">{{ domain }}</option>
      </select>
      <select v-model="selectedOrg" class="p-2 border rounded-md">
        <option value="">All Organizations</option>
        <option v-for="org in uniqueOrganizations" :key="org" :value="org">{{ org }}</option>
      </select>
    </section>

    <!-- Projects Grid -->
    <section class="grid md:grid-cols-3 gap-8 px-12">
      <div v-for="project in filteredProjects" 
          :key="project.id" 
          class="p-6 rounded-lg shadow-md hover:shadow-lg transition space-y-4"
          :class="cardClass">
        <h3 class="text-3xl font-bold">{{ project.name }}</h3>  <!-- Increased to text-3xl -->
        <p class="text-lg mt-2"><b>Organization:</b> {{ project.organization }}</p> <!-- text-lg -->
        <p class="text-lg mt-2"><b>Domain:</b> {{ project.domain }}</p> <!-- text-lg -->
        <p class="text-lg mt-2"><b>Description:</b> {{ project.description }}</p> <!-- text-lg -->
        <div class="mt-5 flex space-x-4">
          <a v-if="project.github" :href="project.github" target="_blank" class="text-xl text-blue-500 hover:underline">
            GitHub
          </a>
          <router-link 
            v-if="userRole === 'Contributor'" 
            :to="{ name: 'Proposal Submission', params: { title: project.name } }" 
            class="text-xl text-green-500 hover:underline"
          >
            Submit Proposal
          </router-link>

        </div>
      </div>
    </section>

    <Footer :theme="theme" />
  </div>
</template>

<script setup>
import { ref, computed, onMounted, watchEffect } from "vue";
import Navbar from '@/components/Navbar.vue';
import Footer from '@/components/Footer.vue';
const theme = ref("light");
const searchQuery = ref("");
const selectedDomain = ref("");
const selectedOrg = ref("");
const userRole = ref("");
const projects = ref([
  { "id": 1, "name": "AI Chatbot", "organization": "AI Innovators", "domain": "AI", "description": "Building an intelligent chatbot for customer support.", "github": "#" },
  { "id": 2, "name": "Neural Art Generator", "organization": "AI Innovators", "domain": "AI", "description": "An AI-based image style transfer system.", "github": "#" },
  { "id": 3, "name": "Decentralized Voting", "organization": "Blockchain Builders", "domain": "Blockchain", "description": "Secure blockchain-based voting system.", "github": "#" },
  { "id": 4, "name": "Crypto Wallet Security", "organization": "Blockchain Builders", "domain": "Blockchain", "description": "Enhancing security in crypto transactions.", "github": "#" },
  { "id": 5, "name": "CyberShield", "organization": "CyberSec Defenders", "domain": "Cybersecurity", "description": "Advanced threat detection system.", "github": "#" },
  { "id": 6, "name": "AI Chatbot", "organization": "AI Innovators", "domain": "AI", "description": "Building an intelligent chatbot for customer support.", "github": "#" },
  { "id": 7, "name": "Neural Art Generator", "organization": "AI Innovators", "domain": "AI", "description": "An AI-based image style transfer system.", "github": "#" },
  { "id": 8, "name": "Decentralized Voting", "organization": "Blockchain Builders", "domain": "Blockchain", "description": "Secure blockchain-based voting system.", "github": "#" },
  { "id": 9, "name": "Crypto Wallet Security", "organization": "Blockchain Builders", "domain": "Blockchain", "description": "Enhancing security in crypto transactions.", "github": "#" },
  { "id": 10, "name": "CyberShield", "organization": "CyberSec Defenders", "domain": "Cybersecurity", "description": "Advanced threat detection system.", "github": "#" },
  { "id": 11, "name": "AI Chatbot", "organization": "AI Innovators", "domain": "AI", "description": "Building an intelligent chatbot for customer support.", "github": "#" },
  { "id": 12, "name": "Neural Art Generator", "organization": "AI Innovators", "domain": "AI", "description": "An AI-based image style transfer system.", "github": "#" },
  { "id": 13, "name": "Decentralized Voting", "organization": "Blockchain Builders", "domain": "Blockchain", "description": "Secure blockchain-based voting system.", "github": "#" },
  { "id": 14, "name": "Crypto Wallet Security", "organization": "Blockchain Builders", "domain": "Blockchain", "description": "Enhancing security in crypto transactions.", "github": "#" },
  { "id": 15, "name": "CyberShield", "organization": "CyberSec Defenders", "domain": "Cybersecurity", "description": "Advanced threat detection system.", "github": "#" }
]);

const themeClass = computed(() => theme.value === "light" ? "bg-light-background text-light-text" : "bg-dark-background text-dark-text");
const navClass = computed(() => theme.value === "light" ? "bg-light-navBackground text-light-navText" : "bg-dark-navBackground text-dark-navText");
const linkClass = computed(() => theme.value === "light" ? "text-light-link" : "text-dark-link");
const buttonClass = computed(() => theme.value === "light" ? "bg-light-buttonBackground text-light-buttonText" : "bg-dark-buttonBackground text-dark-buttonText");
const cardClass = computed(() => theme.value === "light" ? "bg-light-cardBackground text-light-text" : "bg-dark-cardBackground text-dark-text");
const dropClass= computed(()=>theme.value=== "light" ? "text-light-text" : "text-light-text")
const uniqueDomains = computed(() => [...new Set(projects.value.map(proj => proj.domain))]);
const uniqueOrganizations = computed(() => [...new Set(projects.value.map(proj => proj.organization))]);

const filteredProjects = computed(() => {
  return projects.value.filter(proj =>
    (!searchQuery.value || proj.name.toLowerCase().includes(searchQuery.value.toLowerCase())) &&
    (!selectedDomain.value || proj.domain === selectedDomain.value) &&
    (!selectedOrg.value || proj.organization === selectedOrg.value)
  );
});

const toggleTheme = () => {
  theme.value = theme.value === "light" ? "dark" : "light";
  localStorage.setItem("theme", theme.value);
};

onMounted(() => {
  theme.value = localStorage.getItem("theme") || "light";

  userRole.value = localStorage.getItem("role");

  // Extract query parameters from URL
  const params = new URLSearchParams(window.location.search);
  const orgParam = params.get("org");

  // Set the organization filter if 'org' is found in the URL
  if (orgParam) {
    selectedOrg.value = decodeURIComponent(orgParam);
  }

  // Reset search query to make sure filtering happens
  searchQuery.value = "";
});
  watchEffect(() => {
    if (!uniqueOrganizations.value.includes(selectedOrg.value)) {
      selectedOrg.value = ""; // Reset if it's not in the list
    }
  });

</script>
