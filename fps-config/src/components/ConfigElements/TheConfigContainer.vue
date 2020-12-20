<template>
  <div class="config-main-container">
    <div class="configuration-container">
      <category-card></category-card>
      <category-card></category-card>
      <category-card></category-card>
      <category-card></category-card>
      <category-card></category-card>
      <category-card></category-card>
    </div>
  </div>
</template>

<script>
import CategoryCard from "./CategoryCard.vue";
export default {
  components: { CategoryCard },
};
</script>

<style>
.config-main-container {
  background-color: orange;
  grid-row: content-row / span 1;
  grid-column: main-column / span 2;
  display: flex;
  align-items: center;
  justify-content: center;
}
.configuration-container {
  background-color: rgb(255, 255, 255);
  width: 100%;
  height: 80%;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
  gap: 10px 10px;
  align-items: center;
  justify-items: center;
}
</style>
