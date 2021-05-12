<template>
  <div id="app">
    <button @click="fetchCatImg">고양이 사진 보여주세요!</button>
    <AnimalList />
  </div>
</template>

<script>
import { mapMutations } from 'vuex'
import AnimalList from '@/components/AnimalList'
import axios from 'axios'

export default {
  name: 'App',
  components: {
    AnimalList,
  },
  methods: {
    ...mapMutations(['UPDATE_ANIMAL_IMAGES']),  // store에서 불러오고 싶은 걸 작성
    fetchCatImg() {
      const CAT_API_URL = 'https://api.thecatapi.com/v1/images/search'
      axios.get(CAT_API_URL)
      .then((response) => {
        const catImgUrl = response.data[0].url
        // this.$store.commit('UPDATE_ANIMAL_IMAGES', catImgUrl)
        this.UPDATE_ANIMAL_IMAGES(catImgUrl)  // <- helper 사용하는 경우. this로 메서드에 접근함
      })
      .catch((error) => {
        console.log(error)
      })
    },
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
