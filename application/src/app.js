import '../assets/app.sass';

import Vue from 'vue';
import VueRouter from 'vue-router';

import App from './App.vue';

import Login from './views/Login.vue';
import Logout from './views/Logout.vue';
import Profile from './views/Profile.vue';
import About from './views/About.vue';


async function main() {

  Vue.use(VueRouter);

  const routes = [
    { path: '/about', name: 'about', component: About },
    { path: '/login', name: 'login', component: Login },
    { path: '/logout', name: 'logout', component: Logout },
    { path: '/profile', name: 'profile', component: Profile }
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
