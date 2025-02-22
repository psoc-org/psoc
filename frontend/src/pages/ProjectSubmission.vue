<template>
  <!-- Navigation Bar -->
  <nav :class="navClass" class="w-full py-4 px-8 flex items-center justify-between fixed top-0 left-0 right-0 z-50 shadow-lg">
    <h1 class="text-3xl font-extrabold">PSoC</h1>

    <button @click="toggleTheme" :class="buttonClass" class="px-4 py-2 rounded-lg transition duration-300 transform hover:scale-105">
      {{ theme === 'light' ? '🌙 Dark Mode' : '☀️ Light Mode' }}
    </button>
  </nav>
 <div :class="themeClass" class="min-h-screen flex justify-center items-center p-10 mt-12">
   <div class="w-full max-w-4xl mx-auto p-10 rounded-xl shadow-xl" :class="cardClass">
     <h1 class="text-3xl font-semibold text-primary text-center mb-8">Submit Your Organization's Project</h1>
     
     <form class="space-y-8">
       <!-- Organization Details Section -->
       <div class="space-y-4">
         <h3 class="text-2xl text-center font-semibold text-text">Organization Information</h3>
         <hr class="border-primary w-1/3 my-2 mx-auto">
         
         <InputField id="organizationName" label="Organization Name" v-model="formData.organizationName" :theme="theme" />
         <InputField id="contactEmail" label="Contact Email" type="email" v-model="formData.contactEmail" :theme="theme"/>
         <InputField id="website" label="Website" type="url" v-model="formData.website" :theme="theme"/>
       </div>

       <!-- Project Details Section -->
       <div class="space-y-4">
         <h3 class="text-2xl text-center font-semibold text-text">Project Details</h3>
         <hr class="border-primary w-1/3 my-2 mx-auto">

         <InputField id="projectTitle" label="Project Title" v-model="formData.projectTitle" :theme="theme"/>
         <TextareaField id="projectDescription" label="Project Description" v-model="formData.projectDescription" :theme="theme" />
         <TextareaField id="projectBenefits" label="Benefits to Students" v-model="formData.projectBenefits" :theme="theme"/>
         <InputField id="skillsRequired" label="Skills Required" v-model="formData.skillsRequired" :theme="theme"/>
       </div>

       <!-- Timeline Section -->
       <div class="space-y-4">
         <h3 class="text-2xl text-center font-semibold text-text">Project Timeline</h3>
         <hr class="border-primary w-1/3 my-2 mx-auto">
         <TextareaField id="timeline" label="Project Timeline" v-model="formData.timeline"  :theme="theme"/>
       </div>

       <!-- Student Mentorship Section -->
       <div class="space-y-4">
         <h3 class="text-2xl text-center font-semibold text-text">Student Mentorship</h3>
         <hr class="border-primary w-1/3 my-2 mx-auto">
         <TextareaField id="mentorDetails" label="Mentor Details" v-model="formData.mentorDetails" :theme="theme"/>
         <TextareaField id="mentorExperience" label="Mentor's Experience" v-model="formData.mentorExperience"  :theme="theme"/>
       </div>

       <!-- Additional Information Section -->
       <div class="space-y-4">
         <h3 class="text-2xl text-center font-semibold text-text">Additional Information</h3>
         <hr class="border-primary w-1/3 my-2 mx-auto">
         <TextareaField id="additionalInfo" label="Additional Information (Optional)" v-model="formData.additionalInfo" :theme="theme" />
       </div>

       <!-- Submit Section -->
       <div class="text-center">
         <button type="submit" @click="submitForm" :class="buttonClass" class="w-full py-3 mt-6 bg-primary text-buttonText font-semibold rounded-lg hover:bg-tertiary transition duration-300">
           Submit Project
         </button>
       </div>
     </form>
   </div>
 </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';
import InputField from '@/components/InputField.vue';
import TextareaField from '@/components/TextArea.vue';

const formData = ref({
 organizationName: '',
 contactEmail: '',
 website: '',
 projectTitle: '',
 projectDescription: '',
 projectBenefits: '',
 skillsRequired: '',
 timeline: '',
 mentorDetails: '',
 mentorExperience: '',
 additionalInfo: '',
});

const theme = ref(localStorage.getItem("theme") || "light");
const themeClass = computed(() => theme.value === "light" ? "bg-light-background text-light-text" : "bg-dark-background text-dark-text");
const navClass = computed(() => theme.value === "light" ? "bg-light-navBackground text-light-navText" : "bg-dark-navBackground text-dark-navText");
const containerClass = computed(() => theme.value === "light" ? "bg-light-background" : "bg-dark-background");
const cardClass = computed(() => theme.value === "light" ? "bg-light-cardBackground" : "bg-dark-cardBackground");
const textClass = computed(() => theme.value === "light" ? "text-light-text" : "text-dark-text");
const buttonClass = computed(() => theme.value === "light" ? "bg-light-buttonBackground text-light-buttonText border" : "bg-dark-buttonBackground text-dark-buttonText border");

const submitForm = (event) => {
 event.preventDefault();
 console.log(formData.value);
};

const toggleTheme = () => {
 theme.value = theme.value === "light" ? "dark" : "light";
 localStorage.setItem("theme", theme.value);
 document.documentElement.classList.toggle("dark", theme.value === "dark");
};

onMounted(() => {
 document.documentElement.classList.toggle("dark", theme.value === "dark");
});
</script>

<style scoped>
input,
textarea {
 transition: all 0.3s ease;
}
input:focus,
textarea:focus {
 border-color: var(--primary);
 box-shadow: 0 0 10px rgba(95, 255, 22, 0.7);
}
button:hover {
 transform: translateY(-2px);
}
</style>
