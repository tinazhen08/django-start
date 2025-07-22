<template>
  <div>
    <h1>{{ question.question }}</h1>
    <div>
        <ul class="space-y-3">
            <li v-for="(answer, index) in question.answer">
                <label for="">Black {{ index+1 }}</label>
                <select name="" id="">
                    <option value="" disabled>Please select an answer</option>
                    <option v-for="choice in shuffle([answer, ...question.incorrect[index] || []])" :value="choice">
                        {{ choice }}
                    </option>
                </select>
            </li>
        </ul>
        <button type="submit">Submit Answers</button>
    </div>
  </div>
</template>

<script setup lang="ts">
const props = defineProps<{
  question: Question;
}>();

const emit = defineEmits<{
  (e: "answerSelected", choice: string[]): void;
}>();

function selectAnswer(choice: string[]) {
  emit("answerSelected", choice);
} 
</script>

<style scoped></style>
