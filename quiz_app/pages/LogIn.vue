<template>
    <div>
        <form @sumbit.prevent="handleLogin">
            <input class="input mb-4 w-full" v-model="loginForm.email" type="email" placeholder="Email">
            <input class="input mb-4 w-full" v-model="loginForm.password" type="password" placeholder="Password">
            <button class="btn w-full" type="submit">Log In</button>
        </form>
        <p>
            <NuxtLink to="/SignUp">Don't have an account yet? Sign Up</NuxtLink>
        </p>
        <p v-if="errorMessage">{{ errorMessage }}</p>
    </div>
</template>

<script setup lang="ts">
const loginForm = reactive<UserForm>({
  email: 'admin@admin.com',
  password: 'admin',
  username: '',
})

const errorMessage = ref('')

async function handleLogin(){
    const token = await requestEndpoint<{
        access: string;
        refresh: string;
    }>("/api/token/", "POST", {
            email: 'admin@admin.com', 
            password: 'admin',
        })
        console.log(token)
}

onMounted(async () => {
    await handleLogin();
});
</script>

<style scoped>

</style>