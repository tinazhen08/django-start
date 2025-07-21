declare global { 
    interface User {
        id: string 
        role: string 
        username: string
        email: string
    }

    interface UserForm {
        email: string
        password: string
        username: string
    }
}

export {}