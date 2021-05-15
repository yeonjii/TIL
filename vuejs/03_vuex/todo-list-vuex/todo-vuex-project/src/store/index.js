import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from "vuex-persistedstate";

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  state: {
    todos: []
  },
  mutations: {  // state(상태, 데이터) 수정은 여기서!
    CREATE_TODO: function (state, todoItem) {
      // console.log(state)
      state.todos.push(todoItem)
    },
    DELETE_TODO: function (state, todoItem) {
      //  1. todoItem이 첫번째로 만나는 요소의 index를 가져온다.
      const index = state.todos.indexOf(todoItem)
      // 2. 해당 인덱스 1개만 삭제하고 나머지 요소를 토대로 새로운 배열을 생성한다.
      state.todos.splice(index, 1)  // 특정 인덱스값부터 1개의 요소를 삭제하고 새로운 배열을 반환
    },
    UPDATE_TODO: function (state, todoItem) {
      state.todos = state.todos.map((todo) => {
        if (todo === todoItem) {
          return {...todo, completed: !todo.completed }  // 객체가 나와야 함
        }
        return todo
      })
    },
  },
  actions: {
    createTodo: function ({ commit }, todoItem) {
      // console.log(context)
      commit('CREATE_TODO', todoItem)  // mutations의 CREATE_TODO 호출
    },
    deleteTodo: function ({ commit }, todoItem) {
      commit('DELETE_TODO', todoItem)
    },
    updateTodo: function ({ commit }, todoItem) {
      commit('UPDATE_TODO', todoItem)
    },
  },
  getters: {
    // getters는 state(상태값)을 기준으로 계산하기 때문에 인자로 state 필요
    completedTodosCount: function (state) {
      // 최종적으로 값을 사용하기 때문에 리턴값 필요
      return state.todos.filter((todo) => {
        return todo.completed === true
      }).length
    },
    uncompletedTodosCount: function (state) {
      return state.todos.filter((todo) => {
        return todo.completed === false
      }).length
    },
  },
  modules: {
  }
})
