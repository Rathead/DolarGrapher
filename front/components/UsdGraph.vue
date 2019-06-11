<template>
  <div class="graphContainer" >
    <LineChart v-if="showLine" :data="data" :options="options" />
    {{entries}}
  </div>
</template>

<script>

const defOptions = {
  responsive: true,
  maintainAspectRatio: false,
  legend: {
    display: false
  },
  title: {
    display: true,
    text: 'Historical CLP price of USD'
  },
  scales: {
    yAxes: [{
      ticks: {
        beginAtZero: true,
        callback: function(value, index, values) {
          return value + ' CLP';
        }
      }
    }]
  }
};

const defData = {
  labels: [], // Dates
  datasets: [{
    data: [], // Prices
  }]
};

export default {
  props: ["entries"],
/*  data () {
    return {
      showLine: false,
      data: defData,
      options: defOptions
    };
  },
  asyncData () {
    let dat = defData;
    dat.labels = ['A', 'B', 'C'];
    dat.datasets[0].data = [12, 34, 56];

    return { data: dat, options: defOptions, entries};
  },
*/
  data () {
    return {
      showLine: false,
      options: defOptions,
      data: {
        labels: [],
        datasets: [
          {
            data: []
          }
        ]
      }
    }
  },
  async asyncData({ env }) {
    const res = await axios.get("/usd_prices/");
    
    return {
      data: {
        labels: ['A', 'B', 'C'], // res.map(date),
        datasets: [
          {
            data: [12, 34, 45], // res.map(clp_value)
          }
        ]
      },
      showLine: false,
      entries
    };
  },
  mounted () {
    // showLine will only be set to true on the client. This keeps the DOM-tree in sync.
    this.showLine = true;
  }
}
</script>
