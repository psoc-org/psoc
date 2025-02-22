<template>
  <div :class="themeClass" class="min-h-screen flex items-center justify-center px-6 transition-colors duration-300">
    <!-- Navbar -->
    <nav :class="navClass" class="w-full py-4 px-8 flex items-center justify-between fixed top-0 left-0 right-0 z-50 shadow">
      <h1 class="text-3xl font-extrabold">PSoC</h1>

      <!-- Center-aligned Navigation Links -->
      <div class="absolute left-1/2 transform -translate-x-1/2 flex space-x-6">
        <router-link to="/" :class="linkClass" class="font-medium hover:opacity-75">Home</router-link>
        <router-link to="/about" :class="linkClass" class="font-medium hover:opacity-75">About</router-link>
        <router-link to="/vieworganizations" :class="linkClass" class="font-medium hover:opacity-75">View Organizations</router-link>
        <router-link to="/viewprojects" :class="linkClass" class="font-medium hover:opacity-75">View Projects</router-link>
        <router-link to="/contributors" :class="linkClass" class="font-medium hover:opacity-75">Contributors</router-link>
        <router-link to="/mentors" :class="linkClass" class="font-medium hover:opacity-75">Mentors</router-link>
        <router-link to="/organizers" :class="linkClass" class="font-medium hover:opacity-75">Organizers</router-link>
      </div>

      <!-- Theme Toggle Button -->
      <button @click="toggleTheme" :class="buttonClass" class="px-4 py-2 rounded-lg transition">
        {{ theme === "light" ? '🌙 Dark Mode' : '☀️ Light Mode' }}
      </button>
    </nav>
    
    <div class="w-full max-w-md p-8 rounded-xl shadow-lg hover:shadow-2xl transition" :class="cardClass">
      <h2 class="text-3xl font-bold text-center mb-6">Login to PSoC</h2>
      
      <form @submit.prevent="handleLogin" class="space-y-4">
        <div>
          <label class="block text-lg font-medium mb-1" for="email">Email</label>
          <input 
            type="email" 
            id="email" 
            v-model="email" 
            required 
            class="w-full px-4 py-2 rounded-lg border focus:outline-none focus:ring-2 transition" 
            :class="inputClass"
          />
        </div>
        
        <div>
          <label class="block text-lg font-medium mb-1" for="password">Password</label>
          <input 
            type="password" 
            id="password" 
            v-model="password" 
            required 
            class="w-full px-4 py-2 rounded-lg border focus:outline-none focus:ring-2 transition" 
            :class="inputClass"
          />
        </div>

        <div class="flex justify-between text-sm mt-2">
          <router-link to="/forgot-password" class="hover:underline" :class="linkClass">Forgot Password?</router-link>
          <router-link to="/#apply" class="hover:underline" :class="linkClass">Create a New Account</router-link>
        </div>
        
        <button 
          type="submit" 
          class="w-full py-3 rounded-lg shadow transition text-xl font-semibold" 
          :class="buttonClass"
        >
          Login
        </button>
      </form>
    </div>
  </div>
</template>

<script>

import { session } from '@/data/session' // ✅ Import session to use `isLoggedIn`
export default {
  data() {
    return {
      theme: "light",
      email: "",
      password: ""
    };
  },
  computed: {
    themeClass() {
      return this.theme === "light" ? "bg-light-background text-light-text" : "bg-dark-background text-dark-text";
    },
    cardClass() {
      return this.theme === "light" ? "bg-light-cardBackground text-light-text" : "bg-dark-cardBackground text-dark-text";
    },
    buttonClass() {
      return this.theme === "light" ? "bg-light-buttonBackground text-light-buttonText" : "bg-dark-buttonBackground text-dark-buttonText";
    },
    linkClass() {
      return this.theme === "light" ? "text-light-link" : "text-dark-link";
    },
    inputClass() {
      return this.theme === "light" ? "border-gray-300 focus:ring-light-accent" : "border-gray-600 focus:ring-dark-accent";
    }
  },
  methods: {
    handleLogin() {
      alert(`Logging in as: ${this.email}`);
    },
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
