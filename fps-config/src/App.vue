<template>
  <div>
    <content class="main-container">
      <Header></Header>
      <config-container></config-container>
      <fps-evaluation></fps-evaluation>
    </content>
  </div>
</template>

<script>
import Header from "./components/StaticElements/TheHeader";
import ConfigContainer from "./components/ConfigElements/TheConfigContainer";
import FpsEvaluation from "./components/FpsEvaluationElements/FpsEvaluation";

export default {
  name: "App",

  components: { Header, ConfigContainer, FpsEvaluation },
};
</script>

<style>
html {
  box-sizing: border-box;
  font-size: 20px;
  overflow-y: hidden;
}
body {
  margin: 0;
}
.main-container {
  font-family: "Bebas Neue", "Courier New", Courier;

  height: 100vh;
  min-height: 15vh;
  max-height: 100vh;
  margin: 0;
  width: 100vw;
  min-width: 20vw;
  max-width: 100vw;

  display: grid;
  grid-template-columns: [main-column]2fr [secondary-column1]1fr [secondary-column2]1fr [column-end];
  grid-template-rows: [header-row]1fr [content-row]9fr[row-end];
}
</style>
