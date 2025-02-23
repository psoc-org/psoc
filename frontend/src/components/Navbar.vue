<template>
	<nav
	  :class="navClass"
	  class="w-full py-4 px-8 flex items-center justify-between fixed top-0 left-0 right-0 z-50 shadow"
	>
	  <router-link to="/" class="text-3xl font-extrabold cursor-pointer">PSoC</router-link>
  
	  <div class="absolute left-1/2 transform -translate-x-1/2 flex space-x-6">
		<router-link
		  v-if="!isLoggedIn && !isLogin"
		  to="/login"
		  :class="linkClass"
		  class="font-medium hover:opacity-75"
		>Login</router-link>
		<router-link
		  v-if="isLoggedIn && !isLogin"
		  :to="profileRoute"
		  :class="linkClass"
		  class="font-medium hover:opacity-75"
		>Profile</router-link>
		<router-link
		  to="/"
		  :class="linkClass"
		  class="font-medium hover:opacity-75"
		  v-if="!isLogin"
		>Home</router-link>
		<router-link
		  to="/about"
		  :class="linkClass"
		  class="font-medium hover:opacity-75"
		  v-if="!isLogin"
		>About</router-link>
		<router-link
		  v-if="!isLogin"
		  to="/vieworganizations"
		  :class="linkClass"
		  class="font-medium hover:opacity-75"
		>View Organizations</router-link>
		<router-link
		  to="/viewprojects"
		  :class="linkClass"
		  class="font-medium hover:opacity-75"
		  v-if="!isLogin"
		>View Projects</router-link>
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
	  isLoggedIn: Boolean,
	  isLogin: Boolean,
	},
	computed: {
	  navClass() {
		return this.theme === 'light'
		  ? 'bg-light-navBackground text-light-navText'
		  : 'bg-dark-navBackground text-dark-navText'
	  },
	  linkClass() {
		return this.theme === 'light' ? 'text-light-link' : 'text-dark-link'
	  },
	  buttonClass() {
		return this.theme === 'light'
		  ? 'bg-light-buttonBackground text-light-buttonText'
		  : 'bg-dark-buttonBackground text-dark-buttonText'
	  },
	  profileRoute() {
		const userRole = localStorage.getItem('userRole')
		return userRole === 'Organizer' ? '/organization/profile' : '/profile'
	  }
	},
	methods: {
	  toggleTheme() {
		this.$emit('toggle-theme')
	  },
	},
  }
  </script>