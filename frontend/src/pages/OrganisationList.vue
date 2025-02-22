<template>
  <nav :class="navClass" class="w-full py-4 px-8 flex items-center justify-between fixed top-0 left-0 right-0 z-50 shadow">
    <h1 class="text-3xl font-extrabold">PSoC</h1>

    <button @click="toggleTheme" :class="buttonClass" class="px-4 py-2 rounded-lg transition">
      {{ theme === 'light' ? '🌙 Dark Mode' : '☀️ Light Mode' }}
    </button>
  </nav>

  <div :class="themeClass" class="min-h-screen flex flex-col items-center p-10 transition-colors duration-300">
    <h1 :class="linkClass" class="text-3xl font-bold mb-8 mt-12">Organization Approvals</h1>

    <div :class="themeClass" class="w-full max-w-5xl space-y-6">
      <Card v-for="org in organizations" :key="org.id" :class="cardClass">
        <CardHeader>
          <CardTitle class="text-3xl mb-4">{{ org.name }}</CardTitle>
          <CardDescription class="opacity-75">{{ org.description }}</CardDescription>
        </CardHeader>

        <CardContent  class="opacity-80 space-y-2">
          <p><span class="font-semibold">Head:</span> {{ org.head }}</p>
          <p><span class="font-semibold">Founded:</span> {{ org.founded }}</p>
          <p><span class="font-semibold">Location:</span> {{ org.location }}</p>
        </CardContent>

        <CardFooter class="flex ml-2 mt-4">
          <Button variant="default" :class="buttonClass" class="ml-2" @click="viewOrganization(org.id)">
            View Organization
          </Button>
          <Button variant="default" class="bg-green-500 ml-2 hover:bg-green-400" @click="approveOrganization(org.id)">
            Approve
          </Button>
          <Button variant="destructive" class="bg-red-600 text-white ml-2 hover:bg-red-400" @click="declineOrganization(org.id)">
            Decline
          </Button>
        </CardFooter>
      </Card>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();
const theme = ref(localStorage.getItem("theme") || "light");

const themeClass = computed(() => theme.value === "light" ? "bg-light-background text-light-text" : "bg-dark-background text-dark-text");
const navClass = computed(() => theme.value === "light" ? "bg-light-navBackground text-light-navText" : "bg-dark-navBackground text-dark-navText");
const linkClass = computed(() => theme.value === "light" ? "text-light-link" : "text-dark-link");
const buttonClass = computed(() => theme.value === "light" ? "bg-light-buttonBackground text-light-buttonText border" : "bg-dark-buttonBackground text-dark-buttonText border");
const cardClass = computed(() => theme.value === "light" ? "bg-light-cardBackground text-light-text" : "bg-dark-cardBackground text-light-text");

const organizations = ref([
  { id: 1, name: "Python Software Foundation", head: "Guido van Rossum", founded: "2001", location: "USA", description: "A non-profit organization that manages the Python programming language." },
  { id: 2, name: "OpenAI", head: "Sam Altman", founded: "2015", location: "USA", description: "An AI research lab focused on creating beneficial AI systems." }
]);

const viewOrganization = (id) => {
  router.push(`/organization/${id}`);
};

const approveOrganization = (id) => {
  console.log(`Organization ${id} approved ✅`);
};

const declineOrganization = (id) => {
  console.log(`Organization ${id} declined ❌`);
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
