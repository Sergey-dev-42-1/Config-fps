<template>
  <div class="config-main-container">
    <div class="configuration-container">
      <div v-for="(item, index) in categories" :key="index">
        <category-card
          v-if="checkCategory(item)"
          @chooseItem="setItem"
          :category="item"
        ></category-card>
        <element-card
          @dropItem="dropItem"
          @chooseItem="setItem"
          v-else
          :item="showElement(item)"
          :category="item"
        ></element-card>
      </div>
    </div>
  </div>
</template>

<script>
import CategoryCard from "./CategoryCard.vue";
import ElementCard from "./ElementCard.vue";
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
  components: { CategoryCard, ElementCard },
  methods: {
    setItem(args) {
      console.log(args);
      if (args.category === "Материнская плата") {
        this.$store.dispatch("setCurrentMotherboard", args.component);
      } else if (args.category === "Процессор") {
        this.$store.dispatch("setCurrentCPU", args.component);
      } else if (args.category === "Видеокарта") {
        this.$store.dispatch("setCurrentVideocard", args.component);
      } else if (args.category === "Оперативная память") {
        this.$store.dispatch("setCurrentMemory", args.component);
      } else if (args.category === "Накопитель данных") {
        this.$store.dispatch("setCurrentDataDrive", args.component);
      }
    },
    dropItem(category) {
      console.log("recieved drop");

      if (category === "Материнская плата") {
        this.$store.dispatch("dropCurrentMotherboard");
      } else if (category === "Процессор") {
        this.$store.dispatch("dropCurrentCPU");
      } else if (category === "Видеокарта") {
        this.$store.dispatch("dropCurrentVideocard");
      } else if (category === "Оперативная память") {
        this.$store.dispatch("dropCurrentMemory");
      } else if (category === "Накопитель данных") {
        this.$store.dispatch("dropCurrentDataDrive");
      }
      console.log(this.$store.getters.currentMotherboard);
    },
    checkCategory(category) {
      if (
        category === "Материнская плата" &&
        this.$store.getters.currentMotherboard
      ) {
        return false;
      } else if (category === "Процессор" && this.$store.getters.currentCPU) {
        return false;
      } else if (
        category === "Видеокарта" &&
        this.$store.getters.currentVideocard
      ) {
        return false;
      } else if (
        category === "Оперативная память" &&
        this.$store.getters.currentMemory
      ) {
        return false;
      } else if (
        category === "Накопитель данных" &&
        this.$store.getters.currentDataDrive
      ) {
        return false;
      } else {
        return true;
      }
    },
    showElement(category) {
      if (category === "Материнская плата") {
        return this.$store.getters.currentMotherboard;
      } else if (category === "Процессор" && this.$store.getters.currentCPU) {
        return this.$store.getters.currentCPU;
      } else if (
        category === "Видеокарта" &&
        this.$store.getters.currentVideocard
      ) {
        return this.$store.getters.currentVideocard;
      } else if (
        category === "Оперативная память" &&
        this.$store.getters.currentMemory
      ) {
        return this.$store.getters.currentMemory;
      } else if (
        category === "Накопитель данных" &&
        this.$store.getters.currentDataDrive
      ) {
        return this.$store.getters.currentDataDrive;
      } else return {};
    },
  },
};
</script>

<style>
.config-main-container {
  background-color: orange;
  grid-row: content-row / span 1;
  grid-column: main-column / span 2;
  display: flex;
  flex-basis: 0;
  height: 100%;
  align-items: center;
  justify-content: center;
}
.configuration-container {
  background-color: rgb(255, 255, 255);
  width: 100%;
  height: 80%;
  max-height: 80%;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-wrap: wrap;
}
</style>
