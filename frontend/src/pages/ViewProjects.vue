<template>
  <div :class="themeClass" class="min-h-screen transition-colors duration-300">
    
    <!-- Navbar -->
    <nav :class="navClass" class="w-full py-4 px-8 flex items-center justify-between fixed top-0 left-0 right-0 z-50 shadow">
      <router-link to="/" class="text-3xl font-extrabold cursor-pointer">PSoC</router-link>
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
      <h2 class="text-4xl font-bold">View Projects</h2>
      <p class="text-lg mt-2">Explore projects under different organizations in PSoC</p>
    </header>

    <!-- Filters Section -->
    <section class="p-6 flex flex-wrap gap-4 justify-center">
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
    <section class="grid md:grid-cols-3 gap-6 px-12">
      <div v-for="project in filteredProjects" :key="project.id" class="p-6 rounded-lg shadow-md hover:shadow-lg transition" :class="cardClass">
        <h3 class="text-2xl font-semibold">{{ project.name }}</h3>
        <p class="text-sm mt-1"><b>Organization:</b> {{ project.organization }}</p>
        <p class="text-sm"><b>Domain:</b> {{ project.domain }}</p>
        <p class="text-sm"><b>Description:</b> {{ project.description }}</p>
        <div class="mt-4 flex space-x-3">
          <a v-if="project.github" :href="project.github" target="_blank" class="text-blue-500 hover:underline">GitHub</a>
        </div>
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
      selectedOrg: "",
      projects: [
        { "id": 1, "name": "AI Chatbot", "organization": "AI Innovators", "domain": "AI", "description": "Building an intelligent chatbot for customer support.", "github": "#" },
        { "id": 2, "name": "Neural Art Generator", "organization": "AI Innovators", "domain": "AI", "description": "An AI-based image style transfer system.", "github": "#" },
        { "id": 3, "name": "Decentralized Voting", "organization": "Blockchain Builders", "domain": "Blockchain", "description": "Secure blockchain-based voting system.", "github": "#" },
        { "id": 4, "name": "Crypto Wallet Security", "organization": "Blockchain Builders", "domain": "Blockchain", "description": "Enhancing security in crypto transactions.", "github": "#" },
        { "id": 5, "name": "CyberShield", "organization": "CyberSec Defenders", "domain": "Cybersecurity", "description": "Advanced threat detection system.", "github": "#" },
        { "id": 6, "name": "IoT Security Suite", "organization": "CyberSec Defenders", "domain": "Cybersecurity", "description": "Security solutions for IoT networks.", "github": "#" },
        { "id": 7, "name": "Quantum Compiler", "organization": "Quantum Leap", "domain": "Quantum Computing", "description": "Compiler for quantum algorithms.", "github": "#" },
        { "id": 8, "name": "Quantum Key Distribution", "organization": "Quantum Leap", "domain": "Quantum Computing", "description": "Quantum encryption for secure communication.", "github": "#" },
        { "id": 9, "name": "Green Energy Grid", "organization": "EcoTech Solutions", "domain": "Sustainability", "description": "Optimizing energy distribution.", "github": "#" },
        { "id": 10, "name": "Carbon Footprint Tracker", "organization": "EcoTech Solutions", "domain": "Sustainability", "description": "Tracking and reducing carbon footprints.", "github": "#" },
        { "id": 11, "name": "AI Medical Diagnosis", "organization": "MedTech Pioneers", "domain": "Healthcare", "description": "AI-powered medical diagnostics.", "github": "#" },
        { "id": 12, "name": "Wearable Health Monitor", "organization": "MedTech Pioneers", "domain": "Healthcare", "description": "A smart device for real-time health tracking.", "github": "#" },
        { "id": 13, "name": "Smart Learning System", "organization": "EduFuture", "domain": "EdTech", "description": "Personalized learning platform.", "github": "#" },
        { "id": 14, "name": "AI Tutor", "organization": "EduFuture", "domain": "EdTech", "description": "An AI-powered tutor for students.", "github": "#" },
        { "id": 15, "name": "AI Stock Predictor", "organization": "FinTech Gurus", "domain": "Finance", "description": "Predicting stock market trends using AI.", "github": "#" },
        { "id": 16, "name": "Blockchain Payments", "organization": "FinTech Gurus", "domain": "Finance", "description": "Secure and transparent payment system.", "github": "#" },
        { "id": 17, "name": "Autonomous Delivery Robot", "organization": "RoboWorks", "domain": "Robotics", "description": "AI-powered robotic delivery system.", "github": "#" },
        { "id": 18, "name": "Industrial Automation AI", "organization": "RoboWorks", "domain": "Robotics", "description": "AI-based automation for factories.", "github": "#" },
        { "id": 19, "name": "Serverless Cloud Manager", "organization": "Cloud Nexus", "domain": "Cloud Computing", "description": "Automating serverless cloud management.", "github": "#" },
        { "id": 20, "name": "Multi-Cloud Backup", "organization": "Cloud Nexus", "domain": "Cloud Computing", "description": "Secure data backup across cloud providers.", "github": "#" },
        { "id": 21, "name": "Deep Learning Framework", "organization": "NeuralNet Labs", "domain": "AI", "description": "Custom framework for deep learning research.", "github": "#" },
        { "id": 22, "name": "AI-Powered Video Editing", "organization": "NeuralNet Labs", "domain": "AI", "description": "AI-driven video editing automation.", "github": "#" },
        { "id": 23, "name": "FOSS Collaboration Platform", "organization": "Open Source Hub", "domain": "Open Source", "description": "A collaborative platform for open-source development.", "github": "#" },
        { "id": 24, "name": "Open Source Analytics", "organization": "Open Source Hub", "domain": "Open Source", "description": "Insights and analytics for FOSS contributions.", "github": "#" },
        { "id": 25, "name": "IoT Smart Farming", "organization": "AgriTech Innovations", "domain": "Agriculture", "description": "IoT-enabled precision agriculture system.", "github": "#" },
        { "id": 26, "name": "Crop Yield Prediction", "organization": "AgriTech Innovations", "domain": "Agriculture", "description": "Predicting farm yield using AI.", "github": "#" },
        { "id": 27, "name": "Satellite Image Processing", "organization": "Space Explorers", "domain": "Aerospace", "description": "Analyzing space images with AI.", "github": "#" },
        { "id": 28, "name": "Orbital Traffic Management", "organization": "Space Explorers", "domain": "Aerospace", "description": "Managing satellite traffic in space.", "github": "#" },
        { "id": 29, "name": "IoT Smart Home", "organization": "IoT Masters", "domain": "IoT", "description": "Home automation using IoT devices.", "github": "#" },
        { "id": 30, "name": "Industrial IoT Monitoring", "organization": "IoT Masters", "domain": "IoT", "description": "Real-time monitoring of industrial equipment.", "github": "#" },
        { "id": 31, "name": "VR Learning Platform", "organization": "VR Visionaries", "domain": "Virtual Reality", "description": "Immersive learning experiences using VR.", "github": "#" },
        { "id": 32, "name": "VR Medical Training", "organization": "VR Visionaries", "domain": "Virtual Reality", "description": "Medical training simulations in VR.", "github": "#" },
        { "id": 33, "name": "AI-Based Data Insights", "organization": "Data Science Club", "domain": "Data Science", "description": "Generating business insights using AI.", "github": "#" },
        { "id": 34, "name": "Automated Data Cleaning", "organization": "Data Science Club", "domain": "Data Science", "description": "A tool for cleaning and preprocessing datasets.", "github": "#" },
        { "id": 35, "name": "Smart Traffic Analytics", "organization": "Smart Cities Initiative", "domain": "Urban Tech", "description": "Using AI to improve urban traffic flow.", "github": "#" },
        { "id": 36, "name": "AI-Powered Waste Management", "organization": "Smart Cities Initiative", "domain": "Urban Tech", "description": "Smart waste sorting and collection system.", "github": "#" },
        { "id": 37, "name": "AI-Powered Resume Scanner", "organization": "AI Innovators", "domain": "AI", "description": "Analyzing resumes with AI.", "github": "#" },
        { "id": 38, "name": "Blockchain Digital Identity", "organization": "Blockchain Builders", "domain": "Blockchain", "description": "Decentralized identity verification.", "github": "#" },
        { "id": 39, "name": "Cybersecurity AI Assistant", "organization": "CyberSec Defenders", "domain": "Cybersecurity", "description": "AI-based security threat detection.", "github": "#" },
        { "id": 40, "name": "IoT Smart Water Management", "organization": "IoT Masters", "domain": "IoT", "description": "Real-time water usage tracking.", "github": "#" }
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
      return [...new Set(this.projects.map(proj => proj.domain))];
    },
    uniqueOrganizations() {
      return [...new Set(this.projects.map(proj => proj.organization))];
    },
    filteredProjects() {
      return this.projects.filter(proj =>
        (!this.searchQuery || proj.name.toLowerCase().includes(this.searchQuery.toLowerCase())) &&
        (!this.selectedDomain || proj.domain === this.selectedDomain) &&
        (!this.selectedOrg || proj.organization === this.selectedOrg)
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