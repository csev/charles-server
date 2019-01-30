import Vue from 'vue';
import VueRouter from 'vue-router';

import App from './App.vue';
import Test from './components/Test.vue';

import '../assets/app.sass';


async function main() {

  Vue.use(VueRouter);

  const routes = [
    { path: '/foo', component: Test }
  ];

  const router = new VueRouter({
    routes
  });

  const app = new Vue({
    router,
    render: h => h(App)
  }).$mount('#app');

}

main();
