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
                            :class="[inputClass, theme === 'dark' ? 'bg-gray-700 text-white' : 'bg-white text-black']"
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
                            :class="[inputClass, theme === 'dark' ? 'bg-gray-700 text-white' : 'bg-white text-black']"
                        />
                    </div>

                    <div class="flex justify-between text-sm mt-2">
                        <a
                            href="#"
                            @click.prevent="showForgotPasswordPopup = true"
                            class="hover:underline"
                            :class="linkClass"
                        >Forgot Password?</a>
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

        <!-- Forgot Password Popup -->
        <div v-if="showForgotPasswordPopup" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
            <div class="bg-white rounded-lg p-8 max-w-md w-full mx-4">
                <h3 class="text-xl font-bold mb-4 text-black">Reset Password</h3>
                <p class="text-gray-700 mb-4">
                    This is in development and hence we have not implemented secure emailing option to change the password, 
                    as the project is running in localhost as of now, you can directly change the password below without verification
                </p>
                <div class="mb-4">
                    <label class="block text-gray-700 text-sm font-bold mb-2" for="newPassword">
                        New Password
                    </label>
                    <input
                        type="password"
                        id="newPassword"
                        v-model="newPassword"
                        class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
                    />
                </div>
                <div class="flex justify-end space-x-3">
                    <button
                        @click="showForgotPasswordPopup = false"
                        class="px-4 py-2 text-gray-600 hover:text-gray-800"
                    >
                        Cancel
                    </button>
                    <button
                        @click="updatePassword"
                        class="px-4 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600"
                    >
                        Update Password
                    </button>
                </div>
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
const showForgotPasswordPopup = ref(false)
const newPassword = ref('')

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
	onSuccess(data) {
		console.log(data)
		localStorage.setItem('role', data.role)
		console.log('Login successful')
		localStorage.setItem('isLoggedIn', 'true')
		isLoggedIn.value = true
		router.push('/profile')
	},
})

// Update password function
const updatePassword = () => {
    if (newPassword.value) {
        localStorage.setItem('password', newPassword.value)
        showForgotPasswordPopup.value = false
        alert('Password updated successfully!')
    } else {
        alert('Please enter a new password')
    }
}

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