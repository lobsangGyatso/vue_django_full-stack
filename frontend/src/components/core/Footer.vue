<template>
  <v-footer
    class="py-4"
    dark
    height="auto"
  >
    <v-container class="mx-auto">
      <h4  class="mt-3">You can’t stop time, but you can save it!</h4>
      <p class="my-3">Living in the city, there is never enough time to shop for groceries, pick-up supplies, grab food and wade through traffic on the way back home. How about we take care of all of the above for you? What if we can give you all that time back? Send packages across the city and get everything from food, groceries, medicines and pet supplies delivered right to your doorstep. From any store to your door, just make a list and we’ll make it disappear. Just Dunzo It!</p>
      <v-divider class="mx-3" height="100px"></v-divider>
      <v-row  class="my-4">
        <v-col
         cols="12"
         md="3"
        >
        <h4>DUNZO</h4>
        <a href="" style="color:white;">About</a><br>
        <a href="" style="color:white;">Jobs</a><br>
        <a href="" style="color:white;">Contact</a><br>
        <a href="" style="color:white;">Terms & Conditions</a><br>
        <a href="" style="color:white;">Privacy Policy</a><br>
        <a href="" style="color:white;">Dunzo for Partner</a><br>
        <a href="" style="color:white;">Dunzo for Business</a><br>
        <a href="" style="color:white;">Grow with Google</a><br>
        </v-col>
        <v-col
         cols="12"
         md="3"
        >
        <h4>SERVICABLE CITIES</h4>
        <a href="" style="color:white;">Banglore</a><br>
        <a href="" style="color:white;">Pune</a><br>
        <a href="" style="color:white;">Contact</a><br>
        <a href="" style="color:white;">Guagaon</a><br>
        <a href="" style="color:white;">Hyderbad</a><br>
        <a href="" style="color:white;">New Delhi</a><br>
        <a href="" style="color:white;">Chennai</a><br>
        <a href="" style="color:white;">Mumbai</a><br>
        </v-col>
        <v-col
         cols="12"
         md="3"
        >
        <h4>GET IN TOUCH</h4>
        <a href="" style="color:white;">Email</a><br>
        <a href="" style="color:white;">Twitter</a><br>
        <a href="" style="color:white;">Facebook</a><br>
        <a href="" style="color:white;">Instagram</a><br>
        <a href="" style="color:white;">Linkedin</a>
        </v-col>
         <v-col cols="12"
          md="3">
          <v-img :src="require('@/assets/toppick/carrier.jpg')"></v-img>
        </v-col>
        <v-spacer />

        <v-btn
          class="mr-0"
          square
          title="Go to top"
          @click="$vuetify.goTo(0)"
        >
          <v-icon>mdi-chevron-up</v-icon>
        </v-btn>
      </v-row>
    </v-container>
  </v-footer>
</template>

<script>
export default {
  name: 'CoreFooter',
  data: () => ({
    items: [
      {
        href: '#!',
        icon: 'mdi-twitter'
      },
      {
        href: '#!',
        icon: 'mdi-instagram'
      },
      {
        href: '#!',
        icon: 'mdi-facebook'
      },
      {
        href: '#!',
        icon: 'mdi-google-plus'
      },
      {
        href: '#!',
        icon: 'mdi-reddit'
      },
      {
        href: '#!',
        icon: 'mdi-discord'
      },
      {
        href: '#!',
        icon: 'mdi-pinterest'
      }
    ]
  })
}
</script>
