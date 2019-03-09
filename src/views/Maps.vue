<template>
  <div>
    <div class="mapouter">
      <div class="gmap_canvas" id="gmap_canvas">
        <!-- <iframe
          id="gmap_canvas"
          width="100%"
          height="100%"
          src="https://maps.google.com/maps?q=google&t=&z=13&ie=UTF8&iwloc=&output=embed"
          frameborder="0"
          scrolling="no"
          marginheight="0"
          marginwidth="0"
        /> -->
      </div>
    </div>
  </div>
</template>

<style>
.mapouter {
  text-align:right;
  height:100%;
  width:100%;
  position: absolute;
}
.gmap_canvas {
  overflow:hidden;
  background:none!important;
  height:100%;
  width:100%;
}
</style>

<script>
export default {
mounted() {
        var citymap = {
        indore: {
          center: {lat: 22.7239117, lng: 75.7237604},
          population: 2000000
        },
        jabalpur: {
          center: {lat: 23.1756796, lng: 79.8987116},
          population: 1300000
        },
        chandigarh: {
          center: {lat: 30.73, lng: 76.78},
          population: 1100000
        }
      };
        var map = new google.maps.Map(document.getElementById('gmap_canvas'), {
          zoom: 5,
          center: {lat: 22.7239117, lng: 75.7237604},
          mapTypeId: 'terrain'
        });

        for (var city in citymap) {
          // Add the circle for this city to the map.
          var cityCircle = new google.maps.Circle({
            strokeColor: '#FF0000',
            strokeOpacity: 0.8,
            strokeWeight: 2,
            fillColor: '#FF0000',
            fillOpacity: 0.35,
            map: map,
            center: citymap[city].center,
            radius: Math.sqrt(citymap[city].population) * 100
          });
        }
        
      }
}
</script>

