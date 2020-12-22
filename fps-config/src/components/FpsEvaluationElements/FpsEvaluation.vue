<template>
  <div class="fps-container">
    <div v-if="!this.$store.getters.status" class="fps-info-box-empty">
      Добавьте элементы в сборку, результат появится здесь
    </div>
    <div v-else class="fps-info-box">
      <game-card :gameTitle="'AC Odyssey'"></game-card>
      <game-card :gameTitle="'AC Odyssey'"></game-card>
    </div>
  </div>
</template>

<script>
import gameCard from "./GameCard";
export default {
  components: { gameCard },
};
</script>

<style>
.fps-container {
  background-color: rgb(110, 110, 110);
  grid-row: content-row / span 1;
  grid-column: secondary-column2 / column-end;
  display: flex;
  justify-content: center;
  align-items: center;
}
.fps-info-box,
.fps-info-box-empty {
  background-color: rgb(206, 206, 206);
  font-family: sans-serif;
  text-align: center;
  grid-row: content-row / span 1;
  grid-column: secondary-column2 / column-end;
  display: flex;
  flex-direction: column;
  width: 100%;
  height: 80%;
  overflow: auto;
  overflow-x: hidden;
}
.fps-info-box-empty::-webkit-scrollbar {
  display: none;
}
.fps-info-box-empty {
  display: flex;
  justify-content: center;
  align-items: center;
}
.main-text {
  color: #000;
}
.secondary text {
  color: #000;
  grid-row: content-row / span 1;
  grid-column: secondary-column2 / column-end;
}
</style>
