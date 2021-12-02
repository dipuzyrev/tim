<template>
  <div id="nav">
    <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link>
  </div>
  <div class="container">
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

#app {
  font-family: 'Moscow Sans', sans-serif;
  font-weight: normal;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

$container-max-widths: (
  sm: 540px,
  md: 720px,
  lg: 960px,
  xl: 1140px,
  xxl: 1320px
);

$grid-breakpoints: (
  sm: 576px,
  md: 768px,
  lg: 992px,
  xl: 1200px,
  xxl: 1400px
);

.container {
  width: 100%;
  padding: 0 1rem;
  margin: 0 auto;
  max-width: 100%;
  display: grid;
  place-items: center;
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
