<template>
  <div class="home ">
    <v-container class="py-15">
      <v-flex md8 >
        <v-row>
            <v-col v-for=" value in info" :key="value"
             cols="12"
             :md="3"
             >
              <v-card
              :height="value.prominent ? 350 : 200"
              color="white"
              dark
              >
                <v-img
                  :src="'http://127.0.0.1:8000' + value.picture"
                  class="img-circle" alt="Services"
                  @click="allproduct({name: 'Product'})"
                  height="100%"
                  gradient="rgba(0, 0, 0, .42), rgba(0, 0, 0, .42)"
                >
                <v-row class="ml-3">
                  <v-col><h2 class="sub-heading">{{value.productname}}</h2></v-col>
                </v-row>
                </v-img>
                <v-btn class="my-5 ml-4" v-on:click="addtocart(value.id)">Add to cart</v-btn>
              </v-card>
             </v-col>
        </v-row>
      </v-flex>
    </v-container>
  </div>
</template>
<script>
import axios from 'axios'
export default {
  data () {
    return {
      info: '',
      l: ''
    }
  },
  mounted () {
    axios
      .get('http://localhost:8000/product/' + this.$route.params.id)
      .then(response => (this.info = response.data))
  },
  methods: {
    addtocart: function (id) {
      axios
        .get('http://localhost:8000/addtocart/' + id)
        .then(response => (this.info = response.data))
    }
  },
  created () {
    // axios
    //   .post('http://localhost:8000')
  }
}
</script>
