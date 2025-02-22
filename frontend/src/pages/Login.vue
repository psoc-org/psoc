<template>
	<div :class="themeClass" class="min-h-screen flex flex-col transition-colors duration-300">
		<Navbar
			:theme="theme"
			:isLoggedIn="isLoggedIn"
			@toggle-theme="toggleTheme"
			:isLogin="true"
		/>
		<div class="flex-grow flex items-center justify-center">
			<div
				class="w-full max-w-md p-8 rounded-xl shadow-lg hover:shadow-2xl transition"
				:class="cardClass"
			>
				<h2 class="text-3xl font-bold text-center mb-6">Login to PSoC</h2>

				<form @submit.prevent="loginResource.submit" class="space-y-4">
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
						<label class="block text-lg font-medium mb-1" for="password"
							>Password</label
						>
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
						<router-link
							to="/forgot-password"
							class="hover:underline"
							:class="linkClass"
							>Forgot Password?</router-link
						>
						<router-link to="/#apply" class="hover:underline" :class="linkClass"
							>Create a New Account</router-link
						>
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
		<Footer :theme="theme" />
	</div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { createResource } from 'frappe-ui'

import Navbar from '@/components/Navbar.vue'
import Footer from '@/components/Footer.vue'
import { session } from '@/data/session'

// Reactive state
const theme = ref(localStorage.getItem('theme') || 'light')
const email = ref('')
const password = ref('')
const router = useRouter()
const isLoggedIn = ref(session.isLoggedIn || false)

// Computed classes for theming
const themeClass = computed(() =>
	theme.value === 'light'
		? 'bg-light-background text-light-text'
		: 'bg-dark-background text-dark-text'
)
const cardClass = computed(() =>
	theme.value === 'light'
		? 'bg-light-cardBackground text-light-text'
		: 'bg-dark-cardBackground text-dark-text'
)
const buttonClass = computed(() =>
	theme.value === 'light'
		? 'bg-light-buttonBackground text-light-buttonText'
		: 'bg-dark-buttonBackground text-dark-buttonText'
)
const linkClass = computed(() => (theme.value === 'light' ? 'text-light-link' : 'text-dark-link'))
const inputClass = computed(() =>
	theme.value === 'light'
		? 'border-gray-300 focus:ring-light-accent'
		: 'border-gray-600 focus:ring-dark-accent'
)

// Handle login
const loginResource = createResource({
	url: 'psoc.api.auth.login',
	makeParams() {
		return {
			email: email.value,
			password: password.value,
		}
	},
	onSuccess() {
		console.log('Login successful')
		localStorage.setItem('isLoggedIn', 'true')
		isLoggedIn.value = true
		router.push('/profile')
	},
})

// Toggle theme
const toggleTheme = () => {
	theme.value = theme.value === 'light' ? 'dark' : 'light'
	localStorage.setItem('theme', theme.value)
}

// Sync theme on mount
onMounted(() => {
	theme.value = localStorage.getItem('theme') || 'light'
})
</script>
