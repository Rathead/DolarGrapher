<template>
  <header>
    <div class="text-box">
      <h1>📈  USD price in CLP</h1>
      <p class="mt-3">A currency timeline made with chart.js</p>
    </div>
    <div class="graph">
      <UsdGraph :entries="resp" />
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
      let response = await $axios.$get("/usd_prices/");

      return { resp: response };
    } catch (e) {
      return { resp: [] };
    }
  },
/*  data() {
    return { lineData: [] };
  }
*/
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
.graph {
  position: absolute;
  padding: 2vh;
  top: 25%;
  left: 10%;
  background: rgba(255, 255, 255, 0.7);
  width: 70vh;
  height: 35vh;
}
</style>
