<template>
  <div class="faq">
    <div class="wrapperTitle">
      <h1>Часто задаваемые вопросы</h1>
      <div class="backgroundImage">
        <img :src="require('@/assets/FAQ.svg')" alt="Pattern">
      </div>
    </div>
    <div class="questions">
      <template v-for="(answer, question, index) in config" :key="index">
        <Collapse :title="question">
          {{answer}}
        </Collapse>
      </template>
    </div>
  </div>
</template>

<script>
import Collapse from '@/components/Collapse.vue'
import { ref } from '@vue/reactivity'
export default {
  components: {
    Collapse
  },

  setup () {
    const config = ref({
      'Могу ли я подать заявку, если мой продукт не связан напрямую с транспортом?': 'Мы в любом случае рассмотрим все заявки. От промышленного дизайна до рекламных технологий. Но приоритет для участия в акселераторе будет отдан проектам, соответствующим технологическим направлениям отбора.',
      'Могу ли я подать заявку, если я являюсь сотрудником транспортного комплекса?': 'aboba',
      'Могу ли я подать заявку, если у меня нет MVP, но есть хорошая идея?': 'aboba',
      'Могу ли я проходить акселератор, если у меня нет команды?': 'aboba',
      'Моего вопроса тут нет, что мне делать?': 'aboba',
      'Могу ли я подать заявку, если я являюсь сотрудником транспортного ?': 'aboba',
      'Могу ли я подать заявку, если я являюсь сотрудником?': 'aboba',
      'Могу ли я подать заявку, если я являюсь?': 'aboba'

    })

    return {
      config
    }
  }
}
</script>

<style lang="scss" scoped>
.faq {
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
    flex-flow: column;
    justify-items: space-between;
    gap: 5rem;

    & > .backgroundImage {
      display: flex;
      justify-content: center;
      width: 100px;
      overflow: visible;
    }
  }
}
</style>
