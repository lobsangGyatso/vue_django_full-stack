<template>
<div class="container">
    <div class="mt-8"><h2>Top picks for you</h2></div>
    <v-row
     class="mx-0 my-15"
    >
        <v-col
        cols="12"
        md="3"
        >
        <v-card>
            <v-img
            :src="require('@/assets/toppick/one.jpg')"
            >
            </v-img>
        </v-card>
        </v-col>
        <v-col
        cols="12"
        md="3"
        >
        <v-card>
            <v-img
            :src="require('@/assets/toppick/two.jpg')"
            >
            </v-img>
        </v-card>
        </v-col>
        <v-col
        cols="12"
        md="3"
        >
        <v-card>
            <v-img
            :src="require('@/assets/toppick/three.jpg')"
            >
            </v-img>
        </v-card>
        </v-col>
        <v-col
        cols="12"
        md="3"
        >
        <v-card>
            <v-img
            :src="require('@/assets/toppick/four.jpg')"
            >
            </v-img>
        </v-card>
        </v-col>
    </v-row>
    </div>
</template>

<style scoped>
.toppick{
    background-color:aliceblue;
}
</style>
