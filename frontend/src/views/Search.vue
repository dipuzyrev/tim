<template>
  <div class="search">
    <div class="surface">
      <div class="search">
        <img :src="require('@/assets/Search.png')" alt="Search">
        <input v-model="textToSearch" type="text">
        <!-- TODO: добавить algolia поиск короче -->
      </div>

      <div class="tags">
        <DropDown title="Технологическое направление">
          <div class="item">
            <input type="checkbox" name="cityTansport" id="cityTansport" style="width: 37px">
            <label for="cityTansport">Доступный и комфортный городской транспорт</label>
          </div>
          <div class="item">
            <input type="checkbox" name="newTypes" id="newTypes">
            <label for="newTypes">Новые виды мобильности</label>
          </div>
          <div class="item">
            <input type="checkbox" name="safetyRoad" id="safetyRoad">
            <label for="safetyRoad">Безопасность дорожного движения</label>
          </div>
          <div class="item">
            <input type="checkbox" name="healthyStreets" id="healthyStreets">
            <label for="healthyStreets">Здоровые улицы и экология</label>
          </div>
          <div class="item">
            <input type="checkbox" name="digitalTech" id="digitalTech" style="width: 28px">
            <label for="digitalTech">Цифровые технологии в&nbsp;транспорте</label>
          </div>

        </DropDown>
        <DropDown title="Технологическое направление">
          <div class="item">
            <input type="checkbox" name="Idea" id="Idea">
            <label for="Idea">Идея</label>
          </div>
          <div class="item">
            <input type="checkbox" name="Accelerator" id="Accelerator">
            <label for="Accelerator">Аккселератор</label>
          </div>
          <div class="item">
            <input type="checkbox" name="Pilot" id="Pilot">
            <label for="Pilot">Пилот</label>
          </div>

        </DropDown>
      </div>

    </div>
    <div class="surface project" v-for="(proj, index) in projects" :key="index">
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
  </div>
</template>

<script>
import { ref } from '@vue/reactivity'
import { useRoute } from 'vue-router'

import DropDown from '@/components/DropDown.vue'
export default {
  components: {
    DropDown
  },

  setup () {
    const route = useRoute()

    const textToSearch = ref(route.query.q)

    const projects = ref([
      {
        title: 'Titan Power Solution: без проводов к дорожным камерам',
        description: 'Суперконденсаторный источник бесперебойного питания (ИБП) — решение для обеспечения безотказной работы автоматизированных систем управления дорожным движением.',
        date: '01.01.2021',
        step: 'Пилот'
      },
      {
        title: 'Titan Power Solution: без проводов к дорожным камерам',
        description: 'Суперконденсаторный источник бесперебойного питания (ИБП) — решение для обеспечения безотказной работы автоматизированных систем управления дорожным движением.',
        date: '01.01.2021',
        step: 'Пилот',
        thumbnail: '1.png'
      },
      {
        title: 'Titan Power Solution: без проводов к дорожным камерам',
        description: 'Суперконденсаторный источник бесперебойного питания (ИБП) — решение для обеспечения безотказной работы автоматизированных систем управления дорожным движением.',
        date: '01.01.2021',
        step: 'Пилот',
        thumbnail: '1.png'
      }
    ])

    return {
      textToSearch,
      projects
    }
  }
}
</script>

<style lang="scss" scoped>
.search {
  .surface {
    padding: 2rem;
    background: #FFFFFF;
    border-radius: 2rem;

    & > .search {
      display: flex;
      gap: 1rem;
      margin-bottom: 2rem;

      img {
        height: 32px;
        width: 32px;
      }

      input {
        background: #FFFFFF;
        border: none;
        font-family: 'Moscow Sans', sans-serif;
        font-size: 1.5rem;
        color: #000;
        width: 100%;

        &:focus {
          outline: none;
          box-shadow: none;
        }
      }
    }

    .tags {
      display: flex;
      gap: 1rem;

      .item {
        display: flex;
        align-items: center;
        justify-content: flex-start;
        gap: 1rem;
        font-size: 1.25rem;
        color: #1d1d1d;
        padding: 0.5rem 1rem;

        input {
          height: 24px;
          width: 24px;
        }
      }
    }

    &.project {
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
      align-items: center;

      & > .wrapper {
        flex: 0 0 auto;
        width: 66.66%;
        padding-right: 1rem;
        & > .wrapperDate {
          display: flex;

          .date, .step {
            color: #33333340;
            font-size: 1.25rem;
          }

          ul {
            margin: 0;
          }

          .step {
            color: #DD443F;
          }
        }

        h2 {
          font-size: 2.5rem;
        }

        p {
          font-size: 1.25rem;
        }
      }

      & > img {
        flex: 0 0 auto;
        width: 33.33%;
        border-radius: 24px;
      }
    }
  }

  .surface + .surface {
    margin-top: 24px;
  }

}
</style>
