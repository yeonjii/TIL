<template>
  <div>
    <h1>My Adorable Cat List</h1>
    <img
      v-for="image in getAnimalImages"
      :key="image"
      width="200"
      :src="image"
      alt="cat-image"
    >
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'AnimalList',
  computed: {
    ...mapGetters(['getAnimalImages']),  // 불러오고 싶은걸 리스트형태로 작성
    // animalImages() {
    //   return this.$store.getters.getAnimalImages
    // },
  }
}
</script>

<style>

</style>