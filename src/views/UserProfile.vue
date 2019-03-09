<template>
  <v-container
    fill-height
    fluid
    grid-list-xl>
    <v-layout
      justify-center
      wrap
    >
      <!-- <v-flex
        xs12
        md8
      >
        <material-card
          color="green"
          title="Edit Profile"
          text="Complete your profile"
        >
          <v-form>
            <v-container py-0>
              <v-layout wrap>
                <v-flex
                  xs12
                  md4
                >
                  <v-text-field
                    label="Company (disabled)"
                    disabled/>
                </v-flex>
                <v-flex
                  xs12
                  md4
                >
                  <v-text-field
                    class="purple-input"
                    label="User Name"
                  />
                </v-flex>
                <v-flex
                  xs12
                  md4
                >
                  <v-text-field
                    label="Email Address"
                    class="purple-input"/>
                </v-flex>
                <v-flex
                  xs12
                  md6
                >
                  <v-text-field
                    label="First Name"
                    class="purple-input"/>
                </v-flex>
                <v-flex
                  xs12
                  md6
                >
                  <v-text-field
                    label="Last Name"
                    class="purple-input"/>
                </v-flex>
                <v-flex
                  xs12
                  md12
                >
                  <v-text-field
                    label="Adress"
                    class="purple-input"/>
                </v-flex>
                <v-flex
                  xs12
                  md4>
                  <v-text-field
                    label="City"
                    class="purple-input"/>
                </v-flex>
                <v-flex
                  xs12
                  md4>
                  <v-text-field
                    label="Country"
                    class="purple-input"/>
                </v-flex>
                <v-flex
                  xs12
                  md4>
                  <v-text-field
                    class="purple-input"
                    label="Postal Code"
                    type="number"/>
                </v-flex>
                <v-flex xs12>
                  <v-textarea
                    class="purple-input"
                    label="About Me"
                    value="Lorem ipsum dolor sit amet, consectetur adipiscing elit."
                  />
                </v-flex>
                <v-flex
                  xs12
                  text-xs-right
                >
                  <v-btn
                    class="mx-0 font-weight-light"
                    color="success"
                  >
                    Update Profile
                  </v-btn>
                </v-flex>
              </v-layout>
            </v-container>
          </v-form>
        </material-card>
      </v-flex> -->
      <v-flex
        xs12
        md4
      >
        <material-card class="v-card-profile">
          <v-avatar
            slot="offset"
            class="mx-auto d-block"
            size="130"
          >
            <img
              src="./../../public/img/jabalpur.jpg"
            >
          </v-avatar>
          <v-card-text class="text-xs-center">
            <h6 class="category text-gray font-weight-thin mb-3">Smart City</h6>
            <h4 class="card-title font-weight-light">Jablapur</h4>
            <p class="card-description font-weight-light">
              Jabalpur (Hindi: जबलपुर; formerly Jubbulpore) is a tier 2 city in the state of Madhya Pradesh,
              India. According to the 2011 census, it is the third-largest urban agglomeration in Madhya Pradesh
              and the country’s 37th-largest urban agglomeration. It is 2nd largest metropolis of Central India after
              Raipur which is followed by Jabalpur, Bhopal, Bilaspur, Indore and Durg-Bhilai.
            </p>
            <v-btn
              color="success"
              round
              class="font-weight-light"
            ><a href="http://jscljabalpur.org/jabalpur/" 
              target="_blank"
              v-bind:style="{color: 'white', textTransform: 'uppercase', fontWeight: 400}">
              Read More</a></v-btn>
          </v-card-text>
        </material-card>
      </v-flex>
      <v-flex
        xs12
        md4
      >
        <material-card class="v-card-profile">
          <v-avatar
            slot="offset"
            class="mx-auto d-block"
            size="130"
          >
            <img
              src="./../../public/img/chandigarh.jpeg"
            >
          </v-avatar>
          <v-card-text class="text-xs-center">
            <h6 class="category text-gray font-weight-thin mb-3">Smart City</h6>
            <h4 class="card-title font-weight-light">Chandigarh</h4>
            <p class="card-description font-weight-light">
            Chandigarh, the dream city of India's first Prime Minister, Sh. Jawahar Lal Nehru, 
            was planned by the famous French architect Le Corbusier. Picturesquely located at the 
            foothills of Shivaliks, it is known as one of the best experiments in urban planning and 
            modern architecture in the twentieth century in India.
            </p>
            <v-btn
              color="success"
              round
              class="font-weight-light"
            >
            <a href="http://chandigarh.gov.in/knowchd_general.htm" 
              target="_blank"
              v-bind:style="{color: 'white', textTransform: 'uppercase', fontWeight: 400}">
              Read More</a></v-btn>
          </v-card-text>
        </material-card>
      </v-flex>
      <v-flex
        xs12
        md4
      >
        <material-card class="v-card-profile">
          <v-avatar
            slot="offset"
            class="mx-auto d-block"
            size="130"
          >
            <img
              src="./../../public/img/indor.jpg"
            >
          </v-avatar>
          <v-card-text class="text-xs-center">
            <h6 class="category text-gray font-weight-thin mb-3">Smart City</h6>
            <h4 class="card-title font-weight-light">Indore</h4>
            <p class="card-description font-weight-light">
              Indore is located in the western region of Madhya Pradesh (approx.76o E, 23o N),
              on the southern edge of the Malwa plateau, on the Saraswati and Khan rivers,
              which are tributaries of the Shipra River. Indore has an average elevation of 553 meter above
              mean sea level. It is located on an elevated plain, with the Vindhyas range to the south. 
              Two main rivers are Chambal at the west (which originates from Vindhya range south of Mhow) 
              and Kshipra, a tributary of Chambal at the east. Other small rivers include Gambhir and Khan, 
              two tributaries of Kshipra.
            </p>
            <v-btn
              color="success"
              round
              class="font-weight-light"
              ><a href="https://www.smartcityindore.org/introduction/" 
              target="_blank"
              v-bind:style="{color: 'white', textTransform: 'uppercase', fontWeight: 400}">
              Read More</a></v-btn>
          </v-card-text>
        </material-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
export default {
  //
}
</script>
