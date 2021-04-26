<template>
    <div class="popular-instructor-area pd-top-120">
        
        <!-- Google Tag Manager (noscript) -->
        <noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-TTHMK76"
        height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
        <!-- End Google Tag Manager (noscript) -->

        <div class="container">
            <div class="section-title">
                <h2>Преподаватели</h2>
            </div>
            <div class="row">
                <div v-for="teacher in teachers" v-bind:key="teacher.id" class="col-md-4">
                    <div class="single-instructor-inner">
                        <div class="thumb">
                            <img :src="teacher.image" alt="img">
                        </div>
                        <div class="details">
                            <h5><router-link :to="'/teacher/' + teacher.id">{{teacher.title}}</router-link></h5>
                            <p>{{teacher.description}}</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'Teachers',
  components: {
  },
  computed: {
    ...mapGetters([
        'teachers',
    ])
  },
  mounted() {
    this.$store.dispatch('fetchTeachers', this.id);  
  },
}
</script>