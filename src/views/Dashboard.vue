<template>
  <v-container fill-height fluid grid-list-xl>
    <v-layout wrap>
      <v-flex sm6 xs12 md6 lg4>
        <material-stats-card
          color="green"
          icon="mdi-information-outline"
          title="Max Accidents in 2014"
          value="67250"
          sub-icon="mdi-tag"
          sub-text="State - Tamil Nadu"
        />
      </v-flex>
      <v-flex sm6 xs12 md6 lg4>
        <material-stats-card
          color="orange"
          icon="mdi-information-outline"
          title="Max Accidents in 2015"
          value="69059"
          sub-icon="mdi-tag"
          sub-text="State - Tamil Nadu"
        />
      </v-flex>
      <v-flex sm6 xs12 md6 lg4>
        <material-stats-card
          color="red"
          icon="mdi-information-outline"
          title="Max Accidents in 2016"
          value="71431"
          sub-icon="mdi-tag"
          sub-text="State - Tamil Nadu"
        />
      </v-flex>
      <!-- <v-flex sm6 xs12 md6 lg3>
        <material-stats-card
          color="info"
          icon="mdi-information-outline"
          title="Fixed Issues"
          value="75"
          sub-icon="mdi-tag"
          sub-text="State - "
        />
      </v-flex> -->
      <v-flex md12 sm12 lg6>
        <material-chart-card
          :data="dailySalesChart.data"
          :options="dailySalesChart.options"
          color="info"
          type="Line"
        >
          <h4 class="title font-weight-light">Accidents</h4>
          <p class="category d-inline-flex font-weight-light">
            <v-icon color="green" small>mdi-arrow-up</v-icon>
            <span class="green--text">10%</span>&nbsp;
            increase in rate of Accidents in Tamil Nadu
          </p>
        </material-chart-card>
      </v-flex>
      <v-flex md12 sm12 lg6>
        <material-chart-card
          :data="emailsSubscriptionChart.data"
          :options="emailsSubscriptionChart.options"
          :responsive-options="emailsSubscriptionChart.responsiveOptions"
          color="red"
          type="Bar"
        >
          <h4 class="title font-weight-light">Top 5 States with Highest Accident Rates</h4>
        </material-chart-card>
      </v-flex>
      <v-flex md12 lg12>
        <material-card color="orange" title="State Wise Accidental Stats" text>
          <v-data-table :headers="headers" :items="items" hide-actions>
            <template slot="headerCell" slot-scope="{ header }">
              <span class="font-weight-light text-warning text--darken-3" v-text="header.text"/>
            </template>
            <template slot="items" slot-scope="{ index, item }">
              <td>{{ index + 1 }}</td>
              <td>{{ item.name.split("\n")[0].split("   ")[1].trim() }}</td>
              <td class="text-xs-right">{{ item["2014"].split("\n")[0].split("   ")[1].trim() }}</td>
              <td class="text-xs-right">{{ item["2015"].split("\n")[0].split("   ")[1].trim() }}</td>
              <td class="text-xs-right">{{ item["2016"].split("\n")[0].split("   ")[1].trim() }}</td>
            </template>
          </v-data-table>
        </material-card>
      </v-flex>
      
    </v-layout>
  </v-container>
</template>

<script>
const axios = require("axios");
export default {
  data() {
    return {
      dailySalesChart: {
        data: {
          labels: ["2014", "2015", "2016"],
          series: [[67250, 69059, 71431]]
        },
        options: {
          lineSmooth: this.$chartist.Interpolation.cardinal({
            tension: 0
          }),
          low: 40000,
          high: 80000, 
          chartPadding: {
            top: 0,
            right: 0,
            bottom: 0,
            left: 0
          }
        }
      },
      emailsSubscriptionChart: {
        data: {
          labels: [
            "Gujarat",
            "Karnataka",
            "Kerala",
            "MP",
            "Maharashtra"
          ],
          series: [[21859, 43713, 37000, 53472, 61627]]
        },
        options: {
          axisX: {
            showGrid: false
          },
          low: 10000,
          high: 70000,
          chartPadding: {
            top: 0,
            right: 5,
            bottom: 0,
            left: 0
          }
        },
        responsiveOptions: [
          [
            "screen and (max-width: 640px)",
            {
              seriesBarDistance: 5,
              axisX: {
                labelInterpolationFnc: function(value) {
                  return value[0];
                }
              }
            }
          ]
        ]
      },
      headers: [
        {
          sortable: false,
          text: "ID",
          value: "id"
        },
        {
          sortable: false,
          text: "State",
          value: "name"
        },
        {
          sortable: false,
          text: "Accidents in 2014",
          value: "2014",
          align: "right"
        },
        {
          sortable: false,
          text: "Accidents in 2015",
          value: "2015",
          align: "right"
        },
        {
          sortable: false,
          text: "Accidents in 2016",
          value: "2016",
          align: "right"
        },
      ],
      items: [],
      max2014: {
        value: '67250',
        state: 'Tamil Nadu'
      },
      max2015: {
        value: '69059',
        state: 'Tamil Nadu'
      },
      max2016: {
        value: '71431',
        state: 'Tamil Nadu'
      },
      tabs: 0,
      list: {
        0: false,
        1: false,
        2: false
      }
    };
  },
  mounted() {
    this.fetchData();
  },
  methods: {
    complete(index) {
      this.list[index] = !this.list[index];
    },
    fetchData() {
      // Make a request for a user with a given ID
      let vm = this;
      axios
        .get("http://localhost:9000/states")
        .then(function(response) {
          // handle success
          vm.items = response.data;
          vm.max2014 = 
          console.log(response.data);
        })
        .catch(function(error) {
          // handle error
          console.log(error);
        })
        .then(function() {
          // always executed
        });
    }
  }
};
</script>
