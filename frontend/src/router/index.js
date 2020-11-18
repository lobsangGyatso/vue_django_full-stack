import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Product from '../views/allproduct.vue'
import AddCart from '../views/addtocart'
import Register from '../components/Register'
import Login from '../components/Login'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/product/:id',
    name: 'Product',
    component: Product
  },
  {
    path: '/addtocard/',
    name: 'AddCart',
    component: AddCart
  },
  {
    path: '/register/',
    name: 'register',
    component: Register
  },
  {
    path: '/login/',
    name: 'login',
    component: Login
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
