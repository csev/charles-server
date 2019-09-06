<template>
  <div class="ui container">
    <messages />
    <router-view></router-view>
  </div>
</template>

<script>
import WebToken from "../bower_components/sugar-data/lib/webtoken.js";
import Messages from "./components/Messages.vue";

export default {
  components: {
    Messages
  }
}
</script>
