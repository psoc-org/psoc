<template>
  <div :class="themeClass" class="min-h-screen flex flex-col transition-colors duration-300">
    <Navbar :theme="theme" :isLoggedIn="isLoggedIn" @toggle-theme="toggleTheme"/>
    
    <!-- Main content container with flex-grow to fill available space -->
    <div class="flex-grow flex items-center justify-center">
    <div class="min-h-screen flex justify-center items-center p-12 mt-12">
      <div :class="cardClass" class="w-full max-w-4xl mx-auto p-12 shadow-2xl  rounded-xl">
        <div class="text-center mb-12">
          <h2 class="text-3xl font-extrabold text-accent drop-shadow-lg">{{ proposal.projectName }}</h2>
          <p class="text-secondary text-lg mt-4 leading-relaxed">{{ proposal.projectDescription }}</p>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
          <div :class="glassCardClass">
            <h4 class="text-2xl mb-2 font-semibold">Organization</h4>
            <p>{{ proposal.organization }}</p>
          </div>
          <div :class="glassCardClass">
            <h4 class="text-2xl mb-2 font-semibold">Project Goals</h4>
            <p>{{ proposal.projectGoals }}</p>
          </div>
          <div :class="glassCardClass" class="col-span-2">
            <h4 class="text-2xl mb-2 font-semibold">Expected Deliverables</h4>
            <p>{{ proposal.deliverables }}</p>
          </div>
          <div :class="glassCardClass">
            <h4 class="text-2xl mb-2 font-semibold">Timeline</h4>
            <p>{{ proposal.timeline }}</p>
          </div>
          <div :class="glassCardClass">
            <h4 class="text-2xl mb-2 font-semibold">Contact Person</h4>
            <p>{{ proposal.contactPerson }}</p>
          </div>
          <div :class="glassCardClass" class="col-span-2">
            <h4 class="text-2xl mb-2 font-semibold">Contact Email</h4>
            <p>{{ proposal.contactEmail }}</p>
          </div>
        </div>
        <div class="mt-12 flex justify-center">
          <a :href="proposal.downloadLink" :class="downloadButtonClass" class="text-xl font-semibold py-3 px-6 rounded-xl transition-transform transform hover:scale-105 shadow-lg">
            Download Full Proposal
          </a>
        </div>
      </div>
    </div>
    </div>
    <Footer :theme="theme" />
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';
import Navbar from '@/components/Navbar.vue';
import Footer from '@/components/Footer.vue';
const theme = ref(localStorage.getItem("theme") || "light");
const themeClass = computed(() => theme.value === "light" ? "bg-light-background text-light-text" : "bg-dark-background text-dark-text");
const navClass = computed(() => theme.value === "light" ? "bg-light-navBackground text-light-navText" : "bg-dark-navBackground text-dark-navText");
const buttonClass = computed(() => theme.value === "light" ? "bg-light-buttonBackground text-light-buttonText border border-light-text" : "bg-dark-buttonBackground text-dark-buttonText border border-dark-text");
const cardClass = computed(() => theme.value === "light" ? "bg-light-cardBackground text-light-text border-light-text" : "bg-dark-cardBackground text-dark-text border-dark-text ");
const glassCardClass = computed(() => theme.value === "light" ? "bg-light-cardBackground text-light-text shadow-lg p-6 rounded-xl border border-light-text" : "bg-dark-cardBackground text-dark-text shadow-lg p-6 rounded-xl border border-dark-text");
const downloadButtonClass = computed(() => theme.value === "light" ? "bg-light-buttonBackground text-light-buttonText" : "bg-dark-buttonBackground text-dark-buttonText");

const proposal = ref({
  projectName: "EventHive",
  projectDescription: "A collaborative event organizer platform where users can create, manage and participate in events.",
  organization: "Open Source Org",
  projectGoals: "Create a platform that supports seamless event creation, collaboration, and management. Include features like to-do lists, calendar integrations, and real-time chat.",
  deliverables: "Working platform with basic event creation features, user management, and real-time chat functionality.",
  timeline: "6 months, divided into sprints for each feature. First sprint focuses on authentication and basic UI.",
  contactPerson: "John Doe",
  contactEmail: "contact@opensourceorg.com",
  downloadLink: "https://example.com/full-proposal.pdf"
});

const toggleTheme = () => {
  theme.value = theme.value === "light" ? "dark" : "light";
  localStorage.setItem("theme", theme.value);
  document.documentElement.classList.toggle("dark", theme.value === "dark");
};

onMounted(() => {
  document.documentElement.classList.toggle("dark", theme.value === "dark");
});
</script>

<style scoped>
.glass-card h4 {
  font-size: 1.5rem;
  font-weight: bold;
  color: var(--accent-color, #5FFF16);
}
.glass-card p {
  margin-top: 8px;
  font-size: 1.1rem;
  line-height: 1.6;
}
.download-button {
  display: inline-block;
  padding: 14px 28px;
  font-size: 1.2rem;
  font-weight: bold;
  border-radius: 10px;
  transition: all 0.3s ease;
  text-align: center;
}
.download-button:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 16px rgba(0, 255, 0, 0.5);
}
</style>