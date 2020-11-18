<template>
<div>
  <div class="home">
    <v-container>
      <v-flex>
        <h2 class="mt-3">Kathmandu</h2>
        <h4 class="mt-3">Why step out when you can get everything delivered home with the tap of a button? Bangalore’s
        favourite delivery app gets you Food, Grocery, Medicine, Pet Supplies, Fruits & Vegetables, Meat & Fish, Health & Wellness,
        Gifts and Send Packages from one end of the city to the other. From your local kirana stores to your favourite brands,
          grocery shopping to your forgotten charger, we are always on the move for you. Why worry about your chores, when you can get it all Dun!</h4>
      </v-flex>
        <v-row class="my-5">
            <v-col v-for=" value in info" :key="value"
             cols="12"
             :md="3"
             >
              <v-card
              :height="value.prominent ? 350 : 200"
              color="white"
              dark
              v-bind:href="'/product/'+ value.id"
              >
                <v-img
                  :src="'http://127.0.0.1:8000' + value.picture"
                  class="img-circle" alt="Services"
                  @click="allproduct({name: 'Product'})"
                  height="100%"
                  gradient="rgba(0, 0, 0, .42), rgba(0, 0, 0, .42)"
                >
                <v-row class="ml-3">
                  <v-col><h2 class="sub-heading">{{value.title}}</h2></v-col>
                </v-row>
                </v-img>
                <!-- <router-link :to="{ path: '/product/' + value.id, params: {id: value.id } }"></router-link> -->
              </v-card>
             </v-col>
      </v-row>
      </v-container>
      </div>
        <toppick />
        <Area />
  </div>

</template>

<script>
import axios from 'axios'
import toppick from './toppick'
import Area from './DelverArea'
export default {
  name: 'Home',
  components: {
    toppick,
    Area
  },
  data () {
    return {
      info: '',
      path: 'http://localhost:8000/'
    }
  },
  mounted () {
    axios
      .get('http://localhost:8000')
      .then(response => (this.info = response.data))
  }
}
</script>

<style scoped>
.home{
  background-color: rgba(240, 245, 241, 0.445);
}
</style>
