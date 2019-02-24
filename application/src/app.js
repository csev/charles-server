import '../assets/app.sass';

import Vue from 'vue';
import VueRouter from 'vue-router';

import App from './App.vue';

import Welcome from './views/Welcome.vue';

async function main() {

  Vue.filter('limit', function(value, limit) {
    if(value.length <= limit) {
      return value;
    }
    return value.substring(0, limit) + '...';
  });

  Vue.filter('date', function(value) {
    let date = new Date(value);
    return date.toDateString();
  });

  Vue.use(VueRouter);

  const routes = [
    { path: '/', name: 'default', component: Welcome },
  ];

  const router = new VueRouter({
    routes,
    linkActiveClass: 'active',
    linkExactActiveClass: 'active-exact'
  });

  const app = new Vue({
    router,
    render: h => h(App)
  }).$mount('#app');

}

main();
