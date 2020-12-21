<template>
  <div>
    <content class="main-container">
      <custom-header></custom-header>
      <config-container></config-container>
      <fps-evaluation></fps-evaluation>
    </content>
  </div>
</template>

<script>
import CustomHeader from "./components/StaticElements/TheHeader";
import ConfigContainer from "./components/ConfigElements/TheConfigContainer";
import FpsEvaluation from "./components/FpsEvaluationElements/FpsEvaluation";

export default {
  name: "App",

  components: { CustomHeader, ConfigContainer, FpsEvaluation },
};
</script>

<style>
html {
  box-sizing: border-box;
  font-size: 20px;
  overflow-y: auto;
}
body {
  margin: 0;
}
.main-container {
  font-family: "Bebas Neue", sans-serif;
  margin: 0;
  width: 100%;
  min-width: 20vw;
  max-width: 100vw;
  height: 100vh;
  min-height: 20vh;

  display: grid;
  grid-template-columns: [main-column]4fr [secondary-column1]5fr [secondary-column2]5fr [column-end];
  grid-template-rows: [header-row]1fr [content-row]9fr[row-end];
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
