<template>
  <div :class="themeClass" class="min-h-screen flex items-center justify-center px-6 transition-colors duration-300">
    <!-- Navbar -->
    <!-- <nav :class="navClass" class="w-full py-4 px-8 flex items-center justify-between fixed top-0 left-0 right-0 z-50 shadow">
      <router-link to="/" class="text-3xl font-extrabold cursor-pointer">PSoC</router-link>

      <div class="absolute left-1/2 transform -translate-x-1/2 flex space-x-6">
        <router-link to="/" :class="linkClass" class="font-medium hover:opacity-75">Home</router-link>
        <router-link to="/about" :class="linkClass" class="font-medium hover:opacity-75">About</router-link>
        <router-link to="/vieworganizations" :class="linkClass" class="font-medium hover:opacity-75">View Organizations</router-link>
        <router-link to="/viewprojects" :class="linkClass" class="font-medium hover:opacity-75">View Projects</router-link>
      </div>

      <button @click="toggleTheme" :class="buttonClass" class="px-4 py-2 rounded-lg transition">
        {{ theme === "light" ? "Dark Mode" : "Light Mode" }}
      </button>
    </nav> -->
    
    <div class="w-full max-w-md p-8 rounded-xl shadow-lg hover:shadow-2xl transition" :class="cardClass">
      <h2 class="text-3xl font-bold text-center mb-6">Create a New Account</h2>
      
      <form @submit.prevent="handleRegister" class="space-y-4">
        <div>
          <label class="block text-lg font-medium mb-1">User Type</label>
          <select v-model="userType" class="w-full px-4 py-2 rounded-lg border focus:outline-none focus:ring-2 transition" :class="inputClass">
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
        
        <button type="submit" class="w-full py-3 rounded-lg shadow transition text-xl font-semibold" :class="buttonClass">
          Register
        </button>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  
  data() {
    return {
      theme: "light",
      userType: "mentor",
      name: "",
      email: "",
      password: "",
      expertise: "",
      skills: "",
      orgName: ""
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
      return this.theme === "light" ? "border-gray-300 focus:ring-light-accent" : "border-gray-600 focus:ring-dark-accent";
    }
  },
  methods: {
    handleRegister() {
      alert(`Registered as ${this.userType}: ${this.name}`);
    },
    toggleTheme() {
      this.theme = this.theme === "light" ? "dark" : "light";
      localStorage.setItem("theme", this.theme);
    }
  },
  created() {
    this.theme = localStorage.getItem("theme") || "light";
  }
};
</script>
