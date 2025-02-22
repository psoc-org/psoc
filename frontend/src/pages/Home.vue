<template>
  <div :class="themeClass" class="min-h-screen transition-colors duration-300">
    
    <!-- Navbar -->
    <nav :class="navClass" class="w-full py-4 px-8 flex items-center justify-between fixed top-0 left-0 right-0 z-50 shadow">
      <h1 class="text-3xl font-extrabold">PSoC</h1>

      <!-- Center-aligned Navigation Links -->
      <div class="absolute left-1/2 transform -translate-x-1/2 flex space-x-6">
        <router-link v-if="!isLoggedIn" to="/login" :class="linkClass" class="font-medium hover:opacity-75">Login</router-link>
        <router-link v-else to="/" :class="linkClass" class="font-medium hover:opacity-75">Profile</router-link>
        <router-link to="/about" :class="linkClass" class="font-medium hover:opacity-75">About</router-link>
        <router-link to="/vieworganizations" :class="linkClass" class="font-medium hover:opacity-75">View Organizations</router-link>
        <router-link to="/viewprojects" :class="linkClass" class="font-medium hover:opacity-75">View Projects</router-link>
        <router-link to="/contributors" :class="linkClass" class="font-medium hover:opacity-75">Contributors</router-link>
        <router-link to="/mentors" :class="linkClass" class="font-medium hover:opacity-75">Mentors</router-link>
        <router-link to="/organizers" :class="linkClass" class="font-medium hover:opacity-75">Organizers</router-link>
      </div>

      <!-- Theme Toggle Button -->
      <button @click="toggleTheme" :class="buttonClass" class="px-4 py-2 rounded-lg transition">
        {{ theme === 'light' ? '🌙 Dark Mode' : '☀️ Light Mode' }}
      </button>
    </nav>

    <!-- Hero Section -->
    <header class="w-full text-center py-28 mt-16 rounded-b-2xl shadow-sm" :class="themeClass">
      <h3 class="text-4xl md:text-[4rem] font-bold">PSoC</h3>
      <h3 class="text-4xl md:text-[4rem] font-bold">Platform for Season of Commits</h3>
      <p class="text-2xl md:text-[2rem] mt-4">Empowering Open-Source</p>
      <router-link to="/login">
        <button class="mt-6 px-6 py-3 text-xl rounded-lg shadow transition" :class="buttonClass">
          Login to PSoC
        </button>
      </router-link>
    </header>

    <!-- Features Section (Full Width) -->
    <section id="about" class="w-full py-20 px-12">
      <h3 class="text-[2rem] font-bold text-center">Why PSoC?</h3>
      <div class="grid md:grid-cols-3 gap-10 mt-12">
        <div 
          v-for="(feature, index) in features" 
          :key="index" 
          class="p-10 rounded-xl shadow-lg hover:shadow-2xl transition text-left"
          :class="cardClass"
        >
          <h4 class="text-3xl font-semibold flex items-center">
            <span class="mr-3">{{ feature.icon }}</span> {{ feature.title }}
          </h4>
          <p class="mt-5 text-lg">{{ feature.description }}</p>
        </div>
      </div>
    </section>

    <section id="updates" class="w-full py-20 px-12">
      <h3 class="text-[2rem] font-bold text-center">Updates</h3>

      <div class="grid md:grid-cols-2 gap-12 mt-12">
        <div class="p-8 rounded-xl shadow-lg hover:shadow-2xl transition h-64 overflow-y-auto scrollbar-thin" :class="cardClass">
          <h4 class="text-2xl font-semibold">📢 Announcements</h4>
          <ul class="mt-4 text-lg list-disc pl-6">
            <li v-for="(announcement, index) in updates.announcements" :key="index">{{ announcement }}</li>
          </ul>
        </div>
        
        <div class="p-8 rounded-xl shadow-lg hover:shadow-2xl transition h-64 overflow-y-auto scrollbar-thin" :class="cardClass">
          <h4 class="text-2xl font-semibold">📅 Timeline</h4>
          <ul class="mt-4 text-lg list-disc pl-6">
            <li v-for="(item, index) in updates.timeline" :key="index"><b>{{ item.date }}</b> - {{ item.event }}</li>
          </ul>
        </div>
      </div>
      
      <div class="grid md:grid-cols-2 gap-12 mt-12">
        <div class="p-8 rounded-xl shadow-lg hover:shadow-2xl transition h-64 overflow-y-auto scrollbar-thin" :class="cardClass">
          <h4 class="text-2xl font-semibold">📖 Read Our Blogs</h4>
          <ul class="mt-4 text-lg list-disc pl-6">
            <li v-for="(blog, index) in updates.blogs" :key="index">🚀 <b>{{ blog.title }}</b> - {{ blog.description }}</li>
          </ul>
        </div>
        
        <div class="p-8 rounded-xl shadow-lg hover:shadow-2xl transition h-64 overflow-y-auto scrollbar-thin" :class="cardClass">
          <h4 class="text-2xl font-semibold">🔗 Follow Us On</h4>
          <ul class="mt-4 text-lg list-disc pl-6">
            <li v-for="(link, index) in updates.socialLinks" :key="index">{{ link.icon }} <b>{{ link.platform }}</b> - <a :href="link.url" target="_blank" class="text-blue-500 hover:underline">{{ link.description }}</a></li>
          </ul>
        </div>
      </div>
    </section>


    <!-- Call to Action -->
    <section id="apply" class="text-center py-16 mx-6 rounded-2xl shadow-sm" :class="themeClass">
      <h3 class="text-[2rem] font-bold">Start Your Open-Source Journey, Create a New Account.</h3>
      <p class="text-lg mt-4">Join PSoC in a role that suits you best - as a Contributor, Mentor, or Organizer.</p>

      <div class="grid md:grid-cols-3 gap-10 text-left w-full py-20 px-12">
        <!-- Contributor Section -->
        <div class="p-6 rounded-lg shadow-md transition hover:shadow-lg" :class="cardClass">
          <h4 class="text-2xl font-semibold">🚀 Contributor</h4>
          <p class="mt-2 text-sm">
            Gain hands-on experience in open-source projects, collaborate with mentors, and enhance your skills.
          </p>
          <button 
            class="mt-4 px-5 py-3 rounded-lg shadow transition" 
            :class="buttonClass" 
            @click="navigateToCreateAccount('contributor')"
          >
            Apply as Contributor
          </button>
        </div>

        <!-- Mentor Section -->
        <div class="p-6 rounded-lg shadow-md transition hover:shadow-lg" :class="cardClass">
          <h4 class="text-2xl font-semibold">🧑‍🏫 Mentor</h4>
          <p class="mt-2 text-sm">
            Guide contributors, review proposals, and help shape the next generation of open-source enthusiasts.
          </p>
          <button 
            class="mt-4 px-5 py-3 rounded-lg shadow transition" 
            :class="buttonClass" 
            @click="navigateToCreateAccount('mentor')"
          >
            Apply as Mentor
          </button>
        </div>

        <!-- Organizer Section -->
        <div class="p-6 rounded-lg shadow-md transition hover:shadow-lg" :class="cardClass">
          <h4 class="text-2xl font-semibold">📅 Organizer</h4>
          <p class="mt-2 text-sm">
            Manage projects, oversee mentor-contributor interactions, and ensure the success of PSoC.
          </p>
          <button 
            class="mt-4 px-5 py-3 rounded-lg shadow transition" 
            :class="buttonClass" 
            @click="navigateToCreateAccount('organization')"
          >
            Apply as Organizer
          </button>
        </div>
      </div>
    </section>


    <!-- Footer -->
    <footer class="text-center py-4 mt-8 shadow-sm" :class="navClass">
      &copy; 2025 PSoC - Platform for Season of Commits - by Team Askk for FOSS
    </footer>
  </div>
</template>

<script>
export default {
  data() {
    return {
      theme: "light",
      features: [
        { title: "Mentorship", icon: "🎓", description: "Work with experienced mentors in the open-source community." },
        { title: "Networking", icon: "🌎", description: "Connect with open-source enthusiasts and organizations globally." },
        { title: "Experience", icon: "💡", description: "Gain real-world experience by contributing to impactful projects." }
      ],
      updates: {
        announcements: [
          "PSoC 2025 applications are now live! Apply today.",
          "New mentorship programs introduced for this season.",
          "New project categories added—check them out!"
        ],
        timeline: [
          { date: "Jan 2025", event: "Applications Open" },
          { date: "March 2025", event: "Application Deadline" },
          { date: "April 2025", event: "Project Selection & Community Meetup" },
          { date: "May 2025", event: "Coding Period Begins" },
          { date: "Aug 2025", event: "PSoC Wrap-up & Celebrations" }
        ],
        blogs: [
          { title: "Getting Started with Open-Source Contributions", description: "A beginner-friendly guide." },
          { title: "How Mentors Can Shape Open-Source", description: "Insights from industry leaders." },
          { title: "Building Scalable Projects for PSoC", description: "Best practices for contributors." }
        ],
        socialLinks: [
          { platform: "Twitter", icon: "🐦", url: "https://twitter.com/fossunited", description: "Stay updated with the latest news." },
          { platform: "LinkedIn", icon: "💼", url: "https://www.linkedin.com/company/fossunited", description: "Connect with professionals and mentors." },
          { platform: "GitHub", icon: "🐙", url: "https://github.com/fossunited", description: "Explore projects and repositories." },
          { platform: "Website", icon: "💬", url: "https://fossunited.org", description: "Join community discussions and networking." },
          { platform: "Email", icon: "📧", url: "mailto:foundation@fossunited.org", description: "Having any other doubts or queries, do mail us." }
        ]
      }
    };
  },
  computed: {
    themeClass() {
      return this.theme === "light" ? "bg-light-background text-light-text" : "bg-dark-background text-dark-text";
    },
    navClass() {
      return this.theme === "light" ? "bg-light-navBackground text-light-navText" : "bg-dark-navBackground text-dark-navText";
    },
    linkClass() {
      return this.theme === "light" ? "text-light-link" : "text-dark-link";
    },
    buttonClass() {
      return this.theme === "light" ? "bg-light-buttonBackground text-light-buttonText" : "bg-dark-buttonBackground text-dark-buttonText";
    },
    cardClass() {
      return this.theme === "light" ? "bg-light-cardBackground text-light-text" : "bg-dark-cardBackground text-dark-text";
    }
  },
  methods: {
    toggleTheme() {
      this.theme = this.theme === "light" ? "dark" : "light";
      localStorage.setItem("theme", this.theme);
    },
    navigateToCreateAccount(userType) {
      this.$router.push({ path: "/signup", query: { type: userType } });
    }
  },
  created() {
    this.theme = localStorage.getItem("theme") || "light";
  },
  watch: {
    theme(newTheme) {
      document.documentElement.classList.toggle("dark", newTheme === "dark");
    }
  }
};
</script>