<template>
  <div @click="showList" class="element-card">
    <div @click="dropItem" class="material-icon">close</div>
    <div class="element-picture"></div>
    <div class="element-title">{{ item.title }}</div>
    <div class="element-characteristics">{{ item.characteristics }}</div>
    <teleport to="body">
      <list-items
        @close="showList"
        v-if="this.ListShown"
        :element="element"
      ></list-items>
    </teleport>
  </div>
</template>

<script>
import ListItems from "./ListItemsModal";
export default {
  data() {
    return {
      ListShown: false,
    };
  },
  props: { item: Object },
  components: { ListItems },
  methods: {
    showList() {
      console.log(this.ListShown);
      this.ListShown = !this.ListShown;
    },
  },
};
</script>

<style>
.element-card {
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
.element-picture {
  background-color: white;
  border-radius: 10px;
  width: 40%;
  height: 60%;
}
.element-title {
  color: black;
}
</style>
