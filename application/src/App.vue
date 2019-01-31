<template>
  <div>
    <navigation />
    
    <h1>Sugarush</h1>

    <router-view></router-view>
  </div>
</template>

<script>
import Navigation from './components/Navigation.vue';

import WebToken from '../bower_components/sugar-data/lib/webtoken.js';

export default {
  components: {
    Navigation
  }
}
</script>
