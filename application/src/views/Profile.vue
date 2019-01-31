<template>
  <div class='ui centered grid'>
    <span>{{ username }}</span>
  </div>
</template>

<script>
  import WebToken from '../../bower_components/sugar-data/lib/webtoken.js';

  export default {
    data: function() {
      if(WebToken.data.token.length) {
        let token = jwt_decode(WebToken.data.token);
        console.log(token);
        return token.data.attributes;
      } else {
        return {
          username: ''
        };
      }
    }
  };
</script>
