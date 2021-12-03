<template>
  <div
    class="dropdown"
  >
    <button
      class="toggle"
      @click="showDialog = !showDialog;"
    >
      <span class="text">{{ title }}</span>
      <div
        class="arrow"
        :class="{'up': showDialog}"
      >
        <svg width="10" height="6" viewBox="0 0 10 6" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path fill-rule="evenodd" clip-rule="evenodd" d="M0.608279 0.683058C0.86398 0.438981 1.27855 0.438981 1.53425 0.683058L4.99984 3.99112L8.46542 0.683058C8.72112 0.438981 9.13569 0.438981 9.39139 0.683058C9.64709 0.927136 9.64709 1.32286 9.39139 1.56694L5.46282 5.31694C5.20712 5.56102 4.79255 5.56102 4.53685 5.31694L0.608279 1.56694C0.352579 1.32286 0.352579 0.927136 0.608279 0.683058Z" />
        </svg>
      </div>
    </button>
    <transition name="dropdown-dialog">
      <div class="dialog" v-show="showDialog">
        <slot></slot>
      </div>
    </transition>
  </div>
</template>

<script>
import { ref } from 'vue'

export default {
  name: 'LanguageSelector',

  props: ['title'],

  setup () {
    const showDialog = ref(false)

    return {
      showDialog
    }
  }
}
</script>

<style lang="scss" scoped>
.dropdown {
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  position: relative;

  .toggle {
    background: none;
    border: 1px solid #EBEBEB;
    border-radius: .5rem;
    outline: none;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: .75rem 1rem;
    color: #000000;
    font-size: 1.375rem;
    transition: background-color .2s ease-out;

    &:hover {
      cursor: pointer;
    }

    .text {
      margin-right: .625rem;
    }

    .arrow {
      display: inline-block;
      transition: all .3s ease-out;
      position: relative;

      svg {
        width: .875rem;
        height: auto;

        path {
          fill: #CCCCCC;
        }
      }

      &.up {
        transform: rotate(180deg)
      }
    }
  }

  .dialog {
    list-style: none;
    margin: 0;
    padding: .75rem 0rem;
    background-color: #FFFFFF;
    border: 1px solid #EBEBEB;
    border-radius: .375rem;
    position: absolute;
    right: 0;
    top: calc(100% + .25rem);
    // width: 10rem;
    box-shadow: 0px 5px 10px 0px #00000010;
    font-weight: normal;

    & > * {
      padding: .375rem 1rem;
    }

    &:hover {
      cursor: pointer;
    }
  }
}

.dropdown-dialog-enter-active {
  transition: all 0.1s ease-out;
}

.dropdown-dialog-leave-active {
  transition: all 0.1s ease-in;
}

.dropdown-dialog-enter-from,
.dropdown-dialog-leave-to {
  transform: translateY(-0.625rem);
  transform: scale(.8);
  opacity: 0;
}
</style>
