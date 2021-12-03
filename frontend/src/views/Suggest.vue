<template>
  <div class="suggest">
    <div class="wrapperTitle">
      <h1>Оставить запрос на разработку решения</h1>
      <div class="backgroundImage">
        <img :src="require('@/assets/FAQ.svg')" alt="Pattern">
      </div>
    </div>
    <form @submit.prevent='onSubmit' class="questions">
      <div class="item">
        <h3>Что болит?</h3>
        <p>Опишите своими словами существующую в организации проблему. Можно сформулировать проблему в форму задачи</p>
        <textarea required name="mainProblem" id="mainProblem" v-model="mainProblem" cols="30" rows="10"></textarea>
      </div>
      <div class="item">
        <h3>У кого болит?</h3>
        <p>Кто является непосредственно ответственным за проблемный участок?</p>
        <textarea required name="mainProblemDesc" id="mainProblemDesc" v-model="mainProblemDesc" cols="30" rows="10"></textarea>
      </div>
      <div class="item">
        <h3>Как проявляется ваша проблема?</h3>
        <p>Приведите описание реальной ситуации, в которой проблема бы проявилась</p>
        <textarea required name="problemAppear" id="problemAppear" v-model="problemAppear" cols="30" rows="10"></textarea>
      </div>
      <div class="item">
        <h3>Какой желательный срок решения проблемы?</h3>
        <textarea required name="deadlines" id="deadlines" v-model="deadlines" cols="30" rows="10"></textarea>
      </div>
      <div class="item">
        <h3>Что будет если проблему не решать?</h3>
        <p>Опишите нежелательные эффекты, которые возникают или могут возникнуть из-за того, что проблема не решается</p>
        <textarea required name="whatIf" id="whatIf" v-model="whatIf" cols="30" rows="10"></textarea>
      </div>
      <div class="item">
        <h3>Пробовали решать?</h3>
        <p>Как пытались решить проблему ранее? Почему эти попытки оказались неудачными или почему были признаны неудачными? Чем не устроили найденные решения? Общались ли с рынком? Если да, то с кем?</p>
        <textarea required name="tryBefore" id="tryBefore" v-model="tryBefore" cols="30" rows="10"></textarea>
      </div>
      <div class="item">
        <h3>Почему так происходит?</h3>
        <p>Какие на ваш взгляд ключевые причины возникновения проблемы? Что на ваш взгляд является причиной возникновения проблемы?</p>
        <textarea required name="whyItGoes" id="whyItGoes" v-model="whyItGoes" cols="30" rows="10"></textarea>
      </div>
      <div class="item">
        <h3>Как с вами связаться?</h3>
        <p>Укажите наименование вашего предприятия, ваши ФИО, и телефон для связи.</p>
        <textarea required name="contact" id="contact" v-model="contact" cols="30" rows="10"></textarea>
      </div>

      <button type="submit">Отправить</button>
    </form>
  </div>
</template>

<script>
import { ref } from '@vue/reactivity'
import axios from 'axios'
import { useRouter } from 'vue-router'

export default {
  setup () {
    const mainProblem = ref('')
    const mainProblemDesc = ref('')
    const problemAppear = ref('')
    const deadlines = ref('')
    const whatIf = ref('')
    const tryBefore = ref('')
    const whyItGoes = ref('')
    const contact = ref('')
    const router = useRouter()

    const onSubmit = () => {
      axios.post('/api/custom_request/', {
        pain: mainProblem.value,
        problem: mainProblemDesc.value,
        what_if: whatIf.value,
        whose_pain: problemAppear.value,
        period: deadlines.value,
        tried: tryBefore.value,
        contacs: contact.value
      })

      router.back()
    }

    return {
      mainProblem,
      mainProblemDesc,
      problemAppear,
      deadlines,
      whatIf,
      tryBefore,
      whyItGoes,
      contact,
      onSubmit
    }
  }
}
</script>

<style lang="scss" scoped>
.suggest {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  align-items: center;
  gap: 4rem;

  h1 {
    font-size: 4.875rem;
  }

  & > * {
    flex: 1 0 0%;
  }

  .wrapperTitle {
    display: flex;
    justify-items: space-between;
    gap: 5rem;

    & > .backgroundImage {
      display: flex;
      overflow: visible;
      width: 280px;
    }
  }

  .questions {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 4rem 2rem;

    & > .item {
      flex: 0 0 auto;
      width: calc(50% - 1rem);
      display: flex;
      flex-flow: column;
      justify-content: space-between;
    }

    h3 {
      font-size: 2.375rem;
      margin: 0;
      margin-bottom: .75rem;
    }

    p {
      font-size: 1.125rem;
      color: #333333;
      margin: 0;
    }

    textarea {
      margin-top: 1.5rem;
      background: #FFFFFF;
      border: 1px solid #EBEBEB;
      box-sizing: border-box;
      border-radius: 4px;
      width: 100%;
      padding: 1rem;
      font-family: 'Moscow Sans', sans-serif;
      color: #000;
      font-size: 1.125rem;
    }

    button {
      background: #DA3832;
      border: 1px solid #EBEBEB;
      box-sizing: border-box;
      border-radius: 4px;
      padding: 12px 80px;
      color: #FFFFFF;
      font-size: 1.25rem;
      cursor: pointer;
    }
  }
}
</style>
