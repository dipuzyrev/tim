<template>
  <div class="collapse" @click="show = !show">
    <div class="title" :class="{'show': show}">{{title}}</div>
    <div class="content" :class="{'show': show}">
      <slot></slot>
    </div>
  </div>
</template>

<script>
import { ref } from '@vue/reactivity'
export default {
  props: ['title'],

  setup () {
    const show = ref(false)

    return {
      show
    }
  }
}
</script>

<style lang="scss" scoped>
.collapse {
  padding: 1.5rem 0;
  border-bottom: 1px solid #E5E6EB;

  .title {
    font-size: 1.5rem;
    color: #1D1D1D;
    cursor: pointer;
    padding-right: 2rem;
    display: block;
    position: relative;

    &:before {
      content: "";
      position: absolute;
      right: 8px;
      top: calc(50% - 1px);
      width: 14px;
      height: 2px;
      background-color: rgba(0,0,0,.85);
      border-radius: 1px;
      transition: transform .3s ease-in-out;
    }

    &:not(.show):before {
      transform: rotate(180deg);
    }

    &:after {
      content: "";
      position: absolute;
      right: 8px;
      top: calc(50% - 1px);
      width: 14px;
      height: 2px;
      background-color: rgba(0,0,0,.85);
      border-radius: 1px;
      transition: transform .3s ease-in-out;
    }

    &:not(.show):after {
      top: calc(50% - 1px);
      transform: rotate(90deg);
    }
  }

  .content {
    background: #FFFFFF;
    border-radius: 12px;

    &:not(.show) {
      height: 0;
      overflow: hidden;
    }

    &.show {
      margin-top: 1.5rem;
      padding: 2rem 1rem;
    }
  }
}
</style>
