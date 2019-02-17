<template>
  <p>
    <router-link to='/about'>About</router-link>
    <router-link to='/blog'>Blog</router-link>
    <router-link v-if='token' class='right' :to='{ path: `/user/${payload.data.id}/profile` }'>Profile</router-link>
    <router-link v-if='token' class='right' to='/logout'>Logout</router-link>
    <router-link v-else class='right' to='/login'>Login</router-link>
  </p>
</template>

<script>
  import WebToken from '../../bower_components/sugar-data/lib/webtoken.js';

  export default {
    data: function() {
      return WebToken.authentication;
    }
  };
</script>

<style lang='sass' scoped>
  a
    margin: 0 .5em 0 .5em

  .right
    float: right
</style>
