<template>
    <div class="navbar-area">
        <nav class="navbar navbar-expand-lg">
            <div class="container nav-container">
                <div class="responsive-mobile-menu">
                    <button class="menu toggle-btn d-block d-lg-none" v-b-toggle.themefie_main_menu aria-expanded="false" aria-label="Toggle navigation">
                        <span class="icon-left"></span>
                        <span class="icon-right"></span>
                    </button>
                </div>
                <div class="logo">
                    <router-link class="main-logo" to="/"><img src="@/assets/img/logo.png" alt="img" style="width: 50px;"></router-link>
                </div>
                <div class="nav-right-part nav-right-part-mobile">
                    <a class="btn btn-base log-in" href="https://edu.skillslab.center/club/">Вход</a>
                </div>
                <b-collapse class="navbar-collapse" id="themefie_main_menu">
                    <ul class="navbar-nav menu-open text-left pl-lg-5">
                        <li class="">
                            <router-link to="/">Главная</router-link>
                        </li>
                        <li class="">
                            <router-link to="/teachers">Лекторы</router-link>
                        </li>
                        <li class="menu-item-has-children current-menu-item" @click="showLinks">
                            <a href="#">Другие проекты</a>
                            <ul class="sub-menu" id="links">
                                <li><a href="https://www.notion.so/mywork7790/Soft-Skills-Lab-Practice-9c0237548d7646e6802f59286998f0d5">Переговорные клубы при ВУЗах</a></li>
                                <li><a href="https://t.me/klimenkoyuri">Переговорный клуб для руководителей</a></li>
                                <li><a href="https://blog.skillslab.center/">Блог</a></li>
                                <li><a href="https://simulator.skillslab.center">Симулятор</a></li>
                            </ul>
                        </li>
                    </ul>
                </b-collapse>
                <div class="nav-right-part nav-right-part-desktop">
                    <a class="btn btn-white log-in" href="https://edu.skillslab.center/club/">Вход</a>
                </div>
            </div>
        </nav>
    </div>
</template>

<script>
export default {
    methods: {
        showLinks() {
            let element = document.getElementById('links').style
            element.visible = element.visible == '' ? 'visible' : ''
            element.opacity = element.opacity == '' ? '1' : ''
            element.display = element.display == '' ? 'block' : ''
        }
    },
}
</script>