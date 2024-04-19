import Vue from "vue";
import Router from "vue-router";
import Home from "./Home.vue";
import Result from "./Result.vue";

Vue.use(Router);

const router = new Router({
  mode: "history",
  routes: [
    {
      path: "/",
      name: "home-page",
      component: Home,
    },
    {
      path: "/result",
      name: "result-page",
      component: Result,
    },
  ],
});

export default router;
