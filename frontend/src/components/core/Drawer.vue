<template>
    <v-navigation-drawer
    v-model="drawer"
    app
    dark
    temporary
    >
   <v-list>
        <v-list-item v-for="link in links" :key="link.text" router :to="link.routes" active-class="Border">
          <v-list-item-action>
            <v-icon>{{link.icon}}</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>{{link.text}}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
</template>

<script>
export default {
  name: 'CoreDrawer',
  data () {
    return {
    }
  }
}
</script>
