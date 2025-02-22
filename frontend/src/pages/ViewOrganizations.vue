<template>
  <div :class="themeClass" class="min-h-screen transition-colors duration-300">
    
    <!-- Navbar -->
    <nav :class="navClass" class="w-full py-4 px-8 flex items-center justify-between fixed top-0 left-0 right-0 z-50 shadow">
      <h1 class="text-3xl font-extrabold">PSoC</h1>
      <div class="absolute left-1/2 transform -translate-x-1/2 flex space-x-6">
        <router-link to="/" :class="linkClass" class="font-medium hover:opacity-75">Home</router-link>
        <router-link to="/about" :class="linkClass" class="font-medium hover:opacity-75">About</router-link>
        <router-link to="/viewprojects" :class="linkClass" class="font-medium hover:opacity-75">View Projects</router-link>
        <router-link to="/contributors" :class="linkClass" class="font-medium hover:opacity-75">Contributors</router-link>
        <router-link to="/mentors" :class="linkClass" class="font-medium hover:opacity-75">Mentors</router-link>
        <router-link to="/organizers" :class="linkClass" class="font-medium hover:opacity-75">Organizers</router-link>
      </div>
      <button @click="toggleTheme" :class="buttonClass" class="px-4 py-2 rounded-lg transition">
        {{ theme === 'light' ? '🌙 Dark Mode' : '☀️ Light Mode' }}
      </button>
    </nav>

    <!-- Page Header -->
    <header class="text-center py-28 mt-16">
      <h2 class="text-4xl font-bold">View Organizations</h2>
      <p class="text-lg mt-2">Explore organizations participating in PSoC</p>
    </header>

    <!-- Filters Section -->
    <section class="p-6 flex flex-wrap gap-4 justify-center">
      <input v-model="searchQuery" type="text" placeholder="Search by name" class="p-2 border rounded-md" />
      <select v-model="selectedDomain" class="p-2 border rounded-md">
        <option value="">All Domains</option>
        <option v-for="domain in uniqueDomains" :key="domain" :value="domain">{{ domain }}</option>
      </select>
      <input v-model.number="minProjects" type="number" placeholder="Min Projects" class="p-2 border rounded-md" />
      <input v-model.number="minYears" type="number" placeholder="Min Years" class="p-2 border rounded-md" />
    </section>

    <!-- Organizations Grid -->
    <section class="grid md:grid-cols-3 gap-6 px-12">
      <div v-for="org in filteredOrganizations" :key="org.id" class="p-6 rounded-lg shadow-md hover:shadow-lg transition" :class="cardClass">
        <h3 class="text-2xl font-semibold">{{ org.name }}</h3>
        <p class="text-sm mt-1"><b>Domain:</b> {{ org.domain }}</p>
        <p class="text-sm"><b>About:</b> {{ org.about }}</p>
        <p class="text-sm"><b>Projects:</b> {{ org.projects }}</p>
        <p class="text-sm"><b>Years in PSoC:</b> {{ org.years }}</p>
        <div class="mt-4 flex space-x-3">
          <a v-if="org.website" :href="org.website" target="_blank" class="text-blue-500 hover:underline">Website</a>
          <a v-if="org.github" :href="org.github" target="_blank" class="text-blue-500 hover:underline">GitHub</a>
          <a v-if="org.linkedin" :href="org.linkedin" target="_blank" class="text-blue-500 hover:underline">LinkedIn</a>
        </div>
        <router-link :to="`/viewprojects?org=${org.id}`">
          <button class="mt-4 px-5 py-2 rounded-lg shadow transition" :class="buttonClass">View Projects</button>
        </router-link>
      </div>
    </section>

    <!-- Footer -->
    <footer class="text-center py-4 mt-8 shadow-sm" :class="navClass">
      &copy; 2025 PSoC - Platform for Season of Commits - by Team Askk for FOSS
    </footer>
  </div>
</template>

<script>
export default {
  data() {
    return {
      theme: "light",
      searchQuery: "",
      selectedDomain: "",
      minProjects: "",
      minYears: "",
      organizations: [
        { id: 1, name: "AI Innovators", domain: "AI", about: "Pioneering AI Research", projects: 12, years: 5, website: "#", github: "#", linkedin: "#" },
        { id: 2, name: "Blockchain Builders", domain: "Blockchain", about: "Decentralized Solutions", projects: 8, years: 4, website: "#", github: "#", linkedin: "#" },
        { id: 3, name: "CyberSec Defenders", domain: "Cybersecurity", about: "Protecting Digital Assets", projects: 6, years: 3, website: "#", github: "#", linkedin: "#" },
        { id: 4, name: "Quantum Leap", domain: "Quantum Computing", about: "Exploring Quantum Tech", projects: 5, years: 2, website: "#", github: "#", linkedin: "#" },
        { id: 5, name: "EcoTech Solutions", domain: "Sustainability", about: "Green Tech Innovations", projects: 7, years: 4, website: "#", github: "#", linkedin: "#" },
        { id: 6, name: "MedTech Pioneers", domain: "Healthcare", about: "AI in Medicine", projects: 9, years: 5, website: "#", github: "#", linkedin: "#" },
        { id: 7, name: "EduFuture", domain: "EdTech", about: "Revolutionizing Learning", projects: 11, years: 6, website: "#", github: "#", linkedin: "#" },
        { id: 8, name: "FinTech Gurus", domain: "Finance", about: "Modernizing Payments", projects: 10, years: 4, website: "#", github: "#", linkedin: "#" },
        { id: 9, name: "RoboWorks", domain: "Robotics", about: "Building Next-Gen Robots", projects: 8, years: 3, website: "#", github: "#", linkedin: "#" },
        { id: 10, name: "Cloud Nexus", domain: "Cloud Computing", about: "Scalable Cloud Solutions", projects: 13, years: 7, website: "#", github: "#", linkedin: "#" },
        { id: 11, name: "NeuralNet Labs", domain: "AI", about: "Deep Learning Research", projects: 14, years: 5, website: "#", github: "#", linkedin: "#" },
        { id: 12, name: "Open Source Hub", domain: "Open Source", about: "Collaborative Development", projects: 20, years: 8, website: "#", github: "#", linkedin: "#" },
        { id: 13, name: "AgriTech Innovations", domain: "Agriculture", about: "Smart Farming", projects: 6, years: 3, website: "#", github: "#", linkedin: "#" },
        { id: 14, name: "Space Explorers", domain: "Aerospace", about: "AI in Space Tech", projects: 4, years: 2, website: "#", github: "#", linkedin: "#" },
        { id: 15, name: "IoT Masters", domain: "IoT", about: "Connected Devices", projects: 9, years: 5, website: "#", github: "#", linkedin: "#" },
        { id: 16, name: "VR Visionaries", domain: "Virtual Reality", about: "Immersive Experiences", projects: 7, years: 4, website: "#", github: "#", linkedin: "#" },
        { id: 17, name: "Data Science Club", domain: "Data Science", about: "Advanced Analytics", projects: 10, years: 6, website: "#", github: "#", linkedin: "#" },
        { id: 18, name: "Smart Cities Initiative", domain: "Urban Tech", about: "Tech for Urban Development", projects: 5, years: 3, website: "#", github: "#", linkedin: "#" }
      ]
    };
  },
  computed: {
    themeClass() {
      return this.theme === "light" ? "bg-light-background text-light-text" : "bg-dark-background text-dark-text";
    },
    navClass() {
      return this.theme === "light" ? "bg-light-navBackground text-light-navText" : "bg-dark-navBackground text-dark-navText";
    },
    linkClass() {
      return this.theme === "light" ? "text-light-link" : "text-dark-link";
    },
    buttonClass() {
      return this.theme === "light" ? "bg-light-buttonBackground text-light-buttonText" : "bg-dark-buttonBackground text-dark-buttonText";
    },
    cardClass() {
      return this.theme === "light" ? "bg-light-cardBackground text-light-text" : "bg-dark-cardBackground text-dark-text";
    },
    uniqueDomains() {
      return [...new Set(this.organizations.map(org => org.domain))];
    },
    filteredOrganizations() {
      return this.organizations.filter(org =>
        (!this.searchQuery || org.name.toLowerCase().includes(this.searchQuery.toLowerCase())) &&
        (!this.selectedDomain || org.domain === this.selectedDomain) &&
        (!this.minProjects || org.projects >= this.minProjects) &&
        (!this.minYears || org.years >= this.minYears)
      );
    }
  },
  methods: {
    toggleTheme() {
      this.theme = this.theme === "light" ? "dark" : "light";
      localStorage.setItem("theme", this.theme);
    }
  },
  created() {
    this.theme = localStorage.getItem("theme") || "light";
  }
};
</script>
