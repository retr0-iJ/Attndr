import { createStore,  } from 'vuex'

export default createStore({
  state: {
    isAuthenticated: false,
    token: '',
    name: ''
  },
  mutations: {
    initializeAuth(state){
      if(localStorage.getItem('token')){
        state.token = localStorage.getItem('token')
        state.name = localStorage.getItem("name")
        state.isAuthenticated = true
      }else{
        state.token = ''
        state.isAuthenticated = false
      }
    },
    setToken(state, token){
      state.token = token
      state.isAuthenticated = true
    },
    removeToken(state){
      state.token = ''
      state.name = ''
      state.isAuthenticated = false
    },
    setName(state, name){
      state.name = name
    }
  },
  actions: {
  },
  modules: {
  }
})
