<template>
  <div class="modal-backdrop">
    <div class="modal">
      <header class="modal-header">
        Выберите нужный компонент из списка
        <span @click="close" class="material-icons btn-close">close</span>
      </header>
      <section class="modal-body">
        <list-item
          @click="chooseItem(item)"
          class="list-item"
          v-for="(item, index) in items"
          :key="index"
          :component="item"
        ></list-item>
      </section>
    </div>
  </div>
</template>

<script>
import ListItem from "./ListItem.vue";
export default {
  data() {
    return {
      items: [
        {
          name: "Asrock B490",
          socket: "LGA 1233",
          maximumMemoryFrequency: "4933",
          TypeOfSupportedMemory: "DDR8",
          AvailabilityOfM2: true,
        },
        {
          name: "Asrock B460",
          socket: "LGA 1200",
          maximumMemoryFrequency: "2933",
          TypeOfSupportedMemory: "DDR4",
          AvailabilityOfM2: true,
        },
        {
          name: "Asrock B460",
          socket: "LGA 1200",
          maximumMemoryFrequency: "2933",
          TypeOfSupportedMemory: "DDR4",
          AvailabilityOfM2: true,
        },
      ],
    };
  },
  name: "modal",
  components: {
    ListItem,
  },
  props: {
    category: String,
  },
  methods: {
    close() {
      this.$emit("close");
    },
    chooseItem(component) {
      var category = this.category;
      this.$emit("chooseItem", { component, category });
      this.$emit("close");
    },
  },
  emits: ["close", "chooseItem"],
  //Запросить список элементов на mounted
};
</script>

<style scoped>
.modal-backdrop {
  font-family: sans-serif;
  position: fixed;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  background-color: rgba(0, 0, 0, 0.3);
  display: flex;
  justify-content: center;
  align-items: center;
}

.modal {
  width: 60%;
  height: 60%;
  background: #ffffff;
  box-shadow: 2px 2px 20px 1px;
  overflow-x: auto;
  display: flex;
  flex-direction: column;
}

.modal-header {
  padding: 15px;
  display: flex;
}

.modal-header {
  justify-content: space-between;
}

.modal-body {
  position: relative;
  padding: 20px 10px;
  border: 0px;
  overflow: auto;
}

.btn-close {
  border: none;
  font-size: 20px;
  cursor: pointer;
  font-weight: bold;
  color: #000000;
  background: transparent;
}

.list-item {
  background-color: rgb(187, 187, 187);
  width: 100%;
  height: 300px;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
