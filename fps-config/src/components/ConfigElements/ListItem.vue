<template>
  <div class="item-body">
    <img class="item-pic" />
    <span class="item-title">{{ component.name }}</span>
    <div class="element-characteristics">
      <div v-for="(characteristic, index) in component" :key="index">
        {{ characteristic }}
      </div>
    </div>
  </div>
</template>

<script>
//var images = require.context("../../../public/img/items", false, /\....$/);
export default {
  props: { component: Object },
  computed: {
    itemImgSource: function() {
      return 0;
    },
  },
};
</script>

<style>
.item-body {
  width: 100%;
  height: 100%;
  margin: 10px 0px;
  display: grid;
  gap: 10px 10px;
  grid-template: 1fr 3fr / 2fr 5fr;
}
.item-pic {
  background-color: black;
  align-self: center;
  justify-self: center;
  max-width: 90%;
  max-height: 90%;
  width: 250px;
  height: 270px;

  grid-row: 1 /3;
}
.item-title {
  width: 100%;
  font-size: 2rem;
  align-self: center;
  justify-self: center;
  grid-row: 1 / 2;
  grid-column: 2 / 3;
}
.item-characteristics {
  font-size: 10px;
  width: 100%;
  max-height: 10%;
  align-self: left;
  display: table;
}
</style>
