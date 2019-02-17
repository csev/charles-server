<template>
  <div class='ui centered grid'>
    <div>
      <h2>Log In</h2>
      <p>Continue below to log in.</p>
    </div>
    <div v-if='errors.length' class='row'>
      <div class='ui negative message'>
        <div class='header'>Login Failure</div>
        <p>{{ errors.length ? errors[0].detail : '' }}</p>
      </div>
    </div>
    <div class='row'>
      <div class='ui left icon input'>
        <input v-on:keyup.13='login'
               v-model='username'
               type='text'
               placeholder='Username'>
        <i class='user icon'></i>
      </div>
    </div>
    <div class='row'>
      <div class='ui left icon input'>
        <input v-on:keyup.13='login'
               v-model='password'
               type='password'
               placeholder='Password'>
        <i class='lock icon'></i>
      </div>
    </div>
    <div class='row'>
      <div v-on:click='login' class='ui violet button'>Submit</div>
    </div>
  </div>
</template>

<script>
  import WebToken from '../../bower_components/sugar-data/lib/webtoken.js';

  WebToken.url = 'http://localhost:8080/v1/authentication';

  export default {
    data: function() {
      return {
        username: '',
        password: '',
        errors: [ ]
      };
    },
    methods: {
      login: async function() {
        WebToken.attributes = {
          username: this.username,
          password: this.password
        };

        await WebToken.authenticate();

        if(WebToken.authentication.errors.length) {
          this.errors = WebToken.authentication.errors;
        } else {
          this.errors = [ ];
          this.$router.push(`/user/${WebToken.authentication.payload.data.id}/profile`);
        }
      }
    }
  };
</script>
