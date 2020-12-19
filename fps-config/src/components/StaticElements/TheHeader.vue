<template>
  <header class="main-container">
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
  </header>
</template>

<script>
export default {};
</script>

<style scoped>
.main-container {
  background-color: rgb(39, 39, 39);
  line-height: 450%;
  font-family: "Bebas Neue", "Courier New", Courier;
  text-align: center;
  min-height: 75px;
  margin: 0;
  display: flex;
  flex-basis: 0;
  top: 0;
  left: 0;
  width: 100%;
}
.inner-header {
  justify-content: left;
  flex-grow: 4;
  background-color: black;
}
.title {
  color: rgb(238, 170, 62);
  font-size: 2rem;
  margin: 0 auto;
  text-align: center;
  transition: color 0.2s linear;
}
.menu-actions {
  display: flex;
  justify-content: flex-end;
  align-items: center;
  flex-grow: 1;
}

.action-button {
  padding: 0 10px;

  color: rgb(238, 170, 62);
  height: 100%;
  width: 100%;
  font-size: 1.1rem;
  flex-basis: 1;
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

@media screen and (max-width: 640px) {
  .main-container {
    flex-direction: column;
  }
  .menu-actions {
    justify-content: space-around;
  }
}
</style>
