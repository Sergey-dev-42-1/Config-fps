<template>
  <div class="category-card">
    <div class="category-picture"></div>
    <div class="category-title">Motherboard</div>
  </div>
</template>

<script>
export default {
  components: {},
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
