<template>
  <div :class="themeClass" class="min-h-screen flex flex-col transition-colors duration-300">
    <Navbar :theme="theme" :isLoggedIn="isLoggedIn" @toggle-theme="toggleTheme"/>
    
    <!-- Main content container with flex-grow to fill available space -->
    <div class="flex-grow flex items-center justify-center">
      <div class="w-full max-w-md p-8 rounded-xl shadow-lg hover:shadow-2xl transition" :class="cardClass">
        <h2 class="text-3xl font-bold text-center mb-6">Create a New Account</h2>
        
        <form @submit.prevent="handleRegister" class="space-y-4">
          <div>
            <label class="block text-lg font-medium mb-1">User Type</label>
            <select v-model="userType" class="w-full px-4 py-2 rounded-lg border focus:outline-none focus:ring-2 transition" :class="inputClass">
              <option value="mentor">Mentor</option>
              <option value="contributor">Contributor</option>
              <option value="organization">Organization</option>
            </select>
          </div>

          <div>
            <label class="block text-lg font-medium mb-1" for="name">Full Name</label>
            <input type="text" id="name" v-model="name" required class="w-full px-4 py-2 rounded-lg border focus:outline-none focus:ring-2 transition" :class="inputClass" />
          </div>

          <div v-if="userType === 'organization'">
            <label class="block text-lg font-medium mb-1" for="orgName">Organization Name</label>
            <input type="text" id="orgName" v-model="orgName" required class="w-full px-4 py-2 rounded-lg border focus:outline-none focus:ring-2 transition" :class="inputClass" />
          </div>

          <div>
            <label class="block text-lg font-medium mb-1" for="email">Email</label>
            <input type="email" id="email" v-model="email" required class="w-full px-4 py-2 rounded-lg border focus:outline-none focus:ring-2 transition" :class="inputClass" />
          </div>

          <div>
            <label class="block text-lg font-medium mb-1" for="password">Password</label>
            <input type="password" id="password" v-model="password" required class="w-full px-4 py-2 rounded-lg border focus:outline-none focus:ring-2 transition" :class="inputClass" />
          </div>

          <div v-if="userType === 'mentor'">
            <label class="block text-lg font-medium mb-1" for="expertise">Expertise Area</label>
            <input type="text" id="expertise" v-model="expertise" required class="w-full px-4 py-2 rounded-lg border focus:outline-none focus:ring-2 transition" :class="inputClass" />
          </div>

          <div v-if="userType === 'contributor'">
            <label class="block text-lg font-medium mb-1" for="skills">Skills</label>
            <input type="text" id="skills" v-model="skills" required class="w-full px-4 py-2 rounded-lg border focus:outline-none focus:ring-2 transition" :class="inputClass" />
          </div>

          <button type="submit" class="w-full py-3 rounded-lg shadow transition text-xl font-semibold" :class="buttonClass">
            Register
          </button>
        </form>
      </div>
    </div>

    <!-- Footer stays at the bottom -->
    <Footer :theme="theme" />
  </div>
</template>

<script setup>
import Navbar from '@/components/Navbar.vue';
import Footer from '@/components/Footer.vue';
import { ref, computed, onMounted } from 'vue';

const theme = ref(localStorage.getItem("theme") || "light");
const isLoggedIn=false;
const userType = ref("mentor");
const name = ref("");
const orgName = ref("");
const email = ref("");
const password = ref("");
const expertise = ref("");
const skills = ref("");
const themeClass = computed(() => theme.value === "light" ? "bg-light-background text-light-text" : "bg-dark-background text-dark-text");
const navClass = computed(() => theme.value === "light" ? "bg-light-navBackground text-light-navText" : "bg-dark-navBackground text-dark-navText");
const buttonClass = computed(() => theme.value === "light" ? "bg-light-buttonBackground text-light-buttonText border" : "bg-dark-buttonBackground text-dark-buttonText border");
const cardClass = computed(() => theme.value === "light" ? "bg-light-cardBackground text-light-text" : "bg-dark-cardBackground text-dark-text");
const submitButtonClass = computed(() => theme.value === "light" ? "bg-light-buttonBackground text-light-buttonText shadow-lg" : "bg-dark-buttonBackground text-dark-buttonText shadow-lg");

const toggleTheme = () => {
  theme.value = theme.value === "light" ? "dark" : "light";
  localStorage.setItem("theme", theme.value);
  document.documentElement.classList.toggle("dark", theme.value === "dark");
};
const  handleRegister=()=> {
      alert(`Registered as ${this.userType}: ${this.name}`);
    }
onMounted(() => {
  document.documentElement.classList.toggle("dark", theme.value === "dark");
});

</script>
