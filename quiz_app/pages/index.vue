<template>
    <div>
        
    </div>
</template>

<script setup lang="ts">
const config = useRuntimeConfig()

async function handleLogin(){
    const token = await $fetch(config.public.apiBase + "/api/token/", {
        method: "POST",
        body: {
            email: 'admin@admin.com', 
            password: 'admin',
        },
    });
    console.log(token);
}

onMounted(async () => {
    await handleLogin();
});
</script>

<style scoped>

</style>