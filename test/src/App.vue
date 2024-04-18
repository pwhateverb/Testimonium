<template>
  <div id="app">
    <!-- Background image -->
    <div
      id="background"
      class="p-5 text-center bg-image"
      :style="{
        backgroundImage: `url(${backgroundImage})`,
      }"
    >
      <div class="mask" style="background-color: rgba(0, 0, 0, 0.6)">
        <div class="d-flex justify-content-center align-items-center h-100">
          <div class="text-white">
            <h1 class="mb-3">Heading</h1>
            <h4 class="mb-3">Subheading</h4>
            <a
              data-mdb-ripple-init
              class="btn btn-outline-light btn-lg"
              href="#!"
              role="button"
              >Call to action</a
            >
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "App",
  data() {
    return {
      backgroundImage: require("@/assets/t.png"),
    };
  },
};
</script>

<style>
#background {
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center;
  height: 400px;
  width: 100%;
}
</style>
