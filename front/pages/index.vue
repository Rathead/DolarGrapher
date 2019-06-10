<template>
  <header>
    <div class="text-box">
      <h1>📈  USD price in CLP</h1>
      <p class="mt-3">A currency timeline made with C3</p>
    </div>
    <div class="graph">
      <UsdGraph :entries="data"/>
    </div>
  </header>
</template>


<script>
import UsdGraph from '@/components/UsdGraph';

export default {
  head() {
    return {
      title: "Home page"
    };
  },
  components: {
    UsdGraph
  },
  async asyncData( { $axios, params } ) {
    try {
      let data = await $axios.$get("/usd_prices/");
      return { data };
    } catch (e) {
      return { data: [] };
    }
  },
  data() {
    return {
      data: []
    };
  }
};
</script>

<style>
header {
  min-height: 100vh;
  background-position: center;
  background-color: #2F4F4F;
  background-size: cover;
  position: relative;
}
.text-box {
  position: absolute;
  top: 15%;
  left: 15%;
  transform: translateY(-50%);
  color: #fff;
}
.text-box h1 {
  font-family: ligther;
  font-size: 5rem;
}
.text-box p {
  font-size: 2rem;
  font-weight: lighter;
}
UsdGraph {
  position: absolute;
}
</style>
