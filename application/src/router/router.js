import Vue from "vue";
import VueRouter from "vue-router";

Vue.use(VueRouter);

import Welcome from "../views/Welcome.vue";

export const router = new VueRouter({
  linkActiveClass: "active",
  linkExactActiveClass: "exact",
  routes: [
    { path: "/welcome", name: "welcome", component: Welcome }
  ]
});
