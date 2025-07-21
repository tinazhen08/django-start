<template>
    <div>
        <h1>{{ question.question }}</h1>
        
    </div>
</template>

<script setup lang="ts">
const props = defineProps<{
    question: Question
}>();


</script>

<style scoped>

</style>