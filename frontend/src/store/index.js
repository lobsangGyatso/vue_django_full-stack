import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
// import { reject, resolve } from 'core-js/fn/promise'

Vue.use(Vuex)
// Vue.use(axios)
export default new Vuex.Store({
  state: {
    categories: [],
    alltheuser: '',
    userdata: '',
    drawer: null,
    haha: '',
    cartitem: ''
  },
  getters: {
    getlist (state) {
      return state.alltheuser
    }
  },
  mutations: {
    getlist (state, payload) {
      console.log('sdfsdf', payload)
      state.alltheuser = payload
    },
    userlogin (state, payload) {
      console.log(payload)
      state.userdata = payload
    },
    lol (state, payload) {
      console.log('we mustatin methods prototype')
      state.drawer = payload
    },
    weare (state, payload) {
      console.log(payload)
      state.haha = payload
    }
  },
  actions: {
    getlist (context, payload) {
      axios.post('https://jsonplaceholder.typicode.com/todos/')
        .then(function (response) {
          console.log('this is payload', payload)
          console.log(response)
          context.commit('getlist', response.data)
        })
    },
    userlogin (context, credential) {
      context.commit('userlogin', credential)
    }
    // weare ({ commit }, data) {
    //   return new Promise ((resolve, reject) => {
    //     axios.post('https://jsonplaceholder.typicode.com/todos/')
    //     .then(response => {
    //       console.log('we are the best at the time', response.data)
    //       commit('weare', data)
    //       resolve(response)
    //     })
    //     .catch(err => {
    //       console.log('we are the gone wrong in this time',err)
    //       reject('we got wrong at this time', err)
    //     })
    //   })
    // },
    // async best () {
    //   await axios.get('https://jsonplaceholder.typicode.com/todos/', {
    //     methods: 'get'
    //     headers: {
    //       Authoriazation: 'Basic ' + btoa('username:password'),
    //       content-Type: 'application/x-www-form-urlencoded'
    //     }
    //   })
    //     .then(function(response){
    //       console.log("we wait till teh every things is right", response)
    //     })
    //     .catch(function(err){
    //       console.log("we wait till the answer is worng", err)
    //     })
    // }
  },
  modules: {
  }
})
