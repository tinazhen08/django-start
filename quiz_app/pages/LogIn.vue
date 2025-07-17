<template>
    <div>
        <form @sumbit.prevent="">
            <input class="input mb-4 w-full" type="email" placeholder="Email">
            <input class="input mb-4 w-full" type="password" placeholder="Password">
            <button class="btn w-full" type="submit">Log In</button>
        </form>
        <NuxtLink to="/SignUp">Don't have an account yet? Sign Up</NuxtLink>
    </div>
</template>

<script setup lang="ts">
import type { UserForm } from '../composables/types.js'

const loginForm = reactive<UserForm>({
  email: '',
  password: '',
  username: '',
})
</script>

<style scoped>

</style>