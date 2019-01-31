import '../assets/app.sass';

import Vue from 'vue';
import VueRouter from 'vue-router';

import App from './App.vue';

import Login from './views/Login.vue';
import Logout from './views/Logout.vue';
import User from './views/User.vue';


async function main() {

  Vue.use(VueRouter);

  const routes = [
    { path: '/login', name: 'login', component: Login },
    { path: '/logout', name: 'logout', component: Logout },
    { path: '/user', name: 'user', component: User }
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
