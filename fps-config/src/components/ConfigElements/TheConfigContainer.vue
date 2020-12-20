<template>
  <div class="config-main-container">
    <div class="configuration-container">
      <category-card
        v-for="(item, index) in categories"
        :key="index"
        :category="item"
      ></category-card>
    </div>
  </div>
</template>

<script>
import CategoryCard from "./CategoryCard.vue";
export default {
  data() {
    return {
      categories: [
        "Материнская плата",
        "Процессор",
        "Видеокарта",
        "Оперативная память",
        "Накопитель данных",
        "Блок питания",
      ],
    };
  },
  components: { CategoryCard },
};
</script>

<style>
.config-main-container {
  background-color: orange;
  grid-row: content-row / span 1;
  grid-column: main-column / span 2;
  display: flex;
  flex-basis: 0;
  align-items: center;
  justify-content: center;
}
.configuration-container {
  background-color: rgb(255, 255, 255);
  width: 100%;
  min-height: 80%;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-wrap: wrap;
}
</style>
