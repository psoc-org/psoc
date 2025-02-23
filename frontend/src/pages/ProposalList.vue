<template>
  <div :class="themeClass" class="min-h-screen flex flex-col transition-colors duration-300">
    <Navbar :theme="theme" :isLoggedIn="isLoggedIn" @toggle-theme="toggleTheme"/>
    
    <div class="flex-grow flex items-center justify-center">
      <div class="w-full max-w-5xl space-y-6">
        <h1 :class="linkClass" class="text-3xl font-bold mb-8 mt-20 ml-[40%]">Project Proposals</h1>
        <div 
          v-for="proposal in proposals" 
          :key="proposal.id" 
          :class="cardClass"
          class="p-6 rounded-lg border shadow-lg hover:shadow-2xl transform transition-all duration-300"
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
            <div class="flex flex-col items-end gap-2">
              <!-- Status Badge -->
              <div 
                :class="[
                  'px-3 py-1 rounded-full text-sm font-medium',
                  getStatusClass(proposal.status)
                ]"
              >
                {{ proposal.status }}
              </div>
              <!-- Edit Status Button -->
              <button
                @click="openStatusModal(proposal)"
                :class="editButtonClass"
                class="text-sm px-3 py-1 rounded-lg transition-colors duration-200"
              >
                Edit Status
              </button>
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

    <!-- Status Edit Modal -->
    <div v-if="showStatusModal" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
      <div 
        :class="modalClass"
        class="p-6 rounded-lg shadow-xl max-w-md w-full"
      >
        <h3 class="text-xl font-bold mb-4">Update Proposal Status</h3>
        <div class="space-y-4">
          <button
            v-for="status in ['Pending', 'Accepted', 'Declined']"
            :key="status"
            @click="updateStatus(status.toLowerCase())"
            :class="[
              'w-full py-2 px-4 rounded-lg transition-colors duration-200',
              selectedProposal?.status === status.toLowerCase()
                ? getStatusButtonClass(status.toLowerCase())
                : 'bg-gray-200 dark:bg-gray-700'
            ]"
          >
            {{ status }}
          </button>
        </div>
        <div class="mt-6 flex justify-end gap-4">
          <button
            @click="closeStatusModal"
            :class="codeButtonClass"
            class="px-4 py-2 rounded-lg"
          >
            Close
          </button>
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
import { useRouter } from 'vue-router';

const router = useRouter();
const theme = ref(localStorage.getItem("theme") || "light");
const showStatusModal = ref(false);
const selectedProposal = ref(null);

const themeClass = computed(() => theme.value === "light" ? "bg-light-background text-light-text" : "bg-dark-background text-dark-text");
const navClass = computed(() => theme.value === "light" ? "bg-light-navBackground text-light-navText" : "bg-dark-navBackground text-dark-navText");
const linkClass = computed(() => theme.value === "light" ? "text-light-link" : "text-dark-link");
const buttonClass = computed(() => theme.value === "light" ? "bg-light-buttonBackground text-light-buttonText border border-gray-300" : "bg-dark-buttonBackground text-dark-buttonText border border-gray-600");
const cardClass = computed(() => theme.value === "light" ? "bg-light-cardBackground text-light-text border-light-border" : "bg-dark-cardBackground text-dark-text border-dark-border");
const modalClass = computed(() => theme.value === "light" ? "bg-white text-gray-900" : "bg-gray-800 text-gray-100");
const viewButtonClass = computed(() => theme.value === "light" ? "bg-light-buttonBackground text-light-buttonText hover:bg-light-buttonHover" : "bg-dark-buttonBackground text-dark-buttonText hover:bg-dark-buttonHover");
const codeButtonClass = computed(() => theme.value === "light" ? "border-light-buttonBackground text-light-text hover:bg-light-buttonBackground hover:text-light-buttonText" : "border-dark-buttonBackground text-dark-text hover:bg-dark-buttonBackground hover:text-dark-buttonText");
const editButtonClass = computed(() => theme.value === "light" ? "bg-gray-100 text-gray-600 hover:bg-gray-200" : "bg-gray-700 text-gray-300 hover:bg-gray-600");

const proposals = ref([
  { 
    id: 1, 
    title: "(MSS) msui: Improve MSUI", 
    contributor: "Aryan Gupta", 
    mentor: "JoernU76, Reimar Bauer, Matthias Rieß", 
    organization: "Python Software Foundation", 
    description: "The project aims to significantly enhance the user interface of the Mission Support System (MSS) - MSUI by implementing a comprehensive set of improvements.",
    status: "pending"
  },
  { 
    id: 2, 
    title: "AI-Powered Chatbot", 
    contributor: "Alice Johnson", 
    mentor: "Dr. Watson", 
    organization: "OpenAI", 
    description: "Developing an AI-powered chatbot that understands natural language and provides intelligent responses using GPT models.",
    status: "pending"
  }
]);

const getStatusClass = (status) => {
  const classes = {
    pending: theme.value === "light" 
      ? "bg-yellow-100 text-yellow-800" 
      : "bg-yellow-900 text-yellow-100",
    accepted: theme.value === "light" 
      ? "bg-green-100 text-green-800" 
      : "bg-green-900 text-green-100",
    declined: theme.value === "light" 
      ? "bg-red-100 text-red-800" 
      : "bg-red-900 text-red-100"
  };
  return classes[status] || classes.pending;
};

const getStatusButtonClass = (status) => {
  const classes = {
    pending: "bg-yellow-500 text-white",
    accepted: "bg-green-500 text-white",
    declined: "bg-red-500 text-white"
  };
  return classes[status] || classes.pending;
};

const openStatusModal = (proposal) => {
  selectedProposal.value = proposal;
  showStatusModal.value = true;
};

const closeStatusModal = () => {
  showStatusModal.value = false;
  selectedProposal.value = null;
};

const updateStatus = (newStatus) => {
  if (selectedProposal.value) {
    const proposal = proposals.value.find(p => p.id === selectedProposal.value.id);
    if (proposal) {
      proposal.status = newStatus;
    }
  }
  closeStatusModal();
};

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