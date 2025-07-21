<template>
    <div>
        <form @sumbit.prevent="">
            <input class="input mb-4 w-full" v-model="signupForm.email" type="email" placeholder="Email">
            <input class="input mb-4 w-full" v-model="signupForm.username" type="text" placeholder="Username">
            <input class="input mb-4 w-full" v-model="signupForm.password" type="password" placeholder="Password">
            <button class="btn w-full" type="submit">Sign Up</button>
        </form>
        <p>
            <NuxtLink to="/LogIn">Already have an account? Log In</NuxtLink>
        </p>
        <p v-if="errorMessage">{{ errorMessage }}</p>
    </div>
</template>

<script setup lang="ts">
const signupForm = reactive<UserForm>({
  email: '',
  password: '',
  username: '',
})

const errorMessage = ref<string>('')

</script>

<style scoped>

</style>