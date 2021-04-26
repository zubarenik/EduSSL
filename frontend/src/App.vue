<template>
  <div id="app">
    <Navbar></Navbar>
    <router-view/>
    <Footer></Footer>
  </div>
</template>

<style>
  @import './assets/css/custom.css';
  @import './assets/css/responsive.css';
  @import './assets/css/style.css';
  @import './assets/css/plugins.min.css';
</style>

<script>
import Navbar from "@/components/Navbar.vue"
import Footer from "@/components/Footer.vue"

export default {
  name: "App",
  components: {
    Navbar,
    Footer,
  },
  mounted() {
    this.$store.dispatch('fetchCoursesAndCategories');
  },
}
</script>
