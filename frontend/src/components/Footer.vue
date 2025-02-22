<template>
	<footer class="py-6 mt-8 shadow-md transition-colors duration-300" :class="footerClass">
		<div class="container mx-auto text-center">
			<p class="text-sm">&copy; 2025 PSoC - Platform for Season of Commits</p>
			<p class="text-xs mt-1">Built with ❤️ by Team Askk for FOSS</p>
		</div>
	</footer>
</template>

<script>
export default {
	props: {
		theme: String,
	},
	computed: {
		footerClass() {
			return this.theme === 'light'
				? 'bg-light-navBackground text-light-navText'
				: 'bg-dark-navBackground text-dark-navText'
		},
	},
}
</script>
