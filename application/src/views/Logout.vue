<template>
  <div class='ui centered grid'>
    <div v-if='token'>
      <h2>Log Out</h2>
      <p>Are you sure you want to log out?</p>
      <div v-on:click='logout' class='ui orange basic button'>Log Out</div>
    </div>
    <div v-else>
      <h2>Logged Out</h2>
    </div>
  </div>
</template>

<script>
  import WebToken from '../../bower_components/sugar-data/lib/webtoken.js';

  export default {
    data: function() {
      return WebToken.authentication;
    },
    methods: {
      logout: function() {
        WebToken.authentication.token = null;
      }
    }
  }
</script>
