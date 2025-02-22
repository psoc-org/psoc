<template>
  <!-- Navigation Bar -->
  <nav :class="navClass" class="w-full py-4 px-8 flex items-center justify-between fixed top-0 left-0 right-0 z-50 shadow-lg">
    <h1 class="text-3xl font-extrabold">PSoC</h1>

    <button @click="toggleTheme" :class="buttonClass" class="px-4 py-2 rounded-lg transition duration-300 transform hover:scale-105">
      {{ theme === 'light' ? '🌙 Dark Mode' : '☀️ Light Mode' }}
    </button>
  </nav>

  <!-- Page Container -->
  <div :class="themeClass" class="min-h-screen flex justify-center items-center p-10 transition-all duration-500 mt-12">
    <div :class="cardClass" class="w-full max-w-4xl mx-auto p-10 rounded-xl shadow-2xl">
      <h2 class="text-3xl font-bold text-center mb-6">Create Your Organization</h2>
      
      <form @submit.prevent="submitForm" class="space-y-6">
        <!-- Organization Details -->
        <div class="space-y-5">
          <h3 class="text-2xl font-semibold text-center">Organization Details</h3>
          <hr class="w-1/3 my-3 mx-auto border-t-2 border-current">
          
          <InputField id="organizationName" label="Organization Name" v-model="formData.organizationName" :error="errors.organizationName" :theme="theme" />
          <TextareaField id="organizationDescription" label="Organization Description" v-model="formData.organizationDescription" :error="errors.organizationDescription" :theme="theme"/>
        </div>

        <!-- Contact Details -->
        <div class="space-y-5">
          <h3 class="text-2xl font-semibold text-center">Contact Information</h3>
          <hr class="w-1/3 my-3 mx-auto border-t-2 border-current">
          
          <InputField id="contactEmail" type="email" label="Email" v-model="formData.contactEmail" :error="errors.contactEmail" :theme="theme"/>
          <InputField id="website" type="url" label="Website" v-model="formData.website" :theme="theme"/>
        </div>

        <!-- Social Media Links -->
        <div class="space-y-5">
          <h3 class="text-2xl font-semibold text-center">Social Media Links</h3>
          <hr class="w-1/3 my-3 mx-auto border-t-2 border-current">
          
          <InputField id="linkedin" type="url" label="LinkedIn" v-model="formData.linkedin" :theme="theme" />
          <InputField id="github" type="url" label="GitHub" v-model="formData.github" :theme="theme"/>
        </div>

        <!-- Organization Address -->
        <div class="space-y-5">
          <h3 class="text-2xl font-semibold text-center">Organization Address</h3>
          <hr class="w-1/3 my-3 mx-auto border-t-2 border-current">
          
          <InputField id="address" label="Address" v-model="formData.address" :theme="theme"/>
          <InputField id="country" label="Country" v-model="formData.country" :theme="theme"/>
        </div>

        <!-- Additional Information -->
        <div class="space-y-5">
          <h3 class="text-2xl font-semibold text-center">Additional Information</h3>
          <hr class="w-1/3 my-3 mx-auto border-t-2 border-current">
          
          <TextareaField id="additionalInfo" label="Additional Information (Optional)" v-model="formData.additionalInfo" :theme="theme" />
        </div>

        <!-- Submit Button -->
        <div class="text-center">
          <button type="submit" :class="submitButtonClass" class="px-6 py-3 rounded-lg font-semibold transition-transform duration-300 hover:scale-105">
            Create Organization
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

// Theme Management
const theme = ref(localStorage.getItem("theme") || "light");

const themeClass = computed(() => theme.value === "light" ? "bg-light-background text-light-text" : "bg-dark-background text-dark-text");
const navClass = computed(() => theme.value === "light" ? "bg-light-navBackground text-light-navText" : "bg-dark-navBackground text-dark-navText");
const buttonClass = computed(() => theme.value === "light" ? "bg-light-buttonBackground text-light-buttonText border" : "bg-dark-buttonBackground text-dark-buttonText border");
const cardClass = computed(() => theme.value === "light" ? "bg-light-cardBackground text-light-text" : "bg-dark-cardBackground text-dark-text");
const submitButtonClass = computed(() => theme.value === "light" ? "bg-light-buttonBackground text-light-buttonText shadow-lg" : "bg-dark-buttonBackground text-dark-buttonText shadow-lg");

// Form Data
const formData = ref({
  organizationName: '',
  organizationDescription: '',
  contactEmail: '',
  website: '',
  linkedin: '',
  github: '',
  address: '',
  country: '',
  additionalInfo: ''
});

// Validation Errors
const errors = ref({});

// Form Submission & Validation
const submitForm = () => {
  errors.value = {};
  if (!formData.value.organizationName.trim()) {
    errors.value.organizationName = "Organization name is required.";
  }
  if (!formData.value.organizationDescription.trim()) {
    errors.value.organizationDescription = "Description is required.";
  }
  if (!formData.value.contactEmail.match(/^[\w-.]+@([\w-]+\.)+[\w-]{2,4}$/)) {
    errors.value.contactEmail = "Enter a valid email.";
  }

  if (Object.keys(errors.value).length === 0) {
    console.log("Form Submitted:", formData.value);
    alert(" Organization Created Successfully!");
  }
};

// Theme Toggle
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
input, textarea, button {
  transition: all 0.3s ease-in-out;
}
input:focus, textarea:focus {
  box-shadow: 0 0 10px rgba(95, 255, 22, 0.7);
}
button:hover {
  transform: translateY(-2px);
}
</style>
