<template>
    <div :class="themeClass" class="min-h-screen flex flex-col transition-colors duration-300">
        <Navbar :theme="theme" :isLoggedIn="isLoggedIn" @toggle-theme="toggleTheme" />

        <div class="flex-grow flex items-center justify-center mt-20">
            <div :class="cardClass" class="w-full max-w-6xl p-10 rounded-2xl shadow-xl border border-opacity-30">
                <div class="flex flex-col md:flex-row items-center md:items-start">
                    <div class="flex flex-col items-center md:items-start w-full md:w-1/3">
                        <!-- Modified avatar circle with larger letter -->
                        <div 
                            class="w-44 h-44 rounded-full shadow-lg transition transform hover:scale-105 flex items-center justify-center"
                            :class="avatarClass"
                        >
                            <span class="text-[8rem] font-bold leading-none">{{ getFirstLetter(user.name) }}</span>
                        </div>
                        <h2 class="mt-5 text-3xl font-bold" :class="textClass">
                            {{ user.name }}
                        </h2>
                        <p class="text-lg opacity-80" :class="subTextClass">
                            {{ user.email }}
                        </p>
                        <p class="mt-2 text-md font-semibold px-4 py-1 rounded-full" 
                           :class="roleClass">
                            {{ user.role }}
                        </p>
                    </div>

                    <!-- Rest of the template remains the same -->
                    <div class="w-full md:w-2/3 mt-6 md:mt-0 md:pl-6">
                        <h3 class="text-2xl font-semibold border-b pb-2 mb-4" :class="titleClass">
                            About Me
                        </h3>
                        <p class="text-lg opacity-90" :class="subTextClass">{{ user.about }}</p>

                        <div class="mt-5 flex flex-wrap gap-4">
                            <a v-for="(link, key) in user.links" :key="key" :href="link.url" :class="buttonPrimary"
                                class="px-5 py-2 rounded-lg transition duration-300 transform hover:scale-110 shadow-md">
                                {{ link.label }}
                            </a>
                        </div>
                    </div>
                </div>

                <div v-if="user.role === 'Contributor'" class="mt-12">
                    <h3 class="text-2xl font-semibold border-b pb-2 mb-4" :class="titleClass">
                        Submitted Proposals
                    </h3>
                    <div v-for="proposal in proposals" :key="proposal.id" :class="cardClass"
                        class="mb-4 p-6 rounded-lg border-2 shadow-lg transition duration-300 hover:shadow-2xl hover:border-primary hover:scale-105">
                        <h4 class="text-xl font-bold" :class="titleClass">
                            {{ proposal.projectName }}
                        </h4>
                        <p class="text-lg opacity-80" :class="subTextClass">
                            {{ proposal.organization }}
                        </p>
                        <p class="mt-2 text-md" :class="subTextClass">{{ proposal.description }}</p>
                        <div class="mt-3 flex flex-wrap gap-2">
                            <span v-for="tech in proposal.technologies" :key="tech" 
                                  class="px-3 py-1 rounded-full text-sm"
                                  :class="techBadgeClass">
                                {{ tech }}
                            </span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <Footer :theme="theme" />
    </div>
</template>

<script setup>
// Script remains exactly the same as before
import { ref, computed, onMounted } from 'vue'
import Navbar from '@/components/Navbar.vue'
import Footer from '@/components/Footer.vue'
import { createResource } from 'frappe-ui'

const theme = ref(localStorage.getItem('theme') || 'light')
const isLoggedIn = ref(true)

// Mock user data
const user = ref({
    name: 'Sarah Anderson',
    email: 'sarah.anderson@gmail.com',
    role: 'Contributor',
    about: 'Passionate software developer with 3 years of experience in full-stack development. Currently pursuing my Master\'s in Computer Science with a focus on Machine Learning and AI. I love contributing to open-source projects and mentoring fellow developers. When I\'m not coding, you can find me hiking or playing chess.',
    links: [
        { label: 'GitHub', url: 'https://github.com/sarahanderson' },
        { label: 'LinkedIn', url: 'https://linkedin.com/in/sarahanderson' },
        { label: 'Portfolio', url: 'https://sarahanderson.dev' },
        { label: 'Blog', url: 'https://blog.sarahanderson.dev' }
    ]
})

// Mock proposals data
const proposals = ref([
    {
        id: 1,
        projectName: 'AI-Powered Code Review Assistant',
        organization: 'TechLabs Foundation',
        description: 'Developing an intelligent code review system that uses machine learning to identify potential bugs, security vulnerabilities, and code quality issues. The system will integrate with popular version control platforms and provide real-time feedback to developers.',
        technologies: ['Python', 'TensorFlow', 'Git', 'Docker']
    },
    {
        id: 2,
        projectName: 'Sustainable Energy Dashboard',
        organization: 'GreenTech Initiative',
        description: 'Creating an interactive dashboard for tracking and visualizing renewable energy usage across different regions. The project aims to help communities make data-driven decisions about sustainable energy adoption.',
        technologies: ['Vue.js', 'D3.js', 'Node.js', 'MongoDB']
    },
    {
        id: 3,
        projectName: 'Accessibility Testing Framework',
        organization: 'Web Standards Group',
        description: 'Building an automated testing framework for web accessibility compliance. The tool will help developers ensure their applications meet WCAG guidelines and provide suggestions for improvements.',
        technologies: ['JavaScript', 'Jest', 'Puppeteer', 'ARIA']
    }
])

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

const avatarClass = computed(() =>
    theme.value === 'light'
        ? 'bg-blue-100 text-blue-600 border-4 border-blue-200'
        : 'bg-blue-900 text-blue-200 border-4 border-blue-800'
)

const roleClass = computed(() =>
    theme.value === 'light'
        ? 'bg-green-100 text-green-700'
        : 'bg-green-900 text-green-200'
)

const techBadgeClass = computed(() =>
    theme.value === 'light'
        ? 'bg-gray-200 text-gray-700'
        : 'bg-gray-700 text-gray-200'
)

const buttonPrimary = computed(() =>
    theme.value === 'light'
        ? 'bg-blue-600 text-white hover:bg-blue-700'
        : 'bg-blue-500 text-white hover:bg-blue-600'
)

const titleClass = computed(() => theme.value === 'light' ? 'text-gray-800' : 'text-gray-100')
const textClass = computed(() => theme.value === 'light' ? 'text-gray-900' : 'text-gray-50')
const subTextClass = computed(() => theme.value === 'light' ? 'text-gray-600' : 'text-gray-300')

const getFirstLetter = (name) => {
    return name ? name.charAt(0).toUpperCase() : 'U'
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