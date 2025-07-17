<template>
    <div>
        <form @sumbit.prevent="">
            <input class="input mb-4 w-full" type="email" placeholder="Email">
            <input class="input mb-4 w-full" type="text" placeholder="Username">
            <input class="input mb-4 w-full" type="password" placeholder="Password">
            <button class="btn w-full" type="submit">Sign Up</button>
        </form>
        <NuxtLink to="/LogIn">Already have an account? Log In</NuxtLink>
    </div>
</template>

<script setup lang="ts">
import type { UserForm } from '../composables/types.js'

const signupForm = reactive<UserForm>({
  email: '',
  password: '',
  username: '',
})
</script>

<style scoped>

</style>