<template>
    <div>
        <!-- <input type="text" placeholder="Enter Your Quiz Title" v-model="title"> -->
        <CreateQuestion :type="type"/>
    </div>
</template>

<script setup lang="ts">
/* const title = ref(''); */
const type = ref('dd'); 
</script>

<style scoped>

</style>