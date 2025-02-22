<template>
	<nav
		:class="navClass"
		class="w-full py-4 px-8 flex items-center justify-between fixed top-0 left-0 right-0 z-50 shadow-lg"
	>
		<h1 class="text-3xl font-extrabold">PSoC</h1>
		<button
			@click="toggleTheme"
			:class="buttonClass"
			class="px-4 py-2 rounded-lg transition duration-300 transform hover:scale-105"
		>
			{{ theme === 'light' ? '🌙 Dark Mode' : '☀️ Light Mode' }}
		</button>
	</nav>

	<div :class="themeClass" class="min-h-screen flex flex-col items-center p-10 mt-12">
		<div :class="cardClass" class="w-full max-w-6xl p-8 rounded-lg shadow-lg">
			<div class="flex flex-col md:flex-row items-center md:items-start">
				<div class="flex flex-col items-center md:items-start w-full md:w-1/3">
					<img
						:src="user.avatar"
						class="w-40 h-40 border-4 rounded-full"
						:class="borderClass"
					/>
					<h2 class="mt-4 text-3xl font-semibold" :class="textClass">{{ user.name }}</h2>
					<p class="text-lg" :class="subTextClass">{{ user.email }}</p>
				</div>

				<div class="w-full md:w-2/3 mt-6 md:mt-0 md:pl-6">
					<h3 class="text-2xl font-semibold border-b pb-2 mb-4" :class="titleClass">
						About Me
					</h3>
					<p class="text-lg" :class="subTextClass">{{ user.description }}</p>

					<div class="mt-4 flex flex-wrap gap-4">
						<a
							v-for="(link, key) in user.links"
							:key="key"
							:href="link.url"
							:class="buttonPrimary"
							class="px-4 py-2 rounded-lg transition duration-300 hover:scale-105"
							>{{ link.label }}</a
						>
					</div>
				</div>
			</div>

			<div class="mt-10">
				<h3 class="text-2xl font-semibold border-b pb-2 mb-4" :class="titleClass">
					Submitted Proposals
				</h3>
				<div
					v-for="proposal in user.proposals"
					:key="proposal.id"
					:class="cardClass"
					class="mb-3 p-6 rounded-lg border-2 transition duration-300 hover:shadow-xl hover:border-primary"
				>
					<h4 class="text-xl font-bold" :class="titleClass">
						{{ proposal.projectName }}
					</h4>
					<p class="text-lg" :class="subTextClass">{{ proposal.organization }}</p>
					<p class="mt-2 text-md" :class="subTextClass">{{ proposal.description }}</p>
				</div>
			</div>
		</div>
	</div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'

const theme = ref(localStorage.getItem('theme') || 'light')

const themeClass = computed(() =>
	theme.value === 'light'
		? 'bg-light-background text-light-text'
		: 'bg-dark-background text-dark-text',
)
const navClass = computed(() =>
	theme.value === 'light'
		? 'bg-light-navBackground text-light-navText'
		: 'bg-dark-navBackground text-dark-navText',
)
const buttonClass = computed(() =>
	theme.value === 'light'
		? 'bg-light-buttonBackground text-light-buttonText border'
		: 'bg-dark-buttonBackground text-dark-buttonText border',
)
const cardClass = computed(() =>
	theme.value === 'light'
		? 'bg-light-cardBackground text-light-text'
		: 'bg-dark-cardBackground text-dark-text',
)
const submitButtonClass = computed(() =>
	theme.value === 'light'
		? 'bg-light-buttonBackground text-light-buttonText shadow-lg hover:bg-light-hoverButtonBackground hover:text-light-hoverButtonText'
		: 'bg-dark-buttonBackground text-dark-buttonText shadow-lg hover:bg-dark-hoverButtonBackground hover:text-dark-hoverButtonText',
)

const buttonPrimary = computed(
	() =>
		`bg-${theme.value}-buttonBackground text-${theme.value}-buttonText hover:bg-${theme.value}-buttonHoverBackground hover:text-${theme.value}-buttonHoverText`,
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
