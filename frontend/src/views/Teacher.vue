<template>
    <div class="instructor-area pd-top-195">
        
        <!-- Google Tag Manager (noscript) -->
        <noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-TTHMK76"
        height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
        <!-- End Google Tag Manager (noscript) -->

        <div class="container">
            <div class="row">
                <div class="col-lg-4">
                    <div class="instructor-single-thumb text-center">
                        <img :src="teacherInfo(id).image" alt="img">
                    </div>    
                </div>
                <div class="col-lg-8">
                    <div class="instructor-single-details">
                        <h2>{{teacherInfo(id).title}}</h2>
                        <p>{{teacherInfo(id).description}}</p>
                        <h3>Обо мне</h3>
                        <p v-html="teacherInfo(id).text"></p>
                    </div> 

                    <h4 class="mt-5">Мастер-классы</h4>
                    <div class="row">
                        <div v-for="course in teacherInfo(id).courses" v-bind:key="course.id" class="col-lg-6 col-md-6">
                            <div class="single-course-inner style-two">
                                <div class="thumb">
                                    <img :src="course.image" alt="img">     
                                </div>
                                <div class="details">
                                    <div class="meta">
                                        <div class="row">
                                            <div class="col-6">
                                                <p>{{course.capacity}}</p>
                                            </div>
                                            <div class="col-6 text-right">
                                                <p>{{course.date_started}}</p>
                                            </div>
                                        </div>
                                    </div>
                                    <h5><router-link :to="'/course/' + course.id">{{course.title}}</router-link></h5>
                                    <div class="price-inner">
                                        <div class="row">
                                            <div class="col-6">
                                                <p>₽ {{course.cost}}</p>
                                            </div>
                                            <div class="col-6 text-right">
                                                <a href="#"><i class="fa fa-shopping-cart"></i></a>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <nav class="text-center mt-4">
                        <ul class="pagination">
                            <li class="page-item active"><a class="page-link" href="#">1</a></li>
                            <li class="page-item"><a class="page-link" href="#">2</a></li>
                            <li class="page-item"><a class="page-link" href="#">3</a></li>
                            <li class="page-item"><a class="page-link" href="#">4</a></li>
                            <li class="page-item active"><a class="page-link" href="#">Next</a></li>
                        </ul>
                    </nav>   
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'Teacher',
  components: {
  },
  data() {
      return {
          id: this.$route.params.id,
      }
  },
  computed: {
    ...mapGetters([
        'teacherInfo',
    ])
  },
  mounted() {
    this.$store.dispatch('fetchTeacherInfo', this.id);  
  },
}
</script>