export interface User {
    id: number 
    role: string 
    username: string
    email: string
}

export interface UserForm {
    email: string
    password: string
    username: string
}

export interface Question {
    question: string
    answer: string[]
    incorrect: string[]
    quizId: number
}

export interface Quiz {
    id: number
    title: string
    creator: string
    //questions: Question[]
}

