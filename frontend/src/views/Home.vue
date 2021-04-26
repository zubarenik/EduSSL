<template>
  <div class="home">

    <!-- Google Tag Manager (noscript) -->
    <noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-TTHMK76"
    height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
    <!-- End Google Tag Manager (noscript) -->

    <div class="banner-area style-three">
        <div class="container">
            <div class="banner-area-inner">
                <div class="row">
                    <div class="col-md-10 align-self-center mt-md-5">
                        <div class="banner-inner">
                            <h1 class="banner-heading">Онлайн-университет по развитию Soft Skills.</h1>
                        </div>
                    </div>
                    <div class="col-md-10 mt-md-5 mt-2">
                        <p style="font-size: 1.5rem; font-weight: bold; color: #08a2dc;" class="mb-2">Направления обучения:</p>
                        <a :href="`#category${item.id}`" v-for="item in categories" v-bind:key="item.id" class="tag float-left mr-1 mr-md-3 mb-3">
                            {{item.title}}
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </div>
    
    <div class="latest-course-area pd-top-110">
        <div class="container">
            <div class="section-title">
                <h2>Ближайшие мероприятия</h2>
            </div>
            <div class="row">
                <div v-for="item in lastCourses" v-bind:key="item.id" class="col-lg-4 col-md-6">
                    <div class="single-course-inner">
                        <div class="thumb">
                            <img :src="item.image" alt="img">      
                        </div>
                        <div class="details">
                            <div class="meta">
                                <div class="row">
                                    <div class="col-6">
                                        <p>Мест: {{item.capacity}}</p>
                                    </div>
                                    <div class="col-6 text-right">
                                        <p>{{item.date_started}}</p>
                                    </div>
                                </div>
                            </div>
                            <h5 class="mb-1"><router-link :to="'/course/' + item.id">{{item.title}}</router-link></h5>
                            <p class="mb-3">{{item.description}}</p>
                            <div class="price-inner">
                                <div class="row">
                                    <div class="col-6">
                                        <p>₽ {{item.cost}}</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div class="intro-area pd-top-120">
        <div class="container">
            <div class="row justify-content-center">
                <div class="col-xl-7 col-lg-8">
                    <div class="section-title text-center">
                        <h2>Как мы учим?</h2>
                        <p>Мы даем только проверенный опытом и теоретически обоснованный материал, который поможет вам как можно скорее получить результат и применить его в жизни для достижения ваших целей</p>
                    </div>
                </div>
            </div>
            <div class="row justify-content-center">
                <div class="col-lg-4 col-md-6">
                    <div class="single-intro-inner text-center">
                        <div class="thumb">
                            <img src="@/assets/img/icon/1.png" alt="img">
                        </div>
                        <div class="details">
                            <h5>Практические навыки</h5>
                            <p>Мы создали школу так, чтобы уже после первого занятия вы могли использовать навыки на практике</p>
                        </div>
                    </div>
                </div>
                <div class="col-lg-4 col-md-6">
                    <div class="single-intro-inner text-center">
                        <div class="thumb">
                            <img src="@/assets/img/icon/2.png" alt="img">
                        </div>
                        <div class="details">
                            <h5>Экспертный подход</h5>
                            <p>Наши спикеры - специалисты в своей сфере, всегда готовые помочь вам и дать нужные знания и навыки</p>
                        </div>
                    </div>
                </div>
                <div class="col-lg-4 col-md-6">
                    <div class="single-intro-inner text-center">
                        <div class="thumb">
                            <img src="@/assets/img/icon/3.png" alt="img">
                        </div>
                        <div class="details">
                            <h5>Теория и практика</h5>
                            <p>Основательный подход к развитию поможет вам познакомиться с нужными теоретическими основами и научиться их применять в жизни</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div v-for="item in categories" v-bind:key="item.id" :id="`category${item.id}`" class="latest-course-area pd-top-120">
        <div class="container">
            <div class="section-title ">
                <h2>{{item.title}}</h2>
                <p>{{item.description}}</p>
            </div>
            <div class="row">
                <div v-for="course_id in item.courses" v-bind:key="course_id" class="col-lg-4 col-md-6">
                    <div class="single-course-inner">
                        <div class="thumb">
                            <img :src="course(course_id).image" alt="img">
                        </div>
                        <div class="details">
                            <div class="meta">
                                <div class="row">
                                    <div class="col-6">
                                        <p>Мест: {{course(course_id).capacity}}</p>
                                    </div>
                                    <div class="col-6 text-right">
                                        <p>{{course(course_id).date_started}}</p>
                                    </div>
                                </div>
                            </div>
                            <h5 class="mb-1"><router-link :to="'/course/' + course_id">{{course(course_id).title}}</router-link></h5>
                            <p class="mb-3">{{course(course_id).description}}</p>
                            <div class="price-inner">
                                <div class="row">
                                    <div class="col-6">
                                        <p>₽ {{course(course_id).cost}}</p>
                                    </div>  
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div class="latest-course-area pd-top-120">
        <div class="container">
            <div class="section-title ">
                <h2>Архив курсов</h2>
                <p>Эти курсы уже прошли, но вы можете записаться на актуальные</p>
            </div>
            <div class="row">     
                <div v-for="item in storeCourses" v-bind:key="item.id" class="col-lg-4 col-md-6">
                    <div class="single-course-inner">
                        <div class="thumb">
                            <img :src="item.image" alt="img">
                        </div>
                        <div class="details">
                            <div class="meta">
                                <div class="row">
                                    <div class="col-6">
                                        <p>Мест: {{item.capacity}}</p>
                                    </div>
                                    <div class="col-6 text-right">
                                        <p>{{item.date_started}}</p>
                                    </div>
                                </div>
                            </div>
                            <h5 class="mb-1"><router-link :to="'/course/' + item.id">{{item.title}}</router-link></h5>
                            <p class="mb-3">{{item.description}}</p>
                            <div class="price-inner">
                                <div class="row">
                                    <div class="col-6">
                                        <p>₽ {{item.cost}}</p>
                                    </div>    
                                </div>
                            </div>
                        </div>
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
  name: 'Home',
  components: {
  },
  computed: {
    ...mapGetters([
      'courses',
      'categories',
      'course',
    ]),
    lastCourses() {
      if (this.courses.length == 0)
        return
        
      var events = [...this.courses]

      events.sort((a, b) => {
          return new Date(a.date_started) - new Date(b.date_started)
      })

      while (new Date(events[0].date_started) < new Date())
          events.splice(0, 1)
      
      while (events.length > 6)
          events.splice(-1, 1)
      
      return events
    },
    storeCourses() {
      if (this.courses.length == 0)
        return
      
      var archive = [...this.courses]

      archive.sort((a, b) => {
          return new Date(b.date_started) - new Date(a.date_started)
      })

      while (new Date(archive[0].date_started) > new Date())
         archive.splice(0, 1)

      while (archive.length > 18)
          archive.splice(-1, 1)

      return archive
    }
  }
}
</script>
