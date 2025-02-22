<template>
	 <div :class="themeClass" class="min-h-screen flex flex-col transition-colors duration-300">
    <Navbar :theme="theme" :isLoggedIn="isLoggedIn" @toggle-theme="toggleTheme"/>
    
    <!-- Main content container with flex-grow to fill available space -->
    <div class="flex-grow flex items-center justify-center mt-20">
		<div
			:class="cardClass"
			class="w-full max-w-6xl p-10 rounded-2xl shadow-xl border border-opacity-30"
		>
			<div class="flex flex-col md:flex-row items-center md:items-start">
				<div class="flex flex-col items-center md:items-start w-full md:w-1/3">
					<img
						:src="user.avatar"
						class="w-44 h-44 border-4 rounded-full shadow-lg transition transform hover:scale-105"
						:class="borderClass"
					/>
					<h2 class="mt-5 text-3xl font-bold" :class="textClass">{{ user.name }}</h2>
					<p class="text-lg opacity-80" :class="subTextClass">{{ user.email }}</p>
				</div>

				<div class="w-full md:w-2/3 mt-6 md:mt-0 md:pl-6">
					<h3 class="text-2xl font-semibold border-b pb-2 mb-4" :class="titleClass">
						About Me
					</h3>
					<p class="text-lg opacity-90" :class="subTextClass">{{ user.description }}</p>

					<div class="mt-5 flex flex-wrap gap-4">
						<a
							v-for="(link, key) in user.links"
							:key="key"
							:href="link.url"
							:class="buttonPrimary"
							class="px-5 py-2 rounded-lg transition duration-300 transform hover:scale-110 shadow-md"
						>
							{{ link.label }}
						</a>
					</div>
				</div>
			</div>

			<div class="mt-12">
				<h3 class="text-2xl font-semibold border-b pb-2 mb-4" :class="titleClass">
					Submitted Proposals
				</h3>
				<div
					v-for="proposal in user.proposals"
					:key="proposal.id"
					:class="cardClass"
					class="mb-4 p-6 rounded-lg border-2 shadow-lg transition duration-300 hover:shadow-2xl hover:border-primary hover:scale-105"
				>
					<h4 class="text-xl font-bold" :class="titleClass">
						{{ proposal.projectName }}
					</h4>
					<p class="text-lg opacity-80" :class="subTextClass">
						{{ proposal.organization }}
					</p>
					<p class="mt-2 text-md" :class="subTextClass">{{ proposal.description }}</p>
				</div>
			</div>
		</div>
	</div>
<Footer :theme="theme" />
	</div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import Navbar from '@/components/Navbar.vue';
import Footer from '@/components/Footer.vue';

const theme = ref(localStorage.getItem('theme') || 'light')

const themeClass = computed(() =>
	theme.value === 'light'
		? 'bg-light-background text-light-text'
		: 'bg-dark-background text-dark-text',
)
const navClass = computed(() =>
	theme.value === 'light'
		? 'bg-white bg-opacity-70 text-black'
		: 'bg-black bg-opacity-70 text-white',
)
const buttonClass = computed(() =>
	theme.value === 'light'
		? 'bg-black text-white border border-black'
		: 'bg-white text-black border border-white',
)
const cardClass = computed(() =>
	theme.value === 'light'
		? 'bg-white text-black border-gray-300'
		: 'bg-gray-900 text-white border-gray-700',
)
const buttonPrimary = computed(
	() =>
		`bg-${theme.value === 'light' ? 'black text-white' : 'white text-black'} border rounded-lg px-4 py-2`,
)

const user = ref({
	avatar: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTF5-3YjBcXTqKUlOAeUUtuOLKgQSma2wGG1g&s',
	name: 'John Doe',
	email: 'johndoe@example.com',
	description: 'Passionate software developer working with AI & Web3 technologies!',
	links: [
		{ label: 'LinkedIn', url: 'https://linkedin.com/in/kierthana' },
		{ label: 'GitHub', url: 'https://github.com/kierthana' },
		{ label: 'Download Resume', url: 'https://example.com/resume.pdf' },
	],
	proposals: [
		{
			id: 1,
			projectName: 'EventHive',
			organization: 'Open Source Org',
			description: 'A collaborative event organizer platform.',
		},
		{
			id: 2,
			projectName: 'Echo Mind',
			organization: 'AI Research Lab',
			description: 'A chatbot analyzing database-driven insights.',
		},
	],
})

const toggleTheme = () => {
	theme.value = theme.value === 'light' ? 'dark' : 'light'
	localStorage.setItem('theme', theme.value)
	document.documentElement.classList.toggle('dark', theme.value === 'dark')
}

onMounted(() => {
	document.documentElement.classList.toggle('dark', theme.value === 'dark')
})
</script>
