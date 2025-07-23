<template>
    <div>
        <div v-if="type === 'mc'">
            <form action="">
                <input type="text" placeholder="Question">
                <input type="text" placeholder="Correct Answer">
                <input v-for="n in 3" type="text" placeholder="Wrong Answer 1" :key="n">
            </form>
        </div>
        <div v-if="type === 'tf'">
            
        </div>
        <div v-if="type === 'n'">
            
        </div>
        <div v-if="type === 'dd'">
            
        </div>
    </div>
</template>

<script setup lang="ts">
const props = defineProps<{
    type: string
}>();
</script>

<style scoped>

</style>