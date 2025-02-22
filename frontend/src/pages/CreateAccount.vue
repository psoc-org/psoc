<template>
    <div :class="themeClass" class="min-h-screen flex items-center justify-center px-6 transition-colors duration-300">
      <!-- Navbar -->
      <nav :class="['w-full py-4 px-8 flex items-center justify-between fixed top-0 left-0 right-0 z-50 shadow', themeClass]" :style="{ backgroundColor: theme === 'light' ? 'white' : '#1a1a1a' }">
        <h1 class="text-3xl font-extrabold">PSoC</h1>
  
        <div class="absolute left-1/2 transform -translate-x-1/2 flex space-x-6">
          <router-link to="/" :class="linkClass" class="font-medium hover:opacity-75">Home</router-link>
          <router-link to="/about" :class="linkClass" class="font-medium hover:opacity-75">About</router-link>
          <router-link to="/vieworganizations" :class="linkClass" class="font-medium hover:opacity-75">View Organizations</router-link>
          <router-link to="/viewprojects" :class="linkClass" class="font-medium hover:opacity-75">View Projects</router-link>
        </div>
  
        <button @click="toggleTheme" :class="buttonClass" class="px-4 py-2 rounded-lg transition">
          {{ theme === "light" ? '🌙 Dark Mode' : '☀️ Light Mode' }}
        </button>
      </nav>
    <!-- Scrollable Container -->
    <div class="flex-grow w-full flex justify-center pt-24 pb-10 overflow-y-auto">
      <div class="w-full max-w-4xl p-8 rounded-xl shadow-lg hover:shadow-2xl transition" :class="cardClass">
        <h2 class="text-3xl font-bold text-center mb-6">Create a New Account</h2>

        <form @submit.prevent="handleRegister" class="space-y-4">
          <div>
            <label class="block text-lg font-medium mb-1">User Type</label>
            <select v-model="userType"
              class="w-full px-4 py-2 rounded-lg border focus:outline-none focus:ring-2 transition"
              :class="selectClass">
              <option value="mentor">Mentor</option>
              <option value="contributor">Contributor</option>
              <option value="organization">Organization</option>
            </select>
          </div>

          <div>
            <label class="block text-lg font-medium mb-1" for="name">Full Name</label>
            <input type="text" id="name" v-model="name" required class="w-full px-4 py-2 rounded-lg border focus:outline-none focus:ring-2 transition" :class="inputClass" />
          </div>

          <div v-if="userType === 'organization'">
            <label class="block text-lg font-medium mb-1" for="orgName">Organization Name</label>
            <input type="text" id="orgName" v-model="orgName" required class="w-full px-4 py-2 rounded-lg border focus:outline-none focus:ring-2 transition" :class="inputClass" />
          </div>

          <div>
            <label class="block text-lg font-medium mb-1" for="email">Email</label>
            <input type="email" id="email" v-model="email" required class="w-full px-4 py-2 rounded-lg border focus:outline-none focus:ring-2 transition" :class="inputClass" />
          </div>

          <div>
            <label class="block text-lg font-medium mb-1" for="password">Password</label>
            <input type="password" id="password" v-model="password" required class="w-full px-4 py-2 rounded-lg border focus:outline-none focus:ring-2 transition" :class="inputClass" />
          </div>

          <div v-if="userType === 'mentor'">
            <label class="block text-lg font-medium mb-1" for="expertise">Expertise Area</label>
            <input type="text" id="expertise" v-model="expertise" required class="w-full px-4 py-2 rounded-lg border focus:outline-none focus:ring-2 transition" :class="inputClass" />
          </div>

          <div v-if="userType === 'contributor'">
            <label class="block text-lg font-medium mb-1" for="skills">Skills</label>
            <input type="text" id="skills" v-model="skills" required class="w-full px-4 py-2 rounded-lg border focus:outline-none focus:ring-2 transition" :class="inputClass" />
          </div>

          <div v-if="userType === 'organization'">
            <label class="block text-lg font-medium mb-1" for="domain">Domain</label>
            <input type="text" id="domain" v-model="domain" required class="w-full px-4 py-2 rounded-lg border focus:outline-none focus:ring-2 transition" :class="inputClass" />
          </div>

          <div v-if="userType === 'organization'">
            <label class="block text-lg font-medium mb-1" for="about">About</label>
            <textarea id="about" v-model="about" rows="4" required class="w-full px-4 py-2 rounded-lg border focus:outline-none focus:ring-2 transition resize-none" :class="inputClass"></textarea>
          </div>

          <div v-if="userType === 'organization'">
            <label class="block text-lg font-medium mb-1" for="website">Website URL</label>
            <input type="text" id="website" v-model="website" required class="w-full px-4 py-2 rounded-lg border focus:outline-none focus:ring-2 transition" :class="inputClass" />
          </div>

          <div>
            <label class="block text-lg font-medium mb-1" for="github">GitHub URL</label>
            <input type="text" id="github" v-model="github" required class="w-full px-4 py-2 rounded-lg border focus:outline-none focus:ring-2 transition" :class="inputClass" />
          </div>

          <div>
            <label class="block text-lg font-medium mb-1" for="github">LinkedIn URL</label>
            <input type="text" id="github" v-model="linkedin" required class="w-full px-4 py-2 rounded-lg border focus:outline-none focus:ring-2 transition" :class="inputClass" />
          </div>

          <div v-if="userType === 'contributor'">
            <label class="block text-lg font-medium mb-1" for="resume">Resume</label>
            <input type="file" id="resume" @change="handleFileUpload" accept=".pdf,.doc,.docx,.txt"
              class="w-full px-4 py-2 rounded-lg border focus:outline-none focus:ring-2 transition cursor-pointer"
              :class="inputClass" />
          </div>

          <button type="submit" class="w-full py-3 rounded-lg shadow transition text-xl font-semibold" :class="buttonClass">
            Register
          </button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      theme: "light",
      userType: this.$route.query.type || "",
      name: "",
      email: "",
      password: "",
      expertise: "",
      skills: "",
      orgName: "",
      domain: "",
      about: "",
      website: "",
      github: "",
      linkedin: "",
      resume: null, // Ensure file is stored
    };
  },      
    computed: {
      themeClass() {
        return this.theme === "light" ? "bg-light-background text-light-text" : "bg-dark-background text-dark-text";
      },
      cardClass() {
        return this.theme === "light" ? "bg-light-cardBackground text-light-text" : "bg-dark-cardBackground text-dark-text";
      },
      buttonClass() {
        return this.theme === "light" ? "bg-light-buttonBackground text-light-buttonText" : "bg-dark-buttonBackground text-dark-buttonText";
      },
      linkClass() {
        return this.theme === "light" ? "text-light-link" : "text-dark-link";
      },
      inputClass() {
        return this.theme === "light" 
          ? "border-gray-300 focus:ring-light-accent text-black bg-white" 
          : "border-gray-600 focus:ring-dark-accent text-white bg-gray-800";
      },
      selectClass() {
        return this.theme === "light" ? "bg-light-cardBackground text-light-text border-gray-300 focus:ring-light-accent" : "bg-dark-cardBackground text-dark-text border-gray-600 focus:ring-dark-accent";
      }
    },
    methods: {
      handleRegister() {
        alert(`Registered as ${this.userType}: ${this.name}`);
        this.$router.push('/login');
      },
      toggleTheme() {
        this.theme = this.theme === "light" ? "dark" : "light";
        localStorage.setItem("theme", this.theme);
      },
      handleFileUpload(event) {
        const file = event.target.files[0];
        if (file) {
          this.resume = file; // Store the file object in data (optional)
          console.log("Uploaded file:", file.name);
        }
      }
    },
    created() {
      // Load theme preference
      this.theme = localStorage.getItem("theme") || "light";
  
      // Check if userType is passed in query parameters
      if (this.$route.query.type) {
        const validTypes = ["mentor", "contributor", "organization"];
        this.userType = validTypes.includes(this.$route.query.type) ? this.$route.query.type : "";
      }
    }
  };
  </script>
  