<template>
  <div class="home">
    <div class="wrapperTitle">
      <div class="title">
        <h1>Транспортные инновации Москвы</h1>
        <form @submit.prevent='onSubmit(query)'>
          <input type="text" v-model="query" id="search">
          <img :src="require('@/assets/Search.png')" alt="Search">
        </form>
      </div>
      <div class="backgroundImage">
        <img :src="require('@/assets/01.svg')" alt="Pattern">
      </div>
    </div>

    <div class="cards">
      <router-link to="/search" class="card catalogue">
        Каталог проектов
      </router-link>
      <router-link to="/suggest" class="card idea">
        Предложить<br>идею
      </router-link>
      <a href="https://t.me/SeamMiner" class="card connect">
        Связаться с нами
      </a>
    </div>

  </div>
</template>

<script>
import { ref } from '@vue/reactivity'
import { useRouter } from 'vue-router'

export default {
  name: 'Home',

  setup () {
    const query = ref('')
    const router = useRouter()

    const onSubmit = (query) => {
      router.push({ path: 'search', query: { q: query } })
    }

    return {
      query,
      onSubmit
    }
  }
}
</script>

<style lang="scss" scoped>
.home {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  align-items: center;
  gap: 4rem;

  h1 {
    font-size: 4.875rem;
  }

  form {
    position: relative;

    img {
      height: 21px;
      width: 20px;
      position: absolute;
      left: 2rem;
      top: calc(50% - 10.5px)
    }

    input {
      background: #FFFFFF;
      border-radius: 24px;
      border: none;
      padding: 30px 2rem 30px 4rem;
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

  .wrapperTitle {
    display: flex;
    justify-content: space-between;
    gap: 5rem;

    & > .backgroundImage {
      width: 100px;
      overflow: visible;
    }
  }

  .cards {
    display: flex;
    flex-wrap: wrap;
    gap: 1.5rem;
    width: 100%;

    .card {
      text-decoration: none;
      height: 310px;

      &.catalogue {
        width: 475px;
        padding: 2rem 1.5rem;
        background: url('../assets/Catalogue.png');
        background-size: 100% 100%;
        border-radius: 24px;
        color: #FFFFFF;
        font-weight: bold;
        font-size: 1.75rem;
      }

      &.idea, &.connect {
        width: 292px;
        padding: 1.5rem 1rem;
        display: flex;
        align-items: flex-end;
        background: url('../assets/Idea.png');
        background-size: 100% 100%;
        border-radius: 24px;
        color: #FFFFFF;
        font-weight: bold;
        font-size: 1.675rem;
      }

      &.connect {
        background: url('../assets/Connect.png');
        background-size: 100% 100%;
      }
    }
  }

}
</style>
