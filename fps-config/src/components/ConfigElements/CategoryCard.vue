<template>
  <div @click="showList" class="category-card">
    <img class="category-picture" :src="categoryImagePath" />
    <div class="category-title">{{ category }}</div>
    <teleport to="body">
      <transition name="fade">
        <list-items-modal
          @chooseItem="chooseItem"
          @close="showList"
          v-if="this.ListShown"
          :category="category"
        ></list-items-modal>
      </transition>
    </teleport>
  </div>
</template>

<script>
import ListItemsModal from "./ListItemsModal";
var images = require.context("../../../public/img/categories", false, /\....$/);
export default {
  data() {
    return {
      ListShown: false,
    };
  },
  computed: {
    categoryImagePath: function() {
      try {
        return images("./" + this.category + ".jpg");
      } catch {
        return images("./" + this.category + ".png");
      }
    },
  },
  props: { category: String },
  components: { ListItemsModal },
  methods: {
    showList() {
      console.log(this.ListShown);
      this.ListShown = !this.ListShown;
    },
    //плохая реализация, проброс через несколько компонентов
    chooseItem(args) {
      this.$emit("chooseItem", args);
    },
  },
  emits: ["chooseItem"],
};
</script>

<style>
.category-card {
  color: white;

  width: 300px;
  height: 270px;
  margin: 10px;
  box-shadow: 0 0 10px 5px grey;
  border-radius: 10px;
  display: flex;

  flex-direction: column;
  align-items: center;
  justify-content: center;
  transition: box-shadow 0.5s;
}
.category-card:hover {
  box-shadow: 0 0 0px 5px orange;
}
.category-picture {
  background-color: transparent;
  border-radius: 10px;
  width: 200px;
  max-height: 300px;
  margin-top: auto;
}

.category-title {
  color: black;
  justify-self: flex-end;
  margin-top: auto;
  margin-bottom: 10px;
}
</style>
