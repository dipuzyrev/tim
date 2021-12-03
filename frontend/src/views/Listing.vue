<template>
  <div class="listing">
    <div class="wrapperMainInfo">
      <div class="wrapper">
        <div class="wrapperDate">
          <div class="date">{{proj.date}}</div>
          <ul>
            <li class="step">{{proj.step}}</li>
          </ul>
        </div>

        <h2>{{proj.title}}</h2>

        <p>{{proj.description}}</p>
      </div>
      <img v-if="proj.thumbnail" :src="require(`@/assets/${proj.thumbnail}`)" :alt="proj.title">
      <img v-else :src="require(`@/assets/notFound.svg`)">
    </div>
    <div class="wrapperInfo">
      <div class="wrapperTitle">
        <div class="date">{{proj.date}}</div>
        <div>Заявление</div>
      </div>

      <div class="wrapperShortInfo">
        <div class="item">
          <h3>Стадия готовности продукта</h3>
          <p>Продукт</p>
        </div>
        <div class="item">
          <h3>Cертификация продукта</h3>
          <p>Требуется</p>
        </div>
        <div class="item">
          <h3>Размер команды</h3>
          <p>20 человек</p>
        </div>
        <div class="item">
          <h3>Организация Московского транспорта</h3>
          <p>
            ЦОДД
            <img src="../assets/Searh.png" height="40" alt="">
          </p>
        </div>
      </div>

      <div class="wrapperDescription">
        <div class="item">
          <h3>Организация Московского транспорта</h3>
          <p>
            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Laborum molestias, iusto fugit eos suscipit quos asperiores pariatur fuga reprehenderit explicabo rerum magni consequuntur? Eius a molestiae, aperiam totam omnis voluptatum!
          </p>
        </div>
        <div class="item">
          <h3>Организация Московского транспорта</h3>
          <p>
            Lorem ipsum, dolor sit amet consectetur adipisicing elit. Odit eius atque incidunt magni, perferendis dicta ipsam cum, numquam asperiores quidem praesentium voluptas, nulla explicabo in!
          </p>
        </div>
      </div>

      <div class="wrapperPresentation">
        <a href=""></a>
      </div>

      <div class="wrapperAcceleration">
        <div class="wrapperTitle">
          <div class="date">01.01.2021–01.04.2021</div>
          <div>Акселерация</div>
        </div>

        <div class="wrapperPoints">
          <div class="point">
            <div class="circle"></div>
            <div class="wrapperTitle">
              <div class="date">1 Января 2021</div>
              <div>Начало</div>
          </div>
          </div>
          <div class="line"></div>
          <div class="point">
            <div class="circle"></div>
            <div class="wrapperTitle">
              <div class="date">1 Марта 2021</div>
              <div>Demo day</div>
          </div>
          </div>
        </div>

        <video src=""></video>
      </div>

      <div class="wrapperPilot">
        <div class="wrapperTitle">
          <div class="date">01.01.2021–01.04.2021</div>
          <div>Акселерация</div>
        </div>

        <div class="wrapperPoints">
          <div class="point">
              <div class="circle"></div>
              <div class="wrapperTitle">
                <div class="date">1 Января 2021</div>
                <div>Тестирование ИБП на светофорном объекте ЦОДД</div>
            </div>
          </div>
          <div class="line"></div>
          <div class="point">
            <div class="circle"></div>
            <div class="wrapperTitle">
              <div class="date">1 Марта 2021</div>
              <div>Тестирование и улучшение ИБП в лаборатории ЦОДД для получения заключения о соответствии требованиям безопасности</div>
          </div>
          </div>
          <div class="line"></div>
          <div class="point">
            <div class="circle"></div>
            <div class="wrapperTitle">
              <div class="date">1 Марта 2021</div>
              <div>Старт разработки второй версии ИБП с учётом замечаний, полученных от тестирования в лаборатории</div>
          </div>
          </div>
        </div>

        <div class="wrapperLinks">
          <a href=""></a>
          <a href=""></a>
        </div>
      </div>

      <div class="wrapperComments">
        <div class="wrapperTitle">
          <div>Комментарии экспертов</div>
        </div>

        <div class="wrapperComment">
          <img src="" alt="">

          <div>
            <p>Lorem ipsum dolor sit amet.</p>

            <p>Lorem ipsum dolor, sit amet consectetur adipisicing elit. Debitis quidem perferendis eveniet laudantium nam nemo nesciunt cumque rem eligendi maxime.</p>
          </div>
        </div>
      </div>
      
    </div>
  </div>
</template>

<script>
import { ref } from '@vue/reactivity'
export default {
  setup() {
    const project = ref({

    })

    return {
      project
    }
  },
}
</script>

<style lang="scss" scoped>

</style>