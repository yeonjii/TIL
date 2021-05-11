<template>
  <div id="parent">
    <h1>Parent</h1>
    <p>parentData: {{ parentData }}</p>
    <input v-model="parentData" type="text" @input="inputParentData">
    <p>appData: {{ appData }}</p>
    <p>childData: {{ childData }}</p>
    <Child
      :appData="appData"
      :parentData="parentData"
      @child-input="inputChild"
    />
    <!-- Child가 @child-input 이벤트를 보내면 Parent가 "inputChild" 메소드를 실행-->
  </div>
</template>

<script>
// import Child from './Child'
import Child from '@/components/Child'

export default {
  name: 'Parent',
  data: function () {
    return {
      parentData: '',
      childData: '',
    }
  },
  props: {
    appData: String,
  },
  components: {
    Child,
  },
  methods: {
    inputChild: function (data) {
      // data는 payload 안에 들어있는 Child에서 보낸 data를 의미
      this.childData = data
      this.$emit('child-input', this.childData)
    },
    inputParentData() {
      // parent-input 이라는 이벤트랑 parentData라는 데이터를 상위컴포넌트로 보냄
      this.$emit('parent-input', this.parentData)
    }
  }
}
</script>

<style>
#parent {
  border: 1px solid red;
  margin: 20px;
}
</style>