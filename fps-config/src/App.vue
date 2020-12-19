<template>
  <div>
    <Header></Header>
    <p>{{ this.$store.getters.currentMotherboard }}</p>
  </div>
</template>

<script>
import Header from "./components/StaticElements/TheHeader";
export default {
  name: "App",

  components: { Header },
};
</script>

<style>
html {
  box-sizing: border-box;
  font-size: 20px;
}
body {
  margin: 0;
}
</style>
