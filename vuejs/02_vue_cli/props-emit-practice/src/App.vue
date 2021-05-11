<template>
  <div id="app">
    <h1>App</h1>
    <p>appData: {{ appData }}</p>
    <!-- v-model;양방향바인딩. "appData"랑 연결하겠다 -->
    <input v-model="appData" type="text">
    <p>parentData: {{ parentData }}</p>
    <p>childData: {{ childData }}</p>
    <!-- :전달이름="전달값" -->
    <Parent
      :appData="appData"
      @parent-input="inputParent"
      @child-input="inputChild"
    />
  </div>
</template>

<script>
// import Parent from './components/Parent'  (@는 src를 의미)
import Parent from '@/components/Parent'

export default {
  name: 'App',
  data: function () {
    return {
      appData: '',
      parentData: '',
      childData: '',
    }
  },
  components: {
    Parent,
  },
  methods: {
    inputParent: function (data) {
      this.parentData = data
    },
    inputChild: function (data) {
      this.childData = data
    },
  }
}
</script>

<style>
#app {
  font-family: Verdana;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;

  width: 600px;
  border: 1px solid black;
  margin: auto;
  margin-top: 60px;
}
</style>
