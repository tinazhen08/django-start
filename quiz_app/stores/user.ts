import { defineStore } from 'pinia'
import type { User } from '../composables/types.js'

export const useStore = defineStore('user', () => {
    const user = ref<User | null>(null)
    const isSignedIn = ref(false)
    const errorMessage = ref<string>('')

    function signOut() {
        isSignedIn.value = false
        user.value = null
    }

    async function signUp(email: string, username: string, password: string) {
        errorMessage.value = ''


    }
})