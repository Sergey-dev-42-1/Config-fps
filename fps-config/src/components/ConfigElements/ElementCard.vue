<template>
  <div @click="showList" class="element-card">
    <div @click.stop="dropItem" class="material-icons btn-close">close</div>
    <div class="element-picture"></div>
    <div class="element-title">{{ item.name }}</div>

    <teleport to="body">
      <transition name="fade">
        <list-items-modal
          @close="showList"
          @chooseItem="chooseItem"
          v-if="this.ListShown"
          :category="this.category"
        ></list-items-modal>
      </transition>
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
  props: { item: Object, category: String },
  components: { ListItemsModal },
  methods: {
    showList() {
      console.log(this.ListShown);
      this.ListShown = !this.ListShown;
    },
    dropItem() {
      this.$emit("dropItem", this.category);
    },
    chooseItem(args) {
      this.$emit("chooseItem", args);
    },
  },
  emits: ["dropItem", "chooseItem"],
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
}
.element-picture {
  background-color: white;
  border-radius: 10px;
  margin-top: 20px;
  width: 40%;
  height: 60%;
  align-self: center;
  justify-self: center;
}
.element-title {
  color: black;
  align-self: center;
  justify-self: flex-end;
  margin-top: 20px;
}
.btn-close {
  border: none;
  font-size: 20px;
  cursor: pointer;
  font-weight: bold;
  color: #000000;
  margin: 10px 10px 0 0;
  background: transparent;
  justify-self: flex-start;
  align-self: flex-end;
}
</style>
