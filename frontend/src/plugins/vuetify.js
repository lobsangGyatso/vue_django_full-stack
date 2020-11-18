import 'font-awesome/css/font-awesome.min.css'
import 'material-design-icons-iconfont/dist/material-design-icons.css' // Ensure you are using css-loader
import Vue from 'vue'
import Vuetify from 'vuetify/lib'

Vue.use(Vuetify)
const theme = {
  primary: '#4CAF50',
  secondary: '#9C27b0',
  accent: '#9C27b0',
  info: '#00CAE3'
}
export default new Vuetify({
  icons: {
    iconfont: 'md'
  },
  theme: {
    themes: {
      dark: theme,
      light: theme
    }
  }
})
