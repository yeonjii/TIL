<template>
  <div>
    <!-- 클래스바인딩이 객체로 들어갈 경우, 키의 boolean값에 따라서 활성화 여부를 설정함 -->
    <!-- completed라는 클래스 값은 todo.completed값에 따라 on-off가 됨 -->
    <span
      @click="updateTodo(todo)"
      :class="{completed: todo.completed}"
      style="margin-right:10px;"
    >{{ todo.title }}</span>
    <button @click="deleteTodo(todo)">Delete</button>
  </div>
</template>

<script>
import { mapActions } from 'vuex'
export default {
  name: 'TodoListItem',
  props: {
    todo: {
      type: Object,
    }
  },
  methods: {
    // TodoListItem 컴포넌트에서 actions의 'deleteTodo'라는 메서드를 호출한다.
    // deleteTodo: function () {
    //   this.$store.dispatch('deleteTodo', this.todo)
    // },
    // updateTodo: function () {
    //   this.$store.dispatch('updateTodo', this.todo)
    // },

    // ✔ this.todo같은 payload가 있는 경우, 템플릿에서 호출할 때 인자로 넣어줘야함.
    ...mapActions([
      'deleteTodo',
      'updateTodo',
    ])
  },
}
</script>

<style scoped>
  .completed {
    text-decoration: line-through;
  }
</style>