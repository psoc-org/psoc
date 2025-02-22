<template>
	<div class="flex flex-col">
		<label :for="id" :class="labelClass" class="text-lg font-semibold">{{ label }}</label>
		<textarea
			:id="id"
			:value="modelValue"
			@input="$emit('update:modelValue', $event.target.value)"
			:placeholder="placeholder"
			:class="[inputClass, { 'border-red-500': error }]"
			class="p-3 rounded-lg transition-all duration-300 mt-2"
		></textarea>
		<p v-if="error" class="text-red-500 text-sm">{{ error }}</p>
	</div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
	modelValue: String,
	label: String,
	id: String,
	placeholder: String,
	error: String,
	theme: String,
})

const inputClass = computed(() =>
	props.theme === 'light'
		? 'bg-light-navBackground text-light-text border-light-border focus:ring-2 focus:ring-green-400'
		: 'bg-dark-navBackground text-dark-text border-dark-border focus:ring-2 focus:ring-green-400',
)

const labelClass = computed(() => (props.theme === 'light' ? 'text-light-text' : 'text-dark-text'))
</script>
