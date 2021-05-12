import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {  // state는 data !
    animalImages: [],
  },
  getters: {  // computed 같은 역할
    getAnimalImages(state) {
      return state.animalImages
    },
  },
  mutations: {  // methods 같은 역할
    UPDATE_ANIMAL_IMAGES(state, imgUrl) {
      state.animalImages.push(imgUrl)
    }
  },
  actions: {
  },
  modules: {
  }
})
