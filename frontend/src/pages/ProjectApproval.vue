<template>
	<div :class="themeClass" class="min-h-screen bg-[#03001C] flex flex-col items-center p-10">
		<nav
			:class="navClass"
			class="w-full py-4 px-8 flex items-center justify-between fixed top-0 left-0 right-0 z-50 shadow"
		>
			<router-link to="/" class="text-3xl font-extrabold cursor-pointer">PSoC</router-link>

			<!-- Theme Toggle Button -->
			<button
				@click="toggleTheme"
				:class="buttonClass"
				class="px-4 py-2 rounded-lg transition"
			>
				{{ theme === 'light' ? '🌙 Dark Mode' : '☀️ Light Mode' }}
			</button>
		</nav>
		<div
			:class="themeClass"
			class="min-h-screen flex flex-col items-center p-10 transition-colors duration-300"
		>
			<h1 :class="linkClass" class="text-3xl font-bold mb-8 mt-12">Project Approvals</h1>

			<div :class="themeClass" class="w-full max-w-5xl space-y-6">
				<Card v-for="project in projects" :key="project.id" :class="cardClass">
					<CardHeader>
						<CardTitle class="text-3xl mr-3 mb-4">{{ project.name }}</CardTitle>
						<CardDescription class="opacity-75">{{
							project.description
						}}</CardDescription>
					</CardHeader>

					<CardContent class="opacity-80 space-y-2">
						<p><span class="font-semibold">Lead:</span> {{ project.lead }}</p>
						<p>
							<span class="font-semibold">Start Date:</span>
							{{ project.startDate }}
						</p>
						<p>
							<span class="font-semibold">Status:</span>
							{{ project.status }}
						</p>
					</CardContent>

					<CardFooter class="flex ml-2 mt-4">
						<Button
							variant="default"
							:class="buttonClass"
							class="mr-2"
							@click="viewProject(project.id)"
						>
							View Project
						</Button>
						<Button
							variant="default"
							class="bg-green-500 ml-2 hover:bg-green-400"
							@click="approveProject(project.id)"
						>
							Approve
						</Button>
						<Button
							variant="destructive"
							class="bg-red-600 text-white ml-2 hover:bg-red-400"
							@click="declineProject(project.id)"
						>
							Decline
						</Button>
					</CardFooter>
				</Card>
			</div>
		</div>
	</div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
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
const linkClass = computed(() => (theme.value === 'light' ? 'text-light-link' : 'text-dark-link'))
const buttonClass = computed(() =>
	theme.value === 'light'
		? 'bg-light-buttonBackground text-light-buttonText border'
		: 'bg-dark-buttonBackground text-dark-buttonText border',
)
const cardClass = computed(() =>
	theme.value === 'light'
		? 'bg-light-cardBackground text-light-text'
		: 'bg-dark-cardBackground text-light-text',
)

const projects = ref([
	{
		id: 1,
		name: 'AI Chatbot',
		lead: 'Alice Johnson',
		startDate: '2024-02-01',
		status: 'Pending Approval',
		description: 'An AI-powered chatbot for customer service.',
	},
	{
		id: 2,
		name: 'Blockchain Payment System',
		lead: 'Bob Smith',
		startDate: '2024-01-15',
		status: 'Pending Approval',
		description: 'A decentralized payment system using blockchain technology.',
	},
])

const viewProject = (id) => {
	router.push(`/project/${id}`)
}

const approveProject = (id) => {
	console.log(`Project ${id} approved ✅`)
}

const declineProject = (id) => {
	console.log(`Project ${id} declined ❌`)
}
const toggleTheme = () => {
	theme.value = theme.value === 'light' ? 'dark' : 'light'
	localStorage.setItem('theme', theme.value)
	document.documentElement.classList.toggle('dark', theme.value === 'dark')
}

onMounted(() => {
	document.documentElement.classList.toggle('dark', theme.value === 'dark')
})
</script>
