<template>
  <div class="listing">
    <div class="wrapperMainInfo">
      <div class="wrapper">
        <div class="wrapperDate">
          <div class="date">{{new Date(project.application_date).toLocaleDateString('ru-ru')}}</div>
        </div>

        <h2>{{ project.title }}</h2>

        <p>{{ project.description }}</p>
      </div>
      <img :src="require(`@/assets/${project.thumbnail}`)">
    </div>
    <div class="wrapperInfo">
      <div class="wrapperTitle">
        <div class="date">{{new Date(project.application_date).toLocaleDateString('ru-ru')}}</div>
        <h2>Заявление</h2>
      </div>

      <div class="wrapperShortInfo">
        <div class="item">
          <h3>Стадия готовности продукта</h3>
          <p>{{ project.product_stage }}</p>
        </div>
        <div class="item">
          <h3>Cертификация продукта</h3>
          <p>{{ project.requires_cert }}</p>
        </div>
        <div class="item">
          <h3>Размер команды</h3>
          <p>{{ project.team_size }}</p>
        </div>
        <div class="item">
          <h3>Организация Московского транспорта</h3>
          <p>
            {{ project.prior_organization }}
          </p>
        </div>
      </div>

      <div class="wrapperDescription">
        <div class="item">
          <h3>Организация Московского транспорта</h3>
          <p>
            {{project.use_cases}}
          </p>
        </div>
        <div class="item">
          <h3>Организация Московского транспорта</h3>
          <p>
            Lorem ipsum, dolor sit amet consectetur adipisicing elit. Odit eius atque incidunt magni, perferendis dicta ipsam cum, numquam asperiores quidem praesentium voluptas, nulla explicabo in!
          </p>
        </div>
        <img :src="require('@/assets/FAQ.svg')" alt="Pattern">
      </div>

      <div class="wrapperPresentation">
        <a :href="project.presentation_link" class="link idea">Сcылка на презентацию</a>
      </div>

      <!-- <div class="wrapperAcceleration">
        <div class="wrapperTitle">
          <div class="date">01.01.2021–01.04.2021</div>
          <div>Акселерация</div>
        </div>

        <div class="wrapperPoints">
          <div class="point">
            <div class="circle"></div>
            <div class="wrapperTitle">
              <div class="date">1 Января 2021</div>
              <div>Начало</div>
          </div>
          </div>
          <div class="line"></div>
          <div class="point">
            <div class="circle"></div>
            <div class="wrapperTitle">
              <div class="date">1 Марта 2021</div>
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
                <div class="date">1 Января 2021</div>
                <div>Тестирование ИБП на светофорном объекте ЦОДД</div>
            </div>
          </div>
          <div class="line"></div>
          <div class="point">
            <div class="circle"></div>
            <div class="wrapperTitle">
              <div class="date">1 Марта 2021</div>
              <div>Тестирование и улучшение ИБП в лаборатории ЦОДД для получения заключения о соответствии требованиям безопасности</div>
          </div>
          </div>
          <div class="line"></div>
          <div class="point">
            <div class="circle"></div>
            <div class="wrapperTitle">
              <div class="date">1 Марта 2021</div>
              <div>Старт разработки второй версии ИБП с учётом замечаний, полученных от тестирования в лаборатории</div>
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
      </div> -->

    </div>
  </div>
</template>

<script>
import { ref } from '@vue/reactivity'
import { useStore } from 'vuex'
export default {
  setup () {
    const store = useStore()

    const project = ref(store.state.project)

    return {
      project
    }
  }
}
</script>

<style lang="scss" scoped>
.listing {
  .date {
    font-size: 20px;
    line-height: 23px;
    color: #333333;
    opacity: 0.4;
  }
  h2 {
    max-width: 637px;
    font-size: 38px;
    line-height: 37px;
    color: #000000;
    margin-top: 1rem;
    padding-bottom: 1.5rem;
  }
  .wrapperMainInfo {
    display: flex;
    flex-flow: wrap row;
    justify-content: space-between;
    align-items: center;
    gap: 124px;
    margin-top: 4rem;
  }

  .wrapper {
    & > p {
      font-size: 20px;
      line-height: 28px;
      max-width: 537px;
    }
  }

  .wrapperInfo > .wrapperTitle {
    border-bottom: 1px solid #EBEBEB;
  }

  .wrapperShortInfo {
    display: flex;
    flex-wrap: wrap;
    gap: 4rem;
    padding: 2rem 0;
    border-bottom: 1px solid #EBEBEB;

    & > .item {
      flex: 0 0 auto;
      width: calc(50% - 2rem);
    }
  }

  .wrapperDescription {
    display: flex;
    flex-wrap: wrap;
    gap: 4rem;
    padding: 2rem 0;
    border-bottom: 1px solid #EBEBEB;
    position: relative;

    & > .item {
      flex: 0 0 auto;
      width: 50%;
    }

    & > img {
      position: absolute;
      bottom: 0;
      left: 75%;
    }
  }

  .wrapperPresentation {
    padding: 2rem 0;
    border-bottom: 1px solid #EBEBEB;

    a {
      display: initial;
      padding-left: 34px;
      position: relative;

      &::before {
        content: '';
        height: 26px;
        width: 26px;
        background: url('../assets/link.svg');
        position: absolute;
        left: 0;
      }
    }
  }
}
</style>
