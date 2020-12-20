<template>
  <div class="inner-header">
    <span class="title">120 FPS</span>
  </div>
  <div class="menu-actions">
    <div class="action-button">
      <span class="action-text">Ваши конфигурации</span>
    </div>
    <div class="action-button">
      <span class="action-text">Готовые сборки</span>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style scoped>
.inner-header {
  grid-column: main-column / secondary-column1;
  grid-row: header-row / content-row;
  background-color: black;
}
.title {
  color: rgb(238, 170, 62);
  font-size: 5rem;
  padding: 40px 10px;
  text-align: center;
  transition: color 0.2s linear;
}
.menu-actions {
  background-color: rgb(39, 39, 39);
  display: flex;
  justify-content: center;
  grid-column: secondary-column1 / column-end;
  grid-row: header-row / content-row;
}

.action-button {
  padding: 0 10px;
  color: rgb(238, 170, 62);
  flex-grow: 1;
  text-align: center;
  display: flex;
  align-items: center;
  transition: background-color 0.15s linear;
}
.action-text {
  font-family: "Open Sans";
  color: inherit;
  padding: 0 10px;
  font-size: 1.1rem;
}
.action-button:hover {
  background-color: rgb(238, 170, 62);
  color: white;
}
.action-button:active {
  background-color: rgb(121, 89, 39);
  color: white;
}
.title:hover {
  color: white;
}
</style>
