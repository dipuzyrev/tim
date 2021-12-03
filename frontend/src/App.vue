<template>
  <div class="container">
    <div id="nav">
      <router-link class="link" to="/">
        <img class="logo" :src="require('@/assets/Logo.svg')" alt="Logo">
      </router-link>
      <div class="links">
        <router-link class="link" to="/search">Каталог проектов</router-link>
        <a href="#" @click="alert('Вы авторизированы успешно')" class="link">Войти</a>
        <router-link class="link idea" to="/suggest">Предложить идею</router-link>
      </div>
    </div>
    <router-view/>
  </div>
</template>

<style lang="scss">
body {
  margin: 0;
}

$fonts: (
  regular: 400,
  medium: 500,
  bold: 700,
  extrabold: 900
);

@each $weight, $value in $fonts {
  @font-face {
    font-family: 'Moscow Sans';
    src: url('./assets/' + $weight +'.ttf') format("truetype");
    font-weight: $value;
    font-style: normal;
  }
}

*, *:before, *:after {
  transition: all .3s ease-in-out;
  box-sizing: border-box;
}

#app {
  font-family: 'Moscow Sans', sans-serif;
  font-weight: normal;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #000000;
  background: #F5F6F7;
  min-height: 100vh;
  overflow: hidden;
  padding-bottom: 10rem;
}

#nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem;
}

.links {
  display: flex;
}

.link {
  font-size: 1.375rem;
  color: #000000;
  text-decoration: none;
  text-align: center;
  display: block;

  &:hover {
    color: #00000080;
  }

  &.idea {
    color: #DD443F;
    border-bottom: 1px solid #EAB9B7;

    &:hover {
      color: #DD443F80;
    }
  }
}

.logo  {
  width: 180px;
}

@media (max-width: 767.98px) {
  .logo {
    width: 120px;
  }
}

@media (max-width: 991.98px) {
  .link {
    font-size: 1rem;
  }

  .link:not(.idea) {
    display: none;
  }
}

.link + .link {
  margin-left: 32px;
}

$container-max-widths: (
  sm: 540px,
  md: 720px,
  lg: 960px,
  xl: 1140px,
);

$grid-breakpoints: (
  sm: 576px,
  md: 768px,
  lg: 992px,
  xl: 1200px,
);

.container {
  width: 100%;
  padding: 0 1rem;
  margin: 0 auto;
  max-width: 100%;
  display: grid;
}

@each $breakpoint, $container-max-width in $container-max-widths {
  $media-breakpoint: map-get($grid-breakpoints, $breakpoint);
  @media (min-width: $media-breakpoint) {
    .container {
      max-width: $container-max-width;
    }
  }
}

@for $i from 1 through 12 {
  .row-#{$i} {
    grid-row: span $i;
  }
  .col-#{$i} {
    grid-column: span $i;
  }
}

</style>
