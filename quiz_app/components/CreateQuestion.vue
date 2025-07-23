<template>
    <div>
        <div v-if="type === 'mc'">
            <form action="">
                <input type="text" placeholder="Question"/>
                <input type="text" placeholder="Correct Answer"/>
                <input v-for="n in 3" type="text" placeholder="Wrong Answer" :key="n"/>
            </form>
        </div>
        <div v-if="type === 'tf'">
            <form>
                <input type="text" placeholder="Question"/>
                <input type="radio" id="True" name="tf" value="True"/>
                <label for="True">True</label><br/>
                <input type="radio" id="False" name="tf" value="False"/>
                <label for="False">False</label><br/>
                <input type="submit" value="Submit"/>
            </form>
        </div>
        <div v-if="type === 'n'">
            <form action="">
                <input type="text" placeholder="Question"/>
                <input type="text" placeholder="Correct Answer"/>
            </form>
        </div>
        <div v-if="type === 'dd'">
            <!-- <form action="">
                <input type="text" placeholder="Question">
                <textarea name="" id=""></textarea>
            </form> -->
            <form @sumbit.prevent="">
                <div v-for="item in array">
                    <input v-if="item === 'q'" type="text" placeholder="Question"/>
                    <input v-if="item === 'b'" type="text" placeholder="Blank" :key="num" disabled>
                </div>
                <button @click.prevent="array.push('b', 'q');  num ++">Add a Blank</button>
                <div v-for="item in array">
                    <p v-if="item === 'b'">Blank: {{ num }}</p>
                    <input v-if="item === 'b'" type="text" placeholder="Blank - answer" :key="'answer' + num" />
                    <div class="incorrect" v-if="item === 'b'">
                        <input v-for="index of n" type="text" placeholder="Incorrect Answer" :key="'incorrect' + num"/>
                        <button v-if="n < 4" @click.prevent="n++">Add Incorrect Answers</button>
                    </div>
                </div>
            </form>
        </div>
    </div>
</template>

<script setup lang="ts">
const props = defineProps<{
    type: string
}>();

const n = ref(2);
const num = ref(0);
const array = reactive<string[]>(['q']);

</script>

<style scoped>

</style>