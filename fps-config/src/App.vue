<template>
  <div>
    <Header></Header>
    <content>
      <config-container></config-container>
    </content>
    <p>{{ this.$store.getters.currentMotherboard }}</p>
  </div>
</template>

<script>
import Header from "./components/StaticElements/TheHeader";
import ConfigContainer from "./components/ConfigElements/TheConfigContainer";

export default {
  name: "App",

  components: { Header, ConfigContainer },
};
</script>

<style>
ConfigContainere > html {
  box-sizing: border-box;
  font-size: 20px;
}
body {
  margin: 0;
}
</style>
