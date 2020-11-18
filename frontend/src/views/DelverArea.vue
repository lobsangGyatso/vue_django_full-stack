<template>
<div class="all">
    <v-container>
        <h4 class="black-text sub-heading">Areas we deliver to</h4>
        <v-row class="my-4">
            <v-col
            v-for="place in area"
            :key="place"
            cols="12"
            md="3"
            sm="6"
            >
            <a href="#" class="mx-3 text-black" style="color:black;">{{place.name}}</a>
            </v-col>
        </v-row>
    </v-container>
</div>
</template>

<script>
export default {
  data () {
    return {
      area: [
        { name: 'Swyambhu Nath' },
        { name: 'Namgyal Chowk' },
        { name: 'Nayabazar' },
        { name: 'Pokhara' },
        { name: 'Basantapur' },
        { name: 'New Road' },
        { name: 'Boudha' },
        { name: 'Dillibazar' },
        { name: 'Patan' },
        { anem: 'Bakhtapur' }
      ]
    }
  }
}
</script>

<style scoped>
.all{
    background-color: rgb(244, 244, 248);
}
</style>
