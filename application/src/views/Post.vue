<template>
  <div class='ui container'>
    <h2>{{ post.title }}</h2>
    <p>{{ post.content }}</p>
  </div>
</template>

<script>
  import { Model } from '../../bower_components/sugar-data/lib/model.js';

  export default {
    data: function() {
      return {
        post: { },
        errors: [ ]
      };
    },
    created: async function() {
      let model = new Model({
        host: 'http://localhost:8080',
        uri: 'v1',
        type: 'posts',
        id: this.$route.params.id
      });

      await model.load();

      if(model.attributes.errors.length) {
        this.post = { };
        this.errors = model.attributes.errors;
      } else {
        this.post = model.attributes;
        this.errors = [ ];
      }
    }
  }
</script>
