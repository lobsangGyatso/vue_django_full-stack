<template>
    <v-app-bar
    app
    >
    <v-app-bar-nav-icon
    class="hidden-md-and-up"
    @click="toggleDrawer"
    >
    </v-app-bar-nav-icon >
    <v-container>
        <v-row align="center">
            <v-img :src="require('@/assets/logo.png')"
            class="mr-5"
            width="48"
            height="48"
            max-width="48"
            ></v-img>
            <v-btn href="/"  class="hidden-sm-and-down ml-3" text>
                lobangs
            </v-btn>
            <v-spacer />

         <v-btn text class="hidden-sm-and-down ml-3">
           Dunzo for Partners
         </v-btn>
          <v-btn text class="hidden-sm-and-down ml-3">
           Dunzo for Business
         </v-btn>
         <a href="/addtocard/"
         >
           <v-icon
          large
         >
          mdi-cart {{count}}
         </v-icon>
         </a>
         {{count  }}
        <v-btn class="green ml-8">Sign in</v-btn>
        </v-row>
    </v-container>
    </v-app-bar>
</template>

<script>
import axios from 'axios'
export default {
  name: 'CoreAppBar',
  data () {
    return {
      count: 'asdas'
    }
  },
  mounted: {
    axios
    // .get('http')
  }
}
</script>
