<template>
	<div
		:class="themeClass"
		class="min-h-screen flex items-center justify-center px-6 transition-colors duration-300"
	>
		<!-- Navbar -->
		<nav
			:class="[
				'w-full py-4 px-8 flex items-center justify-between fixed top-0 left-0 right-0 z-50 shadow',
				themeClass,
			]"
			:style="{ backgroundColor: theme === 'light' ? 'white' : '#1a1a1a' }"
		>
			<router-link to="/" class="text-3xl font-extrabold cursor-pointer">PSoC</router-link>

			<button
				@click="toggleTheme"
				:class="buttonClass"
				class="px-4 py-2 rounded-lg transition"
			>
				{{ theme === 'light' ? '🌙 Dark Mode' : '☀️ Light Mode' }}
			</button>
		</nav>

		<!-- Form Container -->
		<div class="flex-grow w-full flex justify-center pt-24 pb-10 overflow-y-auto">
			<div
				class="w-full max-w-4xl p-8 rounded-xl shadow-lg hover:shadow-2xl transition"
				:class="cardClass"
			>
				<h2 class="text-3xl font-bold text-center mb-6">
					{{ step === 1 ? 'Create a New Account' : 'Additional Details' }}
				</h2>

				<form @submit.prevent="handleNextStep" class="space-y-6">
					<!-- Step 1: Basic Information -->
					<div v-if="step === 1" class="space-y-4">
						<div v-for="field in firstPartFields" :key="field.id" class="space-y-2">
							<label class="block text-lg font-medium" :for="field.id">{{
								field.label
							}}</label>
							<input
								:type="field.type"
								:id="field.id"
								v-model="firstPartData[field.model]"
								required
								class="w-full px-4 py-2 rounded-lg border focus:outline-none focus:ring-2 transition"
								:class="inputClass"
							/>
						</div>
					</div>

					<!-- Step 2: Extra Details -->
					<div v-if="step === 2" class="space-y-6">
						<div
							v-for="field in secondPartFields"
							:key="field.id"
							class="flex flex-col space-y-4"
						>
							<label class="block text-lg font-medium" :for="field.id">{{
								field.label
							}}</label>
							<input
								:is="field.tag"
								:type="field.type"
								:id="field.id"
								v-model="secondPartData[field.model]"
								required
								class="w-full px-4 py-2 rounded-lg border focus:outline-none focus:ring-2 transition block"
								:class="inputClass"
								:style="field.tag === 'textarea' ? { minHeight: '100px' } : {}"
							/>
						</div>
					</div>

					<!-- Buttons -->
					<div class="flex justify-between">
						<button
							v-if="step === 2"
							@click="step = 1"
							type="button"
							class="px-6 py-3 rounded-lg shadow transition text-lg font-semibold"
							:class="buttonClass"
						>
							Back
						</button>
						<button
							type="submit"
							class="px-6 py-3 rounded-lg shadow transition text-lg font-semibold"
							:class="buttonClass"
							@click="signUpAndDetails"
						>
							{{ step === 1 ? 'Save and Next' : 'Submit' }}
						</button>
					</div>
				</form>
			</div>
		</div>
	</div>
</template>

<script>
import { createResource } from 'frappe-ui'

export default {
	data() {
		return {
			theme: 'light',
			step: 1,
			firstPartData: {
				firstName: '',
				lastName: '',
				username: '',
				email: '',
				password: '',
				confirmPassword: '',
			},
			secondPartData: {
				about: '',
				domain: '',
				technologies: '',
				website: '',
				github: '',
				linkedin: '',
				resume: '',
			},
			firstPartFields: [
				{ id: 'firstName', label: 'First Name', type: 'text', model: 'firstName' },
				{ id: 'lastName', label: 'Last Name', type: 'text', model: 'lastName' },
				{ id: 'username', label: 'Username', type: 'text', model: 'username' },
				{ id: 'email', label: 'Email', type: 'email', model: 'email' },
				{ id: 'password', label: 'Password', type: 'password', model: 'password' },
				{
					id: 'confirmPassword',
					label: 'Confirm Password',
					type: 'password',
					model: 'confirmPassword',
				},
			],
			secondPartFields: [
				{ id: 'about', label: 'About', type: 'text', model: 'about', tag: 'textarea' },
				{ id: 'domain', label: 'Domain', type: 'text', model: 'domain', tag: 'input' },
				{
					id: 'technologies',
					label: 'Technologies',
					type: 'text',
					model: 'technologies',
					tag: 'input',
				},
				{
					id: 'website',
					label: 'Website URL',
					type: 'url',
					model: 'website',
					tag: 'input',
				},
				{ id: 'github', label: 'GitHub URL', type: 'url', model: 'github', tag: 'input' },
				{
					id: 'linkedin',
					label: 'LinkedIn URL',
					type: 'url',
					model: 'linkedin',
					tag: 'input',
				},
				{
					id: 'resume',
					label: 'Upload Resume',
					type: 'file',
					model: 'resume',
					tag: 'input',
				},
			],
		}
	},
	computed: {
		themeClass() {
			return this.theme === 'light'
				? 'bg-light-background text-light-text'
				: 'bg-dark-background text-dark-text'
		},
		cardClass() {
			return this.theme === 'light'
				? 'bg-light-cardBackground text-light-text'
				: 'bg-dark-cardBackground text-dark-text'
		},
		buttonClass() {
			return this.theme === 'light'
				? 'bg-light-buttonBackground text-light-buttonText'
				: 'bg-dark-buttonBackground text-dark-buttonText'
		},
		inputClass() {
			return this.theme === 'light'
				? 'border-gray-300 focus:ring-light-accent text-black bg-white'
				: 'border-gray-600 focus:ring-dark-accent text-white bg-gray-800'
		},
	},
	methods: {
		async signUpAndDetails() {
			const signUpData = this.firstPartData
			const signUpResource = createResource({
				url: 'psoc.api.contributor.register_and_login',
				makeParams() {
					return {
						first_name: signUpData.firstName,
						last_name: signUpData.lastName,
						username: signUpData.username,
						email: signUpData.email,
						password: signUpData.password,
					}
				},
				onSuccess() {
					console.log('Login successful')
				},
			})

			signUpResource.submit()

			const submissionDetailsData = this.secondPartData
			const submissionDetailsResource = createResource({
				url: 'psoc.api.contributor.submit_details',
				makeParams() {
					return {
						about: submissionDetailsData.about,
						domain: submissionDetailsData.domain,
						technologies: submissionDetailsData.technologies,
						website_url: submissionDetailsData.website,
						linkedin: submissionDetailsData.linkedin,
						github: submissionDetailsData.github,
					}
				},
				onSuccess() {
					console.log('Detail submission successful')
				},
			})

			submissionDetailsResource.submit()
		},
		handleNextStep() {
			if (this.step === 1) {
				if (this.firstPartData.password !== this.firstPartData.confirmPassword) {
					alert('Passwords do not match')
					return
				}
				this.step = 2
			} else {
				this.signUpAndDetails()
			}
		},
		toggleTheme() {
			this.theme = this.theme === 'light' ? 'dark' : 'light'
			localStorage.setItem('theme', this.theme)
		},
	},
}
</script>
