<template>
	<div :class="themeClass" class="min-h-screen flex flex-col transition-colors duration-300">
		<Navbar :theme="theme" :isLoggedIn="isLoggedIn" @toggle-theme="toggleTheme" />

		<!-- Main content container -->
		<div class="flex-grow flex items-center justify-center mt-20">
			<div :class="cardClass" class="w-full max-w-6xl p-10 rounded-2xl shadow-xl border border-opacity-30">
				<!-- Organization Header Section -->
				<div class="flex flex-col md:flex-row items-center md:items-start">
					<div class="flex flex-col items-center md:items-start w-full md:w-1/3">
						<div v-if="organization.logo">
							<img :src="organization.logo"
								class="w-44 h-44 border-4 rounded-full shadow-lg transition transform hover:scale-105"
								:class="borderClass" 
								alt="Organization Logo"/>
						</div>
						<div v-else>
							<AvatarLetter 
								:text="organization.name || 'Organization'"
								:class="[
									borderClass,
									theme === 'light' ? 'bg-gray-100 text-gray-700' : 'bg-gray-800 text-gray-200',
									'border-4 shadow-lg transition transform hover:scale-105'
								]"
							/>
						</div>
						<h2 class="mt-5 text-3xl font-bold" :class="textClass">
							{{ organization.name || 'Organization Name' }}
						</h2>
						<p class="text-lg opacity-80" :class="subTextClass">
							{{ organization.email || 'organization@email.com' }}
						</p>
					</div>

					<div class="w-full md:w-2/3 mt-6 md:mt-0 md:pl-6">
						<h3 class="text-2xl font-semibold border-b pb-2 mb-4" :class="titleClass">
							About Organization
						</h3>
						<p class="text-lg opacity-90" :class="subTextClass">
							{{ organization.about || 'Organization description goes here' }}
						</p>

						<div class="mt-5 flex flex-wrap gap-4">
							<a v-for="(link, key) in organization.links" :key="key" :href="link.url" :class="buttonPrimary"
								class="px-5 py-2 rounded-lg transition duration-300 transform hover:scale-110 shadow-md">
								{{ link.label }}
							</a>
						</div>
					</div>
				</div>

				<!-- Projects Section -->
				<div class="mt-12">
					<div class="flex justify-between items-center mb-6">
						<h3 class="text-2xl font-semibold" :class="titleClass">
							Projects
						</h3>
						<div class="flex gap-4">
							<select v-model="statusFilter" :class="selectClass" class="p-2 rounded-lg">
								<option value="">All Status</option>
								<option value="active">Active</option>
								<option value="completed">Completed</option>
								<option value="upcoming">Upcoming</option>
							</select>
						</div>
					</div>

					<div v-if="filteredProjects.length" class="space-y-6">
						<div v-for="project in filteredProjects" :key="project.id" :class="cardClass"
							class="p-6 rounded-lg border-2 shadow-lg transition-all duration-300 hover:shadow-xl">
							<div class="flex justify-between items-start mb-4">
								<div>
									<h4 class="text-xl font-bold" :class="titleClass">
										{{ project.name }}
									</h4>
									<div class="flex items-center gap-2 mt-1">
										<span :class="getStatusClass(project.status)" class="px-2 py-1 rounded-full text-sm">
											{{ project.status }}
										</span>
										<span class="text-sm opacity-80" :class="subTextClass">
											{{ formatDate(project.deadline) }}
										</span>
									</div>
								</div>
								<button @click="toggleProposals(project.id)" :class="buttonPrimary">
									{{ expandedProjects.includes(project.id) ? 'Hide Proposals' : 'Show Proposals' }}
								</button>
							</div>
							
							<p class="mt-2 text-md" :class="subTextClass">{{ project.description }}</p>

							<!-- Proposals for this project -->
							<div v-if="expandedProjects.includes(project.id)" class="mt-4">
								<div class="flex justify-between items-center mb-3">
									<h5 class="text-lg font-semibold" :class="titleClass">Submitted Proposals</h5>
									<span class="text-sm" :class="subTextClass">
										Total: {{ projectProposals[project.id]?.length || 0 }}
									</span>
								</div>
								<div v-if="projectProposals[project.id]?.length" class="space-y-4">
									<div v-for="proposal in projectProposals[project.id]" :key="proposal.id"
										class="p-4 rounded-lg border" :class="subCardClass">
										<div class="flex items-start justify-between">
											<div>
												<h6 class="font-semibold" :class="titleClass">
													{{ proposal.contributor_name }}
												</h6>
												<p class="text-sm opacity-80" :class="subTextClass">
													Submitted: {{ formatDate(proposal.submission_date) }}
												</p>
											</div>
											<router-link :to="`/proposal/list/${proposal.id}`" :class="buttonSecondary">
											View Details
											</router-link>
										</div>
									</div>
								</div>
								<p v-else class="text-md opacity-70" :class="subTextClass">
									No proposals submitted yet.
								</p>
							</div>
						</div>
					</div>
					<div v-else class="text-center py-8" :class="subTextClass">
						No projects found matching the selected filter.
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

// Mock data
const mockProjects = [
  {
    id: 1,
    name: "Open Source Documentation System",
    status: "active",
    deadline: "2025-06-30",
    description: "Developing a comprehensive documentation system for open source projects with built-in version control and collaboration features.",
  },
  {
    id: 2,
    name: "Community Chat Platform",
    status: "upcoming",
    deadline: "2025-08-15",
    description: "Building a real-time chat platform specifically designed for open source communities with support for code sharing and integration with popular version control systems.",
  },
  {
    id: 3,
    name: "Contributor Analytics Dashboard",
    status: "completed",
    deadline: "2025-01-20",
    description: "A analytics dashboard to track and visualize contributor activities, project health metrics, and community engagement statistics.",
  }
]

const mockProposals = {
  1: [
    {
      id: 101,
      contributor_name: "Sarah Chen",
      submission_date: "2025-02-15",
      status: "under_review"
    },
    {
      id: 102,
      contributor_name: "Alex Kumar",
      submission_date: "2025-02-16",
      status: "accepted"
    }
  ],
  2: [
    {
      id: 103,
      contributor_name: "Maria Garcia",
      submission_date: "2025-02-14",
      status: "pending"
    }
  ],
  3: [
    {
      id: 104,
      contributor_name: "James Wilson",
      submission_date: "2024-12-20",
      status: "completed"
    },
    {
      id: 105,
      contributor_name: "Priya Patel",
      submission_date: "2024-12-21",
      status: "completed"
    }
  ]
}

const theme = ref(localStorage.getItem('theme') || 'light')
const orgId = ref('your_org_id') // Replace with actual org ID from your auth system
const organization = ref({})
const projects = ref([])
const projectProposals = ref({})
const expandedProjects = ref([])
const statusFilter = ref('')

// Theme-related computed properties
const themeClass = computed(() =>
	theme.value === 'light'
		? 'bg-light-background text-light-text'
		: 'bg-dark-background text-dark-text'
)

const cardClass = computed(() =>
	theme.value === 'light'
		? 'bg-white text-black border-gray-300'
		: 'bg-gray-900 text-white border-gray-700'
)

const borderClass = computed(() =>
	theme.value === 'light'
		? 'border-gray-200'
		: 'border-gray-700'
)

const textClass = computed(() =>
	theme.value === 'light'
		? 'text-gray-900'
		: 'text-white'
)

const subTextClass = computed(() =>
	theme.value === 'light'
		? 'text-gray-600'
		: 'text-gray-300'
)

const titleClass = computed(() =>
	theme.value === 'light'
		? 'text-gray-800'
		: 'text-gray-100'
)

const selectClass = computed(() =>
	theme.value === 'light'
		? 'bg-white border-gray-300 text-gray-700'
		: 'bg-gray-800 border-gray-600 text-gray-200'
)

const subCardClass = computed(() =>
	theme.value === 'light'
		? 'bg-gray-50 border-gray-200'
		: 'bg-gray-800 border-gray-700'
)

const buttonPrimary = computed(() =>
	`bg-${theme.value === 'light' ? 'black text-white' : 'white text-black'} border rounded-lg px-4 py-2`
)

const buttonSecondary = computed(() =>
	theme.value === 'light'
		? 'bg-gray-100 text-gray-800 hover:bg-gray-200 px-3 py-1 rounded'
		: 'bg-gray-800 text-gray-200 hover:bg-gray-700 px-3 py-1 rounded'
)

// Filter projects based on status
const filteredProjects = computed(() => {
	if (!statusFilter.value) return projects.value
	return projects.value.filter(project => project.status.toLowerCase() === statusFilter.value)
})

// Get status badge color class
const getStatusClass = (status) => {
	const statusClasses = {
		active: 'bg-green-100 text-green-800 dark:bg-green-900 dark:text-green-200',
		completed: 'bg-blue-100 text-blue-800 dark:bg-blue-900 dark:text-blue-200',
		upcoming: 'bg-yellow-100 text-yellow-800 dark:bg-yellow-900 dark:text-yellow-200'
	}
	return statusClasses[status.toLowerCase()] || 'bg-gray-100 text-gray-800 dark:bg-gray-800 dark:text-gray-200'
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
		auto: true,
	})
}

// Fetch organization's projects
const fetchProjects = () => {
	createResource({
		url: 'psoc.api.organization.get_organization_projects',
		makeParams() {
			return { organization_id: orgId.value }
		},
		onSuccess(data) {
			if (data.status === 'success' && Array.isArray(data.data)) {
				projects.value = data.data
			} else {
				console.error('Unexpected projects data format:', data)
				projects.value = mockProjects // Use mock data as fallback
			}
		},
		onError(err) {
			console.error('Error fetching projects:', err.message)
			projects.value = mockProjects // Use mock data on error
		},
		auto: true,
	})
}

// Fetch proposals for a specific project
const fetchProjectProposals = (projectId) => {
	createResource({
		url: 'psoc.api.organization.get_project_proposals',
		makeParams() {
			return { project_id: projectId }
		},
		onSuccess(data) {
			if (data.status === 'success' && Array.isArray(data.data)) {
				projectProposals.value = {
					...projectProposals.value,
					[projectId]: data.data,
				}
			} else {
				console.error('Unexpected proposals data format:', data)
				projectProposals.value[projectId] = mockProposals[projectId] || [] // Use mock data as fallback
			}
		},
		onError(err) {
			console.error('Error fetching proposals:', err.message)
			projectProposals.value[projectId] = mockProposals[projectId] || [] // Use mock data on error
		},
		auto: true,
	})
}

const toggleProposals = (projectId) => {
	const index = expandedProjects.value.indexOf(projectId)
	if (index === -1) {
		expandedProjects.value.push(projectId)
		fetchProjectProposals(projectId)
	} else {
		expandedProjects.value.splice(index, 1)
	}
}

const formatDate = (date) => {
	return new Date(date).toLocaleDateString('en-US', {
		year: 'numeric',
		month: 'long',
		day: 'numeric',
	})
}

const toggleTheme = () => {
	theme.value = theme.value === 'light' ? 'dark' : 'light'
	localStorage.setItem('theme', theme.value)
	document.documentElement.classList.toggle('dark', theme.value === 'dark')
}

onMounted(() => {
	document.documentElement.classList.toggle('dark', theme.value === 'dark')
	fetchOrgData()
	fetchProjects()
})
</script>