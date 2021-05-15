<template>
  <div>
    <TodoListItem
      v-for="(todo, idx) in todos"
      :key="idx"
      :todo="todo"
    />
    <!-- todo를 TodoListItem.vue에서 사용할 수 있도록 내려보냄 -->
  </div>
</template>

<script>
import { mapState } from 'vuex'
import TodoListItem from '@/components/TodoListItem'

export default {
  name: 'TodoList',
  components: {
    TodoListItem,
  },
  // computed는 계산된 결과값만 사용하기 때문에 반드시 리턴값이 있어야 함
  computed: {
    // todos: function () {
    //   return this.$store.state.todos
    // }
    ...mapState(['todos',])
  },
}
</script>

<style>

</style>