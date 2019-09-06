import "../assets/app.sass";

import Vue from "vue";

import WebToken from "../bower_components/sugar-data/lib/webtoken.js";

import { HOST } from "./settings.js";
import { router } from "./router/router.js";
import { store } from "./store/store.js";
import "./filters/filters.js";

import App from "./App.vue";

async function main() {

  const app = new Vue({
    router,
    store,
    render: h => h(App)
  }).$mount("#app");

  function forceUpdateAll(element) {
    for(let child of element.$children) {
      forceUpdateAll(child);
    }
    element.$forceUpdate();
  }

  function seconds(seconds) {
    return seconds * 1000;
  }

  setInterval(async function() {
    if(WebToken.authenticated) {
      await WebToken.refresh(`${HOST}/v1/authentication`);
      forceUpdateAll(app);
    }
  }, seconds(240));

  WebToken.expired = function() {
    store.commit("addMessage", {
      class: "error centered",
      content: "Your session has expired."
    });
    router.push({ name: "welcome" });
    forceUpdateAll(app);
  };

  router.push({ name: "welcome" });
}

main();
