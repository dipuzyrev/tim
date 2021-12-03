<template>
  <div class="search">
    <div class="surface">
      <div class="search">
        <img :src="require('@/assets/Search.png')" alt="Search">
        <input v-model="textToSearch" type="text" placeholder="Метро">
      </div>

      <div class="tags">
        <span>Найдено результатов: {{ searchedProducts.length }}</span>
      </div>

    </div>
    <div class="wrapperContent">
      <div class="filters surface">
        <div class="tags">
          <h2>Теги</h2>
          <div class="wrapperTags">
            <div class="bubble" @click="identity = !identity" :class="{active: identity}">Идентификация</div>
            <div class="bubble" @click="payment = !payment" :class="{active: payment}">Оплата</div>
            <div class="bubble" @click="eco = !eco" :class="{active: eco}">Экология</div>
            <div class="bubble" @click="safety = !safety" :class="{active: safety}">Безопасность</div>
            <div class="bubble" @click="geo = !geo" :class="{active: geo}">Геолокация</div>
            <div class="bubble">...</div>
          </div>
        </div>

        <div class="priorityOrganizations">
          <h2>Приоритетные организации</h2>
          <div class="wrapperOrganizations">
            <div class="bubble" @click="MosMetro = !MosMetro" :class="{active: MosMetro}">Московский метрополитен</div>
            <div class="bubble" @click="MosGorTrans = !MosGorTrans" :class="{active: MosGorTrans}">Мосгортранс</div>
            <div class="bubble" @click="CODD = !CODD" :class="{active: CODD}">ЦОДД</div>
            <div class="bubble" @click="AMPP = !AMPP" :class="{active: AMPP}">АМПП</div>
            <div class="bubble" @click="OrgPer = !OrgPer" :class="{active: OrgPer}">Организатор перевозок</div>
            <div class="bubble" @click="MosTransPorj = !MosTransPorj" :class="{active: MosTransPorj}">Мостранспроект</div>
          </div>
        </div>

        <div class="pilot">
          <h2>Пилот</h2>
          <div class="wrapperPilot">
            <div>
              <input type="radio" name="pilot" id="notMatter" value="notMatter" v-model="pilot">
              <label for="notMatter">Не важно</label>
            </div>
            <div>
              <input type="radio" name="pilot" id="no" value="no" v-model="pilot">
              <label for="no">Нет</label>
            </div>
            <div>
              <input type="radio" name="pilot" id="wip" value="wip" v-model="pilot">
              <label for="wip">В прогрессе</label>
            </div>
            <div>
              <input type="radio" name="pilot" id="passed" value="passed" v-model="pilot">
              <label for="passed">Прошло</label>
            </div>
            <div v-if="pilot === 'passed'">
              <input type="checkbox" name="pilot" id="success" v-model="successful">
              <label for="success">Удачно</label>
            </div>
          </div>
        </div>
      </div>
      <div class="cases">
        <template v-if="searchedProducts.length">
      <a href="#" @click="goTo(proj)" class="surface project" v-for="(proj, index) in searchedProducts" :key="index">
        <div class="wrapper">
          <div class="wrapperDate">
            <div class="date">{{ new Date(proj.application_date).toLocaleDateString('ru-ru')}}</div>
          </div>

          <h2>{{proj.title}}</h2>

          <p>{{proj.description}}</p>
        </div>
      </a>
    </template>
    <template v-else>
      <div class="surface project">
        <div class="wrapper">
          <div class="wrapperDate">
            <div class="step">Проблема</div>
          </div>

          <h2>Не нашли, <br> что искали?</h2>

          <p>По вашему запросу ничего не найдено. <router-link class="lnk" to="/suggest">Предложите идею</router-link> или <a href="https://t.me/SeamMiner" class="lnk">свяжитесь с нами.</a></p>
        </div>
      </div>
    </template>
      </div>
    </div>

  </div>
</template>

<script>
import { ref } from '@vue/reactivity'
import { useRoute, useRouter } from 'vue-router'
import { useStore } from 'vuex'
import axios from 'axios'

import { computed, onMounted } from '@vue/runtime-core'
export default {

  setup () {
    const route = useRoute()
    const router = useRouter()
    const store = useStore()

    const textToSearch = ref(route.query.q || '')

    const MosMetro = ref(false)
    const MosGorTrans = ref(false)
    const CODD = ref(false)
    const AMPP = ref(false)
    const OrgPer = ref(false)
    const MosTransPorj = ref(false)

    const identity = ref(false)
    const payment = ref(false)
    const eco = ref(false)
    const safety = ref(false)
    const geo = ref(false)

    const pilot = ref('notMatter')
    const successful = ref(false)

    const projects = ref([])
    const pilots = new Map([
      ['no', '1'],
      ['wip', '2'],
      ['passed', '3']
    ])

    const getInfo = async () => {
      axios.get('/api/projects/').then(
        (result) => {
          result.data.projects.forEach((project) => {
            projects.value.push(project.fields)
          })
        }
      ).catch(e => alert(e))
    }

    const filteredProjects = computed(() => {
      return projects.value.filter((item) => {
        return (
          (MosMetro.value && item.tags.includes('MosMetro')) ||
         (MosGorTrans.value && item.tags.includes('MosGorTrans')) ||
          (CODD.value && item.tags.includes('CODD')) ||
          (AMPP.value && item.tags.includes('analize')) ||
          (OrgPer.value && item.tags.includes('OrgPer')) ||
          (MosTransPorj.value && item.tags.includes('MosTransPorj')) ||
          (identity.value && item.tags.includes('identification')) ||
          (payment.value && item.tags.includes('payment')) ||
          (eco.value && item.tags.includes('eco')) ||
          (safety.value && item.tags.includes('safety')) ||
         (geo.value && item.tags.includes('geo')) ||
          (item.pilot === pilots.get(pilot.value)) ||
          (item.success_pilot === successful.value && pilot.value === 'passed')
        )
      })
    })

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

    const goTo = (project) => {
      store.commit('change', project)
      router.push('/listing')
    }

    onMounted(() => {
      getInfo()
    })

    return {
      textToSearch,
      identity,
      payment,
      eco,
      safety,
      geo,
      MosMetro,
      MosGorTrans,
      CODD,
      AMPP,
      OrgPer,
      MosTransPorj,
      searchedProducts,
      pilot,
      successful,
      goTo
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
    margin-top: 24px;

    & > .search {
      display: flex;
      align-items: center;
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
        font-size: 2.375rem;
        color: #000;
        width: 100%;

        &:focus {
          outline: none;
          box-shadow: none;
        }
      }
    }

    .tags {

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
      color: #000000;
      text-decoration: none;

      :hover {
        cursor: pointer;
      }

      & > .wrapper {

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
    }
  }

  .lnk {
    font-size: 1.25rem;
    color: #DD443F;
    border-bottom: 1px solid #EAB9B7;
    text-decoration: none;

    &:hover {
      color: #DD443F80;
    }

  }

  .wrapperContent {
    display: flex;
    flex-wrap: wrap;
    gap: 1.5rem;

    & > * {
      flex: 0 0 auto;
    }

    & > .filters {
      width: calc(33.33% - .75rem);
    }

    & > .cases {
      width: calc(66.66% - .75rem);
    }
  }

  .wrapperTags, .wrapperOrganizations, .wrapperPilot {
    display: flex;
    flex-wrap: wrap ;
    // align-items: center;
    gap: 1rem;
  }

  .wrapperPilot {
    flex-flow: column;

    label {
      margin-left: 1rem;
    }
  }

  .bubble {
    padding: calc(.75rem - 1px) 1rem .75rem;
    background: #F5F6F7;
    border-radius: 12px;
    color: #333333;

    &:hover {
      cursor: pointer
    }

    &.active {
      background: #333333;
      color: #F5F6F7;
    }
  }

}
</style>
