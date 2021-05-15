<template>
  <div>
    <input type="text" v-model="todoTitle" @keyup.enter="createTodo">
    <button @click="createTodo">Add</button>
  </div>
</template>

<script>
export default {
  name: 'TodoForm',
  // 공유할 데이터가 아니므로 state에서 안하고 여기서 data처리
  data: function () {
    return {
      todoTitle: '',
    }
  },
  methods: {
    createTodo: function () {
      const todoItem = {
        title: this.todoTitle,
        completed: false,
      }
      if (todoItem.title.trim()) {
        this.$store.dispatch('createTodo', todoItem)
      }
      this.todoTitle = '' // 초기화
    }
  }

}
</script>

<style>

</style>