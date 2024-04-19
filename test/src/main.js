import Vue from "vue";
//import App from "./App.vue";
import Result from "./Result.vue";
import "bootstrap/dist/css/bootstrap.css";
import "bootstrap/dist/js/bootstrap.js";
Vue.config.productionTip = false;

new Vue({
  render: (h) => h(Result),
}).$mount("#app");
