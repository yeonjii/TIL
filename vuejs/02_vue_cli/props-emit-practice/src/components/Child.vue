<template>
  <div id="child">
    <h1>Child</h1>
    <p>childData: {{ childData }}</p>
    <!-- @이벤트이름="실행할 메소드" -->
    <!-- input이라는 이벤트가 발생하면 inputChildData라는 메소드가 실행 -->
    <input v-model="childData" type="text" @input="inputChildData">
    <p>appData: {{ appData }}</p>
    <p>parentData: {{ parentData }}</p>
  </div>
</template>

<script>
export default {
  name: 'Child',
  data: function () {
    return {
      childData: '',
    }
  },
  props: {
    appData: String,
    parentData: String,
  },
  methods: {
    inputChildData() {
      // 데이터를 보낼때는 $emit 을 사용
      this.$emit('child-input', this.childData)
    }
  },
}
</script>

<style>
#child {
  border: 1px solid blue;
  margin: 20px;
}
</style>