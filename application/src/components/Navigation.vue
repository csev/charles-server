<template>
  <p>
    <router-link to='/user'>User</router-link>
    <router-link v-if='token.length' class='right' to='/logout'>Logout</router-link>
    <router-link v-else class='right' to='/login'>Login</router-link>
  </p>
</template>

<script>
  import WebToken from '../../bower_components/sugar-data/lib/webtoken.js';

  export default {
    data: function() {
      return WebToken.data;
    }
  };
</script>

<style lang='sass' scoped>
  a
    margin: 0 .5em 0 .5em

  .right
    float: right
</style>
