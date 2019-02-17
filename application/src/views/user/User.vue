<template>
  <div>
    <div class='ui text menu'>
      <router-link class='item' :to='{ path: `/user/${$route.params.userId}/profile` }'>Profile</router-link>
      <router-link class='item' :to='{ path: `/user/${$route.params.userId}/new-post` }'>New Post</router-link>
      <router-link class='item' :to='{ path: `/user/${$route.params.userId}/posts` }'>Posts</router-link>
    </div>
    <router-view></router-view>
  </div>
</template>
