<template>
  <div class="search">
    <div class="surface">
      <div class="search">
        <img :src="require('@/assets/Search.png')" alt="Search">
        <input v-model="textToSearch" type="text">
        <!-- TODO: добавить algolia поиск короче -->
      </div>

      <div class="tags">
        <div class="tags">
          <DropDown title="Технологическое направление">
            <div class="item">
              <input type="checkbox" name="cityTansport" id="cityTansport" v-model="cityTansport" style="width: 37px">
              <label for="cityTansport">Доступный и комфортный городской транспорт</label>
            </div>
            <div class="item">
              <input type="checkbox" name="newTypes" v-model="newTypes" id="newTypes">
              <label for="newTypes">Новые виды мобильности</label>
            </div>
            <div class="item">
              <input type="checkbox" name="safetyRoad" v-model="safetyRoad" id="safetyRoad">
              <label for="safetyRoad">Безопасность дорожного движения</label>
            </div>
            <div class="item">
              <input type="checkbox" name="healthyStreets" v-model="healthyStreets" id="healthyStreets">
              <label for="healthyStreets">Здоровые улицы и экология</label>
            </div>
            <div class="item">
              <input type="checkbox" name="digitalTech" id="digitalTech" v-model="digitalTech" style="width: 28px">
              <label for="digitalTech">Цифровые технологии в&nbsp;транспорте</label>
            </div>

          </DropDown>
          <DropDown title="Стадия проекта">
            <div class="item">
              <input type="checkbox" name="Idea" v-model="idea" id="idea">
              <label for="idea">Идея</label>
            </div>
            <div class="item">
              <input type="checkbox" name="Accelerator" v-model="accelerator" id="accelerator">
              <label for="accelerator">Аккселератор</label>
            </div>
            <div class="item">
              <input type="checkbox" name="Pilot" v-model="pilot" id="pilot">
              <label for="pilot">Пилот</label>
            </div>

          </DropDown>
        </div>
        <span>Найдено {{ searchedProducts.length }} продуктов</span>
      </div>

    </div>
    <div class="surface project" v-for="(proj, index) in searchedProducts" :key="index">
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
import { computed } from '@vue/runtime-core'
export default {
  components: {
    DropDown
  },

  setup () {
    const route = useRoute()

    const textToSearch = ref(route.query.q)

    const cityTansport = ref(false)
    const newTypes = ref(false)
    const safetyRoad = ref(false)
    const healthyStreets = ref(false)
    const digitalTech = ref(false)

    const idea = ref(false)
    const accelerator = ref(false)
    const pilot = ref(true)

    const projects = ref([
      {
        title: 'Titan Power Solution: без проводов к дорожным камерам',
        description: 'Суперконденсаторный источник бесперебойного питания (ИБП) — решение для обеспечения безотказной работы автоматизированных систем управления дорожным движением.',
        date: '01.01.2021',
        step: 'Пилот',
        pilot: true,
        cityTansport: true
      },
      {
        title: 'Titan Power Solution: без проводов к дорожным камерам',
        description: 'Суперконденсаторный источник бесперебойного питания (ИБП) — решение для обеспечения безотказной работы автоматизированных систем управления дорожным движением.',
        date: '02.01.2021',
        step: 'Пилот',
        thumbnail: '1.png',
        accelerator: true,
        newTypes: true
      },
      {
        title: 'Titan Power Solution: без проводов к дорожным камерам',
        description: 'Суперконденсаторный источник бесперебойного питания (ИБП) — решение для обеспечения безотказной работы автоматизированных систем управления дорожным движением.',
        date: '03.01.2021',
        step: 'Пилот',
        thumbnail: '1.png',
        idea: true,
        safetyRoad: true
      }
    ])

    const filteredProjects = computed(() => {
      return projects.value.filter((item) => {
        return (
          item.cityTansport === cityTansport.value ||
          item.newTypes === newTypes.value ||
          item.safetyRoad === safetyRoad.value ||
          item.healthyStreets === healthyStreets.value ||
          item.digitalTech === digitalTech.value ||
          item.idea === idea.value ||
          item.accelerator === accelerator.value ||
          item.pilot === pilot.value
        )
      })
    })

    // watchEffect(() => {
    //   filteredProjects.value = projects.value.filter((item) => {
    //     return (
    //       !!item.cityTansport === cityTansport.value ||
    //       !!item.newTypes === newTypes.value ||
    //       !!item.safetyRoad === safetyRoad.value ||
    //       !!item.healthyStreets === healthyStreets.value ||
    //       !!item.digitalTech === digitalTech.value ||
    //       !!item.idea === idea.value ||
    //       !!item.accelerator === accelerator.value ||
    //       !!item.pilot === pilot.value
    //     )
    //   })
    // })

    const searchedProducts = computed(() => {
      return filteredProjects.value.filter((projects) => {
        return (
          projects.title
            .toLowerCase()
            .indexOf(textToSearch.value.toLowerCase()) !== -1
        )
      }).sort((a, b) => {
        return new Date(b.date) - new Date(a.date)
      })
    })

    return {
      textToSearch,
      cityTansport,
      newTypes,
      safetyRoad,
      healthyStreets,
      digitalTech,
      idea,
      accelerator,
      pilot,
      searchedProducts
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
      justify-content: space-between;
      align-items: center;
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

      span {
        font-size: 1.375rem;
        color: #00000040;
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
        padding-right: 5rem;

         @media (max-width: 991.98px) {
          width: 100%;
        }

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

        @media (max-width: 991.98px) {
          width: 100%;
        }
      }
    }
  }

  .surface + .surface {
    margin-top: 24px;
  }

}
</style>
