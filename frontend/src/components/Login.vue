<template>
  <v-app>
    <v-content>
      <v-container class="fill-height">
        <v-row align="center" justify="center">
          <v-col cols="12" sm="8" md="8">
            <v-card class="elevation-12">
            <v-window v-model="step">
              <v-window-item :value="i">
                <v-row>
                  <v-col cols="12" md="8">
                    <v-card-text class="mt-12">
                      <h1 class="text-center">sign in to haha</h1>
                        <div class="text-center my-2 " mt-4>
                          <v-btn class="mx-2" fab color="black" outlined>
                            <v-icon>fas fa-code</v-icon>
                          </v-btn>
                          <v-btn class="mx-2" fab color="black" outlined>
                            <v-icon>fab fa-google-plus-g</v-icon>
                          </v-btn>
                          <v-btn class="mx-2" fab color="black" outlined>
                            <v-icon>fab fa-linkedin-in</v-icon>
                          </v-btn>
                        </div>
                        <h1 class="text-center mlt-4">ensure your email for Registraion</h1>
                        <v-form>
                          <v-text-field
                          label="Email"
                          name="email"
                          prepend-icon="email"
                          type="text"
                          color="teal accent-3"
                          >
                          </v-text-field>
                          <v-text-field
                          label="Password"
                          id="password"
                          name="password"
                          prepend-icon="lock"
                          type="password"
                          color="teal accent-3"
                          >
                          </v-text-field>
                        </v-form>
                        <h3 class="text-center mt-3">Forget ur password?</h3>
                    </v-card-text>
                    <div class="text-center mt-3">
                      <v-btn>SIGN IN</v-btn>
                    </div>
                  </v-col>
                  <v-col cols="12" md="4" class="teal accent-3">
                    <v-cart-text class="white-text mt-12 ">
                        <h1 class="text-center display-1">Hello, Friends !</h1>
                        <h5 class="text-center">Enter your personal detail and start journy with us</h5>
                    </v-cart-text>
                    <div class="text-center">
                      <v-btn rounded outlined="" >Sign in</v-btn>
                    </div>
                  </v-col>
                </v-row>
              </v-window-item>
            </v-window>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
import { mapActions } from 'vuex'
export default {
  data () {
    return {
      l: '',
      username: 'lobsang',
      password: 'gyatso'
    }
  },
  computed: {
    alluser () {
      return this.$store.state.alltheuser
    },
    credential () {
      return this.$store.state.userdata
    }
  },
  methods: {
    getuser () {
      this.$store.dispatch('getlist')
        .then(response => {
          console.log('we are the right posoition')
        })
        .catch(err => {
          console.log('we are wrong', err)
        })
    },
    // login () {
    //   this.$store.dispatch('userlogin', {
    //     username: this.username,
    //     password: this.password
    //   })
    //     .then(response => {
    //       console.log('we are the inthe right login ', response)
    //     })
    //     .catch(err => {
    //       console.log('we are the worong login', err)
    //     })
    // },
    ...mapActions({
      haha: 'userlogin',
      getlist: 'getlist'
    }),
    login () {
      this.getlist({
        username: this.username,
        password: this.password
      })
    }

  },
  created () {
    this.$store.dispatch('getlist')
  }
}
</script>
