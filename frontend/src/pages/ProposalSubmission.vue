<template>
	<div :class="themeClass" class="min-h-screen flex flex-col transition-colors duration-300">
    <Navbar :theme="theme" :isLoggedIn="isLoggedIn" @toggle-theme="toggleTheme"/>
    
    <!-- Main content container with flex-grow to fill available space -->
    <div class="flex-grow flex items-center justify-center">
		<div :class="cardClass" class="w-full max-w-4xl mx-auto p-10 rounded-xl shadow-xl">
			<h1 class="text-3xl font-semibold text-center mb-8">Submit Your Proposal</h1>

			<form class="space-y-8" @submit.prevent="submitForm">
				<!-- Personal Information Section -->
				<div class="space-y-4">
					<h3 class="text-xl font-semibold text-center">Personal Information</h3>
					<hr class="border-[#5FFF16] w-1/3 my-2 mx-auto" />

					<InputField
						id="name"
						label="Full Name"
						v-model="formData.name"
						placeholder="John Doe"
						:theme="theme"
					/>
					<InputField
						id="email"
						label="Email Address"
						type="email"
						v-model="formData.email"
						placeholder="johndoe@example.com"
						:theme="theme"
					/>
				</div>

				<!-- Project Information Section -->
				<div class="space-y-4">
					<h3 class="text-xl font-semibold text-center">Project Information</h3>
					<hr class="border-[#5FFF16] w-1/3 my-2 mx-auto" />

					<InputField
						id="projectTitle"
						label="Project Title"
						v-model="formData.projectTitle"
						placeholder="Enter the project title"
						:theme="theme"
						/>

					<TextArea
						id="synopsis"
						label="Synopsis"
						v-model="formData.synopsis"
						placeholder="Brief summary of your project"
						:theme="theme"
					/>
					<TextArea
						id="technicalApproach"
						label="Technical Approach"
						v-model="formData.technicalApproach"
						placeholder="Describe the technologies and approach you will use to implement your project"
						:theme="theme"
					/>
				</div>

				<!-- Timeline Section -->
				<div class="space-y-4">
					<h3 class="text-xl font-semibold text-center">Project Timeline</h3>
					<hr class="border-[#5FFF16] w-1/3 my-2 mx-auto" />
					<TextArea
						id="timeline"
						label="Timeline"
						v-model="formData.timeline"
						placeholder="Break your project into phases and outline your milestones"
						:theme="theme"
					/>
				</div>

				<!-- Community Engagement Section -->
				<div class="space-y-4">
					<h3 class="text-xl text-center font-semibold">Community Engagement</h3>
					<hr class="border-[#5FFF16] w-1/3 my-2 mx-auto" />
					<TextArea
						id="communityEngagement"
						label="How will you engage with the community?"
						v-model="formData.communityEngagement"
						placeholder="Explain how you will interact with the community during the program"
						:theme="theme"
					/>
				</div>

				<!-- Additional Information Section -->
				<div class="space-y-4">
					<h3 class="text-xl text-center font-semibold">Additional Information</h3>
					<hr class="border-[#5FFF16] w-1/3 my-2 mx-auto" />
					<TextArea
						id="experience"
						label="Experience and Qualifications"
						v-model="formData.experience"
						placeholder="Describe your relevant skills, experience, and past work"
						:theme="theme"
					/>
					<InputField
						id="githubLink"
						label="GitHub Link (Optional)"
						type="url"
						v-model="formData.githubLink"
						placeholder="Link to your GitHub profile or relevant work"
						:theme="theme"
					/>
				</div>

				<!-- File Upload Section -->
				<div class="space-y-4">
					<h3 class="text-xl text-center font-semibold">Upload Proposal Document</h3>
					<hr class="border-[#5FFF16] w-1/3 my-2 mx-auto" />
					<div>
						<label
							for="fileUpload"
							:class="theme === 'light' ? 'text-light-text' : 'text-dark-text'"
							class="text-lg"
						>
							Upload your project proposal document
						</label>
						<input
							id="fileUpload"
							type="file"
							@change="handleFileUpload"
							class="w-full p-3 mt-2 rounded-lg border-2 focus:outline-none focus:ring-2"
							:class="
								theme === 'dark'
									? 'bg-light-buttonBackground text-light-buttonText border-dark-border focus:ring-2 focus:ring-green-400'
									: 'bg-dark-buttonBackground text-dark-buttonText border-light-border focus:ring-2 focus:ring-green-400'
							"
							accept=".pdf,.docx,.txt"
						/>
						<p
							v-if="formData.file"
							:class="theme === 'light' ? 'text-light-text' : 'text-dark-text'"
							class="mt-2"
						>
							File: {{ formData.file.name }}
						</p>
					</div>
				</div>

				<!-- Submit Section -->
				<div class="text-center">
					<button
						:class="submitButtonClass"
						type="submit"
						class="w-full py-3 mt-6 text-[#0B0F1F] font-semibold rounded-lg transition duration-300"
					>
						Submit Proposal
					</button>
				</div>
			</form>
		</div>
	</div>
<Footer :theme="theme" />
	</div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import InputField from '@/components/InputField.vue'
import TextArea from '@/components/TextArea.vue'
import Navbar from '@/components/Navbar.vue';
import Footer from '@/components/Footer.vue';
import { useRoute, useRouter } from 'vue-router';

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

const formData = ref({
	name: '',
	email: '',
	projectTitle: '',
	synopsis: '',
	technicalApproach: '',
	timeline: '',
	communityEngagement: '',
	experience: '',
	githubLink: '',
	file: null,
  	projectTitle: ""
})
const route = useRoute();
const router = useRouter();

const handleFileUpload = (event) => {
	const file = event.target.files[0]
	if (file) {
		formData.value.file = file
	}
}

const submitForm = () => {
	// Check if any required field is empty
	if (
		!formData.value.name ||
		!formData.value.email ||
		!formData.value.projectTitle ||
		!formData.value.synopsis ||
		!formData.value.technicalApproach ||
		!formData.value.timeline ||
		!formData.value.communityEngagement ||
		!formData.value.experience
	) {
		alert("Please fill in all required fields.");
		return; // Stop submission if any field is empty
	}
	console.log(formData.value)
	router.push('/profile');
}

const toggleTheme = () => {
	theme.value = theme.value === 'light' ? 'dark' : 'light'
	localStorage.setItem('theme', theme.value)
	document.documentElement.classList.toggle('dark', theme.value === 'dark')
}

onMounted(() => {
	document.documentElement.classList.toggle('dark', theme.value === 'dark')
	formData.value.projectTitle = route.params.title || route.query.title || "";
})
</script>

<style scoped>
input,
textarea {
	transition: all 0.3s ease;
}
/* input:focus,
textarea:focus {
	border-color: #5fff16;
	box-shadow: 0 0 10px rgba(95, 255, 22, 0.7);
} */
button:hover {
	transform: translateY(-2px);
}
</style>
