<template>
  <div @click="showList" class="category-card">
    <div class="category-picture"></div>
    <div class="category-title">{{ category }}</div>
    <teleport to="body">
      <list-items-modal
        @chooseItem="chooseItem"
        @close="showList"
        v-if="this.ListShown"
        :category="category"
      ></list-items-modal>
    </teleport>
  </div>
</template>

<script>
import ListItemsModal from "./ListItemsModal";
export default {
  data() {
    return {
      ListShown: false,
    };
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
};
</script>

<style>
.category-card {
  color: white;
  background-color: rgb(170, 170, 170);
  width: 300px;
  height: 300px;
  margin: 10px;
  border-radius: 10px;
  display: flex;

  flex-direction: column;
  align-items: center;
  justify-content: center;
}
.category-picture {
  background-color: white;
  border-radius: 10px;
  width: 40%;
  height: 60%;
}
.category-title {
  color: black;
}
</style>
