<template>
  <div class="graphContainer">
    {{entries}} 
  </div>
</template>

<script>
//import c3 from 'c3'
//import d3 from 'd3'

export default {
  props: ["entries"],
  watch: {
    entries: function(newVal) {
      console.log("AAAA");
    }
  }
}
</script>

<style scoped>
.graphContainer {
  position: relative;
  background: rgba(255, 255, 255, 0.7);
  height: 50vh;
  width: 70vh;
  border-radius: 15px;
}
</style>
