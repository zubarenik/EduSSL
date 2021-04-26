<template>
    <div>

        <!-- Google Tag Manager (noscript) -->
        <noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-TTHMK76"
        height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
        <!-- End Google Tag Manager (noscript) -->

        <div class="course-view-details-inner pd-top-120">
            <div class="container">
                <div class="row">
                    <div class="col-md-8 align-self-center">
                        <div class="details">
                            <span class="sub-title">
                                <div v-for="item in courseInfo(id).category" v-bind:key="item">{{item}}</div>
                            </span>
                            <h1 class="course-heading">{{courseInfo(id).title}}</h1>
                            <p style="font-size: 1.5rem;" class="mb-2">{{courseInfo(id).description}}</p>
                            <ul class="info-area text-left mt-3">
                                <li class="mr-4"><span><i class="fa fa-rub"></i> {{courseInfo(id).cost}}</span></li>
                                <li class="mr-4"><span><i class="fa fa-clock-o"></i> {{courseInfo(id).lessons.length}} занятия</span></li>
                                <li><span><i class="fa fa-calendar"></i> {{courseInfo(id).date_started}}</span></li>                
                            </ul>
                            <ul class="price-area">
                                <li><a class="btn btn-base" v-scroll-to="'#pay'" href="#">Записаться</a></li>
                            </ul>
                        </div>
                    </div>
                    <div class="col-md-4 d-none d-md-flex ">
                        <div class="thumb" style="margin-top: 43px;">
                            <img :src="courseInfo(id).image" alt="img">
                        </div>
                    </div>
                </div>
            </div>
        </div>
        
        <div class="latest-course-area pd-top-110">
            <div class="container">
                <div class="section-title ">
                    <h2>Для кого</h2>
                </div>
                <div class="row">
                    <div v-for="item in courseInfo(id).jobs" v-bind:key="item[0]" class="col-lg-4 col-md-4">
                        <div class="single-course-inner">
                            <div class="thumb">
                                <img :src="item[2]" alt="img">
                            </div>
                            <div class="details">
                                <h5 class="mb-1"><a href="#">{{item[0]}}</a></h5>
                                <p class="mb-3">{{item[1]}}</p>             
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div class="category-area pd-top-110">
            <div class="container">
                <div class="row justify-content-center">
                    <div class="col-12">
                        <div class="section-title">
                            <h2>Чему вы научитесь</h2>
                        </div>
                    </div>
                </div>
                <div class="row">
                    <div v-for="item in courseInfo(id).goals" v-bind:key="item[0]" class="col-lg-3 col-sm-6">
                        <div class="single-category-inner text-center">
                            <h4>{{item[0]}}</h4>
                            <h6>{{item[1]}}</h6>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div class="category-area pd-top-110">
            <div class="container">
                <div class="row justify-content-center">
                    <div class="col-12">
                        <div class="section-title">
                            <h2>Программа</h2>
                        </div>
                    </div>
                </div>
                <div class="row">
                    <div class="col-lg-12">
                        <div class="course-view-sitebar mt-5 mt-lg-0">
                            <div v-for="lesson in courseInfo(id).lessons" v-bind:key="lesson.id" class="widget widget-accordion-inner p-0">
                                <h5 class="widget-title">{{lesson.title}}</h5>
                                <div v-for="theme in lesson.themes" v-bind:key="theme.id" class="faq-accordion accordion">
                                    <div class="card">
                                        <div class="card-header">
                                            <button class="btn" v-b-toggle="`lesson${lesson.id}_theme${theme.id}`">{{theme.title}}<i class="fa fa-plus"></i><i class="fa fa-minus"></i></button>
                                        </div>
                                        <b-collapse class="mt-2" :id="`lesson${lesson.id}_theme${theme.id}`">
                                            <div v-html="theme.text" class="card-body"></div>
                                        </b-collapse>
                                    </div>
                                </div>  
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div class="category-area pd-top-110">
            <div class="container">
                <div class="row justify-content-center">
                    <div class="col-12">
                        <div class="section-title">
                            <h2>Отзывы</h2>
                        </div>
                    </div>
                </div>
                <div class="row">
                    <div v-for="item in courseInfo(id).reviews" v-bind:key="item[0]"  class="col-lg-4 col-sm-6">
                        <div class="widget widget-author-inner">
                            <div class="media">
                                <div class="media-left">
                                    <img :src="item[3]" alt="img">
                                </div>
                                <div class="media-body align-self-center">
                                    <h5>{{item[0]}}</h5>
                                    <p>{{item[1]}}</p>
                                </div>
                            </div>
                            <p>{{item[2]}}</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div class="category-area pd-top-110">
            <div class="container">
                <div class="row justify-content-center">
                    <div class="col-12">
                        <div class="section-title">
                            <h2>Преподаватели</h2>
                        </div>
                    </div>
                </div>
                <div class="row">
                    <div v-for="item in courseInfo(id).teachers" v-bind:key="item[0]" class="col-lg-4">
                        <div class="single-instructor-inner">
                            <div class="thumb">
                                <img :src="item[3]" alt="img">
                            </div>
                            <div class="details">
                                <h5><router-link :to="'/teacher/' + item[0]">{{item[1]}}</router-link></h5>
                                <p>{{item[2]}}</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div class="category-area pd-top-110 back-primary" style="padding-bottom: 110px;" id="pay">
            <div class="container">
                <div class="row">
                    <div class="col-lg-6">
                        <form class="contact-form">
                            <h3>Записаться на мастер-класс {{courseInfo(id).title}}</h3>
                            <p>Оплатите онлайн или дождитесь звонка менеджера</p>
                            <div class="row">
                                <div class="col-12">
                                    <div class="single-input-wrap">
                                        <label>Имя</label>
                                        <input v-model="name" type="text" class="form-control" placeholder="Ваше имя">
                                    </div>
                                </div>
                                <div class="col-12">
                                    <div class="single-input-wrap">
                                        <label>Email</label>
                                        <input v-model="email" type="text" class="form-control" placeholder="Ваш Email">
                                    </div>
                                </div>
                                <div class="col-12">
                                    <div class="single-input-wrap">
                                        <label>Телефон</label>
                                        <input v-model="number" type="text" class="form-control" placeholder="Ваш номер телефона">
                                    </div>
                                </div>
                                <div class="col-12">
                                    <div class="single-input-wrap">
                                        <label>Промокод</label>
                                        <input v-model="slug" type="text" class="form-control">
                                    </div>
                                </div>
                            </div>
                            <button @click.prevent="saveSubscriber()" type="submit" class="btn btn-base">Записаться</button>
                        </form>
                    </div>   
                    <div class="col-lg-6">
                        <div class="contact-page-inner ml-xl-5 mt-5 mt-lg-0">
                            <div class="contact-map">
                                <h3>Ваши новые навыки:</h3>
                                <div class="row">
                                    <div v-for="item in courseInfo(id).skills" v-bind:key="item[0]" class="col-lg-6 col-sm-6">
                                        <div class="single-category-inner text-center">
                                            <h4>{{item[0]}}</h4>
                                            <h6>{{item[1]}}</h6>
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
  name: 'Course',
  components: {
  },
  data() {
      return {
          id: this.$route.params.id,
          name: "",
          email: "",
          number: "",
          slug: "",
      }
  },
  computed: {
    ...mapGetters([
        'courseInfo',
    ])
  },
  methods: {
    async checkPromoCode() {
        let result
        await this.$axios.get(`/check_promocode/${this.id}/`, { 
            params: {
                slug: this.slug 
            }
        })
        .then(response => {
            result = response.data ? response.data.slug : null 
        })
        return result
    },
    async saveSubscriber() {
        if (this.name == "" || this.email == "" || this.number == "") {
            alert("Заполните, пожалуйста, все поля формы!")
            return
        }
        
        const person = new FormData()
        person.append('name', this.name)
        person.append('email', this.email)
        person.append('number', this.number)
        person.append('promocode', await this.checkPromoCode())

        this.$axios.post(`/course/${this.id}/`, person)
        .then(response => {
            this.name = ""
            this.email = ""
            this.number = ""
            this.slug = ""

            if (!response.data){ 
                this.$router.push('/success')
                return
            }
           
            const win = window.open("about:blank", "", "height=600, width=400")
            win.document.write("Перенаправляем в платежный сервис...")
            win.location.replace(response.data.link)
            win.focus()
            
            this.checkPayment(win, response.data.person)
        })
        .catch((error) => {
            console.log(error)
        })
    },
    checkPayment(win, person) {
        var timer = setInterval(() => {
            this.$axios.get(`/check_payment/${person}/`)
            .then((response) => {
                if (win.closed){
                    alert("Платеж отменен") 
                    clearInterval(timer)  
                }

                if (response.data.status == 1)
                    alert("Что-то во время платежа прошло плохо")
                
                if (response.data.status == 2) {
                    win.close()
                    this.$router.push('/success')
                    clearInterval(timer)
                }
            })
            .catch((error) => {
                console.log(error)
            })
        },
        5000
      )
    }
  },
  mounted() {
    this.$store.dispatch('fetchCourseInfo', this.id) 
  },
}
</script>
