<template>
	<div :class="themeClass" class="min-h-screen flex flex-col transition-colors duration-300">
	  <Navbar :theme="theme" :isLoggedIn="isLoggedIn" @toggle-theme="toggleTheme" />
  
	  <div class="flex-grow flex items-center justify-center mt-20 mb-10">
		<div
		  :class="cardClass"
		  class="w-full max-w-6xl p-10 rounded-2xl shadow-xl border border-opacity-30"
		>
		  <!-- Organization Header Section -->
		  <div class="flex flex-col md:flex-row items-center md:items-start gap-8">
			<div class="flex flex-col items-center md:items-start w-full md:w-1/3">
			  <div v-if="organization.logo">
				<img
				  :src="organization.logo"
				  class="w-44 h-44 border-4 rounded-full shadow-lg transition transform hover:scale-105"
				  :class="borderClass"
				  alt="Organization Logo"
				/>
			  </div>
			  <div v-else>
				<AvatarLetter
				  :text="organization.name"
				  :class="[
					borderClass,
					theme === 'light' ? 'bg-gray-100 text-gray-700' : 'bg-gray-800 text-gray-200',
					'border-4 shadow-lg transition transform hover:scale-105'
				  ]"
				/>
			  </div>
			  <h2 class="mt-5 text-3xl font-bold" :class="textClass">
				{{ organization.name }}
			  </h2>
			  <p class="text-lg opacity-80" :class="subTextClass">{{ organization.tagline }}</p>
			</div>
  
			<div class="w-full md:w-2/3">
			  <!-- Organization Details -->
			  <div class="space-y-6">
				<div>
				  <h3 class="text-2xl font-semibold border-b pb-2 mb-4" :class="titleClass">
					Organization Details
				  </h3>
				  
				  <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
					<div :class="subCardClass" class="p-4 rounded-lg">
					  <h4 class="font-semibold" :class="textClass">Organization ID</h4>
					  <p :class="subTextClass">{{ organization.organizationId }}</p>
					</div>
					
					<div :class="subCardClass" class="p-4 rounded-lg">
					  <h4 class="font-semibold" :class="textClass">Email</h4>
					  <p :class="subTextClass">{{ organization.email }}</p>
					</div>
  
					<div :class="subCardClass" class="p-4 rounded-lg">
					  <h4 class="font-semibold" :class="textClass">Domain</h4>
					  <p :class="subTextClass">{{ organization.domain }}</p>
					</div>
  
					<div :class="subCardClass" class="p-4 rounded-lg">
					  <h4 class="font-semibold" :class="textClass">Website</h4>
					  <a :href="organization.website" :class="subTextClass" class="hover:underline">
						{{ organization.website }}
					  </a>
					</div>
				  </div>
				</div>
  
				<div>
				  <h3 class="text-2xl font-semibold border-b pb-2 mb-4" :class="titleClass">About</h3>
				  <p class="text-lg opacity-90" :class="subTextClass">{{ organization.about }}</p>
				</div>
  
				<div>
				  <h3 class="text-2xl font-semibold border-b pb-2 mb-4" :class="titleClass">
					Technologies
				  </h3>
				  <div class="flex flex-wrap gap-2">
					<span
					  v-for="tech in organization.technologies"
					  :key="tech"
					  :class="subCardClass"
					  class="px-3 py-1 rounded-full text-sm"
					>
					  {{ tech }}
					</span>
				  </div>
				</div>
  
				<div>
				  <h3 class="text-2xl font-semibold border-b pb-2 mb-4" :class="titleClass">
					Social Links
				  </h3>
				  <div class="flex flex-wrap gap-4">
					<a
					  v-if="organization.linkedin"
					  :href="organization.linkedin"
					  :class="buttonPrimary"
					  class="flex items-center gap-2"
					  target="_blank"
					>
					  LinkedIn
					</a>
					<a
					  v-if="organization.github"
					  :href="organization.github"
					  :class="buttonPrimary"
					  class="flex items-center gap-2"
					  target="_blank"
					>
					  GitHub
					</a>
					<a
					  v-if="organization.website"
					  :href="organization.website"
					  :class="buttonPrimary"
					  class="flex items-center gap-2"
					  target="_blank"
					>
					  Website
					</a>
				  </div>
				</div>
  
				<!-- Action Buttons -->
				<div class="flex justify-end gap-4 mt-8">
				  <button
					@click="handleDecline"
					class="px-6 py-2 rounded-lg border transition duration-300"
					:class="buttonSecondary"
				  >
					Decline
				  </button>
				  <button
					@click="handleAccept"
					class="px-6 py-2 rounded-lg transition duration-300"
					:class="buttonPrimary"
				  >
					Accept
				  </button>
				</div>
			  </div>
			</div>
		  </div>
		</div>
	  </div>
	  <Footer :theme="theme" />
	</div>
  </template>
  
  <script setup>
  import { ref, computed, onMounted } from 'vue'
  import Navbar from '@/components/Navbar.vue'
  import Footer from '@/components/Footer.vue'
  import { createResource } from 'frappe-ui'
  
  // AvatarLetter component
  const AvatarLetter = {
	props: {
	  text: {
		type: String,
		default: '?'
	  },
	  class: {
		type: String,
		default: ''
	  }
	},
	template: `
	  <div 
		:class="['w-44 h-44 rounded-full flex items-center justify-center text-6xl font-bold', class]"
	  >
		{{ letter }}
	  </div>
	`,
	computed: {
	  letter() {
		return (this.text || '?').charAt(0).toUpperCase()
	  }
	}
  }
  
  const theme = ref(localStorage.getItem('theme') || 'light')
  const orgId = ref('your_org_id')
  const organization = ref({
	name: 'Example Organization',
	organizationId: 'ORG123456',
	email: 'contact@example.org',
	tagline: 'Building the future of technology',
	about: 'We are a forward-thinking organization dedicated to innovation and excellence in software development.',
	domain: 'Technology',
	technologies: ['Vue.js', 'Node.js', 'Python', 'AWS', 'Docker'],
	website: 'https://example.org',
	linkedin: 'https://linkedin.com/company/example-org',
	github: 'https://github.com/example-org'
  })
  
  // Theme-related computed properties
  const themeClass = computed(() => 
	theme.value === 'light' ? 'bg-light-background text-light-text' : 'bg-dark-background text-dark-text'
  )
  
  const cardClass = computed(() =>
	theme.value === 'light' ? 'bg-white text-black border-gray-300' : 'bg-gray-900 text-white border-gray-700'
  )
  
  const borderClass = computed(() =>
	theme.value === 'light' ? 'border-gray-200' : 'border-gray-700'
  )
  
  const textClass = computed(() =>
	theme.value === 'light' ? 'text-gray-900' : 'text-white'
  )
  
  const subTextClass = computed(() =>
	theme.value === 'light' ? 'text-gray-600' : 'text-gray-300'
  )
  
  const titleClass = computed(() =>
	theme.value === 'light' ? 'text-gray-800' : 'text-gray-100'
  )
  
  const subCardClass = computed(() =>
	theme.value === 'light' ? 'bg-gray-50 border-gray-200' : 'bg-gray-800 border-gray-700'
  )
  
  const buttonPrimary = computed(() =>
	`bg-${theme.value === 'light' ? 'black text-white' : 'white text-black'} border rounded-lg px-4 py-2`
  )
  
  const buttonSecondary = computed(() =>
	theme.value === 'light'
	  ? 'bg-gray-100 text-gray-800 hover:bg-gray-200'
	  : 'bg-gray-800 text-gray-200 hover:bg-gray-700'
  )
  
  // Action handlers
  const handleAccept = () => {
	// Implement accept logic
	console.log('Organization accepted')
  }
  
  const handleDecline = () => {
	// Implement decline logic
	console.log('Organization declined')
  }
  
  const toggleTheme = () => {
	theme.value = theme.value === 'light' ? 'dark' : 'light'
	localStorage.setItem('theme', theme.value)
	document.documentElement.classList.toggle('dark', theme.value === 'dark')
  }
  
  // Fetch organization data
  const fetchOrgData = () => {
	createResource({
	  url: 'psoc.api.organization.get_organization_profile',
	  makeParams() {
		return { organization_id: orgId.value }
	  },
	  onSuccess(data) {
		if (data.status === 'success' && data.data.length > 0) {
		  organization.value = data.data[0]
		} else {
		  console.error('Unexpected data format:', data)
		}
	  },
	  onError(err) {
		console.error('Error fetching organization data:', err.message)
	  },
	  auto: true
	})
  }
  
  onMounted(() => {
	document.documentElement.classList.toggle('dark', theme.value === 'dark')
	fetchOrgData()
  })
  </script>