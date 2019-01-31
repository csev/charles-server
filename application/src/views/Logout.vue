<template>
  <div>
    <div v-if='token.length'>
      <h2>Log Out</h2>
      <div v-on:click='logout' class='ui secondary button'>Log Out</div>
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
