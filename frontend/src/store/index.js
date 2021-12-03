import { createStore } from 'vuex'

export default createStore({
  state: {
    project: {}
  },
  mutations: {
    change (state, newProject) {
      state.project = newProject
    }
  },
  actions: {
  },
  modules: {
  }
})
