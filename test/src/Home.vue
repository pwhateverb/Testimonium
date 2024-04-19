<template>
  <div id="app">
    <div id="navbar">
      <span id="home">Home</span>
      <span id="requirements">Requirements</span>
    </div>
    <div id="line"></div>
    <img id="logo" src="./assets/logo.png" />
    <div id="header">
      <h1 class="text-center text-white">Testimonium</h1>
      <p class="text-center sub-header">
        Testimonium is a platform that allows you to create and share your
        testimonies with the world.
      </p>
    </div>
    <button type="button" class="btn btn-outline-light txt_reqs">
      Write<br />Requirements
    </button>
    <div @click="generate()">
      <button type="button" class="btn btn-danger upload_pdf">
        Upload PDF
      </button>
    </div>
    <div
      id="background"
      class="p-5 text-center bg-image"
      :style="{
        backgroundImage: `url(${backgroundImage})`,
      }"
    ></div>
    <div class="jumbotron">
      <h2 class="display-4">Product benefits</h2>
      <p class="lead">
        <br />Testamonium is a platform that allows you to fully automate the
        <br />process of writing detailed test specifcations from your
        requirements.
      </p>
      <hr class="my-4" />
      <p>
        It uses utility classes for typography and spacing to space content out
        within the larger container.
      </p>
    </div>
  </div>
</template>
  
  <script>
import axios from "axios";

export default {
  name: "home-page",
  data() {
    return {
      backgroundImage: require("@/assets/background.png"),
      requirements: "FR1: The user shall be able to view and manage plants",
    };
  },
  methods: {
    generate() {
      const encodedRequirements = encodeURIComponent(this.requirements);
      axios
        .get("http://127.0.0.1:5000?requirements=" + encodedRequirements)
        .then((response) => {
          sessionStorage.setItem("tests", JSON.stringify(response.data));
          console.log("Tests:", process.env.TESTS);
          this.$router.push("/result");
        })
        .catch((error) => {
          console.error("Error making request:", error);
        });
    },
  },
};
</script>
  
  <style>
#navbar {
  position: absolute;
  top: 15px;
  right: 10px;
}

#navbar span {
  margin-right: 20px;
  font-size: 20px;
  color: white;
  cursor: pointer;
}

#background {
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center;
  height: 400px;
  width: 100%;
}

#line {
  position: absolute;
  top: 70px;
  height: 1px;
  background: white;
  width: 100%;
}

#logo {
  position: absolute;
  top: 15px;
  margin-left: 40px;
  width: 240px;
  cursor: pointer;
}

#header {
  position: absolute;
  top: 100px;
  width: 100%;
}

.sub-header {
  color: rgb(234, 234, 234);
}

.txt_reqs {
  position: absolute;
  top: 230px;

  left: 44%;
  transform: translateX(-50%);
}

.upload_pdf {
  height: 60px;
  width: 125px;
  position: absolute;
  top: 230px;
  left: 56%;
  transform: translateX(-50%);
}
</style>
  