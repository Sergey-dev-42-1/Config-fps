<template>
  <div class="fps-container">
    <div v-if="!this.$store.getters.status" class="fps-info-box">
      Добавьте элементы в сборку, результат появится здесь
    </div>
    <div v-else class="fps-info-box">
      Готово
    </div>
  </div>
</template>

<script>
export default {};
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
.fps-info-box {
  background-color: rgb(206, 206, 206);
  font-family: sans-serif;
  text-align: center;
  grid-row: content-row / span 1;
  grid-column: secondary-column2 / column-end;
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 80%;
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
