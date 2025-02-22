<template>
	<div :class="themeClass" class="min-h-screen transition-colors duration-300">
		<!-- Navbar -->
    <Navbar :theme="theme" :isLoggedIn="isLoggedIn" @toggle-theme="toggleTheme"/>


		<!-- About Page -->
		<section class="max-w-6xl mx-auto py-24 px-6">
			<h2 class="text-[2rem] font-bold text-center">
				PSoC (Platform for Season of Commits)
			</h2>
			<p class="text-xl text-center mt-4">
				A decentralized, open-source platform designed to streamline the process of
				managing and organizing open-source contribution programs like Season of Commits,
				GSoC, and Outreachy.
			</p>

			<!-- About Section -->
			<div class="mt-12">
				<h3 class="text-2xl font-semibold">🌎 What is PSoC?</h3>
				<p class="mt-4 text-lg leading-relaxed">
					PSoC is a **collaborative ecosystem** that empowers **developers, mentors, and
					organizations** to engage in open-source development effectively. It provides a
					structured way to propose projects, submit applications, and contribute under
					expert guidance.
				</p>
				<p class="mt-4 text-lg leading-relaxed">
					Unlike traditional closed-source platforms, PSoC is **fully open-source** and
					adaptable, ensuring that every contributor has access to transparent processes
					and fair selection.
				</p>
			</div>

			<!-- Features Section -->
			<div class="mt-12">
				<h3 class="text-2xl font-semibold">🚀 Key Features of PSoC</h3>
				<ul class="mt-6 grid md:grid-cols-2 gap-6">
					<li
						class="p-6 rounded-lg shadow-sm hover:shadow-md transition"
						:class="cardClass"
					>
						<h4 class="text-xl font-bold">📜 Proposal Submission</h4>
						<p class="mt-2 text-sm">
							Contributors can submit project proposals that go through a structured
							review process, allowing mentors to provide feedback.
						</p>
					</li>
					<li
						class="p-6 rounded-lg shadow-sm hover:shadow-md transition"
						:class="cardClass"
					>
						<h4 class="text-xl font-bold">✅ Approval Management</h4>
						<p class="mt-2 text-sm">
							A seamless approval workflow for mentors and organizers to evaluate and
							accept contributors based on skill and interest.
						</p>
					</li>
					<li
						class="p-6 rounded-lg shadow-sm hover:shadow-md transition"
						:class="cardClass"
					>
						<h4 class="text-xl font-bold">🤝 Mentor-Contributor Collaboration</h4>
						<p class="mt-2 text-sm">
							Direct interactions between mentors and contributors to foster
							learning, skill development, and project success.
						</p>
					</li>
					<li
						class="p-6 rounded-lg shadow-sm hover:shadow-md transition"
						:class="cardClass"
					>
						<h4 class="text-xl font-bold">📊 Analytics & Insights</h4>
						<p class="mt-2 text-sm">
							Visual dashboards displaying contributions, project progress, and
							community engagement.
						</p>
					</li>
					<li
						class="p-6 rounded-lg shadow-sm hover:shadow-md transition"
						:class="cardClass"
					>
						<h4 class="text-xl font-bold">🔍 Project Filtering</h4>
						<p class="mt-2 text-sm">
							Find and filter projects based on expertise, technology stack, and
							interest areas.
						</p>
					</li>
					<li
						class="p-6 rounded-lg shadow-sm hover:shadow-md transition"
						:class="cardClass"
					>
						<h4 class="text-xl font-bold">🔐 Secure User Management</h4>
						<p class="mt-2 text-sm">
							A role-based access system ensures that contributors, mentors, and
							organizers have the appropriate permissions.
						</p>
					</li>
				</ul>
			</div>

			<!-- Tech Stack -->
			<div class="mt-12">
				<h3 class="text-2xl font-semibold">🛠️ Tech Stack</h3>
				<ul class="mt-4 grid md:grid-cols-2 gap-6">
					<li class="p-4 rounded-lg shadow-sm" :class="cardClass">Frappe Framework</li>
					<li class="p-4 rounded-lg shadow-sm" :class="cardClass">Frappe UI</li>
					<li class="p-4 rounded-lg shadow-sm" :class="cardClass">Vue.js</li>
					<li class="p-4 rounded-lg shadow-sm" :class="cardClass">TailwindCSS</li>
				</ul>
			</div>

			<!-- Why Join Section -->
			<div class="mt-12">
				<h3 class="text-2xl font-semibold">🎯 Why Join PSoC?</h3>
				<ul class="mt-6 list-disc pl-6 text-lg">
					<li>
						<b>For Contributors:</b> Gain hands-on experience, contribute to real-world
						projects, and get mentorship from experts.
					</li>
					<li>
						<b>For Mentors:</b> Guide the next generation of developers, review
						proposals, and contribute to open-source leadership.
					</li>
					<li>
						<b>For Organizers:</b> Manage projects, oversee the contributor selection
						process, and ensure a seamless experience.
					</li>
				</ul>
			</div>
		</section>

		<!-- Footer -->
    <Footer :theme="theme" class="mt-12" />
	</div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import Navbar from '@/components/Navbar.vue'
import Footer from '@/components/Footer.vue'

// Theme Management
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
		? 'bg-light-buttonBackground text-light-buttonText shadow-lg'
		: 'bg-dark-buttonBackground text-dark-text shadow-lg',
)

// Function to toggle theme
const toggleTheme = () => {
	theme.value = theme.value === 'light' ? 'dark' : 'light'
	localStorage.setItem('theme', theme.value)
}

onMounted(() => {
	theme.value = localStorage.getItem('theme') || 'light'
})
</script>
