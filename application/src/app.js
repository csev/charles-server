import '../assets/app.sass';

import Vue from 'vue';
import VueRouter from 'vue-router';

import App from './App.vue';

import About from './views/About.vue';
import Blog from './views/Blog.vue';
import Post from './views/Post.vue';
import Login from './views/Login.vue';
import Logout from './views/Logout.vue';

import User from './views/user/User.vue';
import Profile from './views/user/Profile.vue';
import Posts from './views/user/Posts.vue';
import EditPost from './views/user/EditPost.vue';
import NewPost from './views/user/NewPost.vue';


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
  })

  Vue.use(VueRouter);

  const routes = [
    { path: '/', name: 'default', component: About },
    { path: '/about', name: 'about', component: About },
    { path: '/blog', name: 'blog', component: Blog },
    { path: '/blog/:id', component: Post },
    { path: '/login', name: 'login', component: Login },
    { path: '/logout', name: 'logout', component: Logout },
    { path: '/user/:userId', component: User, children: [
      { path: 'profile', name: 'user-profile', component: Profile },
      { path: 'posts', name: 'user-posts', component: Posts },
      { path: 'edit-post/:postId', name: 'user-edit-post', component: EditPost },
      { path: 'new-post', name: 'user-new-post', component: NewPost }
    ]},
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
