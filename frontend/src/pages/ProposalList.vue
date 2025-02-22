<template>
  <nav :class="navClass" class="w-full py-4 px-8 flex items-center justify-between fixed top-0 left-0 right-0 z-50 shadow">
    <router-link to="/" class="text-3xl font-extrabold cursor-pointer">PSoC</router-link>

    <button @click="toggleTheme" :class="buttonClass" class="px-4 py-2 rounded-lg transition">
      {{ theme === 'light' ? '🌙 Dark Mode' : '☀️ Light Mode' }}
    </button>
  </nav>
  <div :class="themeClass" class="min-h-screen flex flex-col items-center p-10">
    <h1 :class="linkClass" class="text-3xl font-bold mb-8">Project Proposals</h1>

    <div class="w-full max-w-5xl space-y-6">
      <div 
        v-for="proposal in proposals" 
        :key="proposal.id" 
        :class="cardClass"
        class="cursor-pointer p-6 rounded-lg border shadow-lg hover:shadow-2xl transform transition-all duration-300 hover:scale-105"
      >
        <div class="flex justify-between mb-4">
          <div>
            <p class="text-sm font-semibold">Contributor</p>
            <p class="text-xl font-bold">&lt;{{ proposal.contributor }}&gt;</p>
          </div>
          <div>
            <p class="text-sm font-semibold">Mentor</p>
            <p>{{ proposal.mentor }}</p>
          </div>
          <div>
            <p class="text-sm font-semibold">Organization</p>
            <p>{{ proposal.organization }}</p>
          </div>
        </div>

        <h2 class="text-2xl font-semibold mb-2">{{ proposal.title }}</h2>
        <p>{{ proposal.description }}</p>

        <div class="mt-4 flex space-x-4">
          <button 
            @click="viewProposal(proposal.id)" 
            :class="codeButtonClass"
            class="px-4 py-2 border rounded-lg transition"
          >
            View project details
          </button>
          <button 
            :class="codeButtonClass"
            class="px-4 py-2 border rounded-lg transition"
          >
            View code
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();
const theme = ref(localStorage.getItem("theme") || "light");

const themeClass = computed(() => theme.value === "light" ? "bg-light-background text-light-text" : "bg-dark-background text-dark-text");
const navClass = computed(() => theme.value === "light" ? "bg-light-navBackground text-light-navText" : "bg-dark-navBackground text-dark-navText");
const linkClass = computed(() => theme.value === "light" ? "text-light-link" : "text-dark-link");
const buttonClass = computed(() => theme.value === "light" ? "bg-light-buttonBackground text-light-buttonText border border-gray-300" : "bg-dark-buttonBackground text-dark-buttonText border border-gray-600");
const cardClass = computed(() => theme.value === "light" ? "bg-light-cardBackground text-light-text border-light-border" : "bg-dark-cardBackground text-dark-text border-dark-border");
const viewButtonClass = computed(() => theme.value === "light" ? "bg-light-buttonBackground text-light-buttonText hover:bg-light-buttonHover" : "bg-dark-buttonBackground text-dark-buttonText hover:bg-dark-buttonHover");
const codeButtonClass = computed(() => theme.value === "light" ? "border-light-buttonBackground text-light-text hover:bg-light-buttonBackground hover:text-light-buttonText" : "border-dark-buttonBackground text-dark-text hover:bg-dark-buttonBackground hover:text-dark-buttonText");

const proposals = ref([
  { 
    id: 1, 
    title: "(MSS) msui: Improve MSUI", 
    contributor: "Aryan Gupta", 
    mentor: "JoernU76, Reimar Bauer, Matthias Rieß", 
    organization: "Python Software Foundation", 
    description: "The project aims to significantly enhance the user interface of the Mission Support System (MSS) - MSUI by implementing a comprehensive set of improvements."
  },
  { 
    id: 2, 
    title: "AI-Powered Chatbot", 
    contributor: "Alice Johnson", 
    mentor: "Dr. Watson", 
    organization: "OpenAI", 
    description: "Developing an AI-powered chatbot that understands natural language and provides intelligent responses using GPT models."
  }
]);

const viewProposal = (id) => {
  router.push(`/proposal/details/${id}`);
};
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
div:hover {
  transition: all 0.3s ease-in-out;
}
</style>
