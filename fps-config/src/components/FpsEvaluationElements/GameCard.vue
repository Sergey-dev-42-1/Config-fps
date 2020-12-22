<template>
  <div class="game-grid-container">
    <div class="game-card">
      <img class="game-picture" :src="gameImg" />
      <div class="game-title">{{ gameTitle }}</div>
    </div>
    <div class="eval-result">
      Ожидаемый FPS на ультра настройках в FullHD разрешении:
      <span class="evaluation-fps">{{ evaluate }} </span>
    </div>
  </div>
</template>

<script>
import evaluation from "./evalution";
var images = require.context("../../../public/img/games", false, /\....$/);
export default {
  components: {},
  props: { gameTitle: String },
  computed: {
    gameImg: function() {
      try {
        return images("./" + this.gameTitle + ".jpg");
      } catch {
        return images("./" + this.gameTitle + ".png");
      }
    },
    evaluate: function() {
      let getters = this.$store.getters;
      return evaluation.evaluate(
        getters.currentCPU,
        getters.currentVideocard,
        getters.currentMemory,
        getters.currentDataDrive,
        this.gameTitle
      );
    },
  },
};
</script>

<style scoped>
.game-grid-container {
  background-color: white;
  margin: 10px 10px 0 10px;
  width: 100%;
  height: 342.5px;
  display: grid;
  grid-template: 1fr / 1fr 9fr;
  border-radius: 10px;
}
.game-card {
  color: white;

  width: 300px;
  height: 100%;
  border-radius: 10px;
  display: flex;

  flex-direction: column;
  align-items: center;
  justify-content: center;
  grid-template: 2/3;
}
.game-title {
  font-weight: bold;
  color: black;
  align-self: center;
  justify-self: flex-end;
  width: 100%;
  border-radius: 00px 0px 0 10px;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 10px 0px;
  background-color: rgb(255, 255, 255);
}
.game-picture {
  background-color: transparent;
  border-radius: 10px 0 0 0;
  width: 100%;
  height: 300px;
  margin-top: auto;
}
.eval-result {
  font-weight: bold;
  color: black;
  align-self: center;
  width: 100%;
  height: 100%;
  display: flex;
  border-radius: 0 10px 10px 0px;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background-color: rgb(255, 255, 255);
  grid-column: 2/3;
}
.evaluation-fps {
  font-family: "Bebas Neue";
  background-color: black;
  font-size: 30px;
  width: 60px;
  height: 60px;
  color: orange;
  border-radius: 10px;
  display: flex;
  justify-content: center;
  align-items: center;
}
.btn-close {
  border: none;
  font-size: 20px;
  cursor: pointer;
  font-weight: bold;
  color: #000000;
  margin: 10px 10px 0 0;
  background: transparent;
  justify-self: flex-start;
  align-self: flex-end;
}
</style>
