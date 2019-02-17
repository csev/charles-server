<template>
  <div>
    <h3>Posts</h3>
    <div v-if='collection' class='ui container'>
      <div v-for='post in collection.items'>
        <span class='ui violet label date'>{{ post.created | date }}</span>
        <router-link :to='{ path: `/user/${$route.params.userId}/edit-post/${post._id}` }'>Post</router-link>
        <h3>{{ post.title }}</h3>
        <p>{{ post.content | limit(500) }}</p>
        <div class='ui divider'></div>
      </div>
    </div>
    <div v-else>
      <div class="ui segment">
        <p></p>
        <div class="ui active dimmer">
          <div class="ui loader"></div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import { Collection } from '../../../bower_components/sugar-data/lib/collection.js';

  export default {
    data: function() {
      return {
        collection: null
      };
    },
    created: async function() {
      let collection = new Collection({
        host: 'http://localhost:8080',
        uri: 'v1',
        type: 'posts'
      });

      await collection.find({
        query: {
          owner: this.$route.params.id
        },
        sort: [ '-created' ]
      });

      this.collection = collection.attributes;
    }
  }
</script>

<style lang='sass' scoped>
  .date
    float: right
</style>
