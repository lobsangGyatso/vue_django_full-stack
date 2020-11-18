<template>
    <div class="mt-5">
       <v-container>
             <v-layout row>
                <v-flex md8>
                 <v-col>
                   <v-card class="py-3 px-3">
                       <v-card-title>Sign it to place your order</v-card-title>
                       <v-card-text>
                           New to Dunzo? Sign up now to get started! Or log in to your existing account.
                       </v-card-text>
                       <v-btn class="green text-center ml-3 rounded">Sign In</v-btn>
                    </v-card>
                </v-col>
                <v-col>
                   <v-card class="py-3 px-3">
                       <v-card-title>Add delivery address</v-card-title>
                       <v-card-text>
                          Choose your delivery address from address book or add new
                       </v-card-text>
                    </v-card>
                </v-col>
               <v-col>
                  <v-card class="py-3 px-3">
                       <v-card-title>Select payment method</v-card-title>
                       <v-card-text>
                           Select your payment method from the existing one or add new one
                       </v-card-text>
                    </v-card>
                </v-col>
                </v-flex>
                <v-flex md4>
                <v-col>
                   <v-card class="py-3 px-3">
                       <v-card-title>Your Cart  </v-card-title>
                       <v-card-text>
                           From
                       </v-card-text>
                    </v-card>
                </v-col>
                <v-col>
                   <v-card class="py-0">
                           <v-icon class="ml-5 my-5 float-left"> mdi-cart
                           </v-icon>
                           <v-text-field
                           placeholder="Any instruction for the delivery partner?"
                           ></v-text-field>
                    </v-card>
                </v-col>
                </v-flex>
            </v-layout>
            </v-container>
    </div>
</template>
<script>
export default {
  data () {
    return {
    }
  }
}
</script>
