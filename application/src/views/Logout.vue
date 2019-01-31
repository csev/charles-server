<template>
  <div class='ui centered grid'>
    <div v-if='token.length'>
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
      return WebToken.data;
    },
    methods: {
      logout: function() {
        WebToken.data.token = '';
      }
    }
  }
</script>
