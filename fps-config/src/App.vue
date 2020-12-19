<template>
  <div>
    <Header></Header>
    <content class="content-container">
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
.content-container {
  height: 90vh;
  display: flex;
  flex-basis: 0;
}
</style>
