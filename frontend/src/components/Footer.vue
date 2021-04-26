<template>
    <div>
        <footer class="footer-area pd-top-135">
            <div class="container"> 
                <div class="footer-bottom">
                    <div class="row">
                        <div class="col-md-6">
                            <div class="thumb">
                                <img src="@/assets/img/logo.png" alt="img" style="max-height: 50px;max-width: 50px;">
                            </div>
                        </div>
                        <div class="col-md-6 text-md-right mt-3 mt-md-0 align-self-center">
                            <p>©2020 <span>Soft Skills Lab</span> Разместить ссылки на оферту и политику обработки персональных данных</p>
                        </div>
                    </div>
                </div>
            </div>
        </footer>
        
        <go-top bg-color="var(--main-color)" 
                size="44px"
                radius="4px"
                right="30px"
                bottom="30px">
        </go-top>
    </div>
</template>

<script>
import GoTop from '@inotom/vue-go-top';

export default {
  components: {
    GoTop
  }
}
</script>