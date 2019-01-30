import Vue from 'vue';
import VueRouter from 'vue-router';

import App from './App.vue';

import FooView from './views/FooView.vue';
import BarView from './views/BarView.vue';

import '../assets/app.sass';


async function main() {

  Vue.use(VueRouter);

  const routes = [
    { path: '/foo', component: FooView },
    { path: '/bar', component: BarView }
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
