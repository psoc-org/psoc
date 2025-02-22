<template>
	<nav :class="navClass" class="w-full py-4 px-8 flex items-center justify-between fixed top-0 left-0 right-0 z-50 shadow">
	  <router-link to="/" class="text-3xl font-extrabold cursor-pointer">PSoC</router-link>
	  
	  <div class="absolute left-1/2 transform -translate-x-1/2 flex space-x-6">
		<router-link v-if="!isLoggedIn" to="/login" :class="linkClass" class="font-medium hover:opacity-75">Login</router-link>
		<router-link v-else to="/profile" :class="linkClass" class="font-medium hover:opacity-75">Profile</router-link>
		<router-link to="/about" :class="linkClass" class="font-medium hover:opacity-75">About</router-link>
		<router-link to="/vieworganizations" :class="linkClass" class="font-medium hover:opacity-75">View Organizations</router-link>
		<router-link to="/viewprojects" :class="linkClass" class="font-medium hover:opacity-75">View Projects</router-link>
		<router-link to="/contributors" :class="linkClass" class="font-medium hover:opacity-75">Contributors</router-link>
		<router-link to="/mentors" :class="linkClass" class="font-medium hover:opacity-75">Mentors</router-link>
		<router-link to="/organizers" :class="linkClass" class="font-medium hover:opacity-75">Organizers</router-link>
	  </div>
	  
	  <button @click="toggleTheme" :class="buttonClass" class="px-4 py-2 rounded-lg transition">
		{{ theme === 'light' ? '🌙 Dark Mode' : '☀️ Light Mode' }}
	  </button>
	</nav>
  </template>
  
  <script>
  export default {
	props: {
	  theme: String,
	  isLoggedIn: Boolean
	},
	computed: {
	  navClass() {
		return this.theme === "light" ? "bg-light-navBackground text-light-navText" : "bg-dark-navBackground text-dark-navText";
	  },
	  linkClass() {
		return this.theme === "light" ? "text-light-link" : "text-dark-link";
	  },
	  buttonClass() {
		return this.theme === "light" ? "bg-light-buttonBackground text-light-buttonText" : "bg-dark-buttonBackground text-dark-buttonText";
	  }
	},
	methods: {
	  toggleTheme() {
		this.$emit("toggle-theme");
	  }
	}
  };
  </script>