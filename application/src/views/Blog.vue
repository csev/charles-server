<template>
  <div>
    <div class='ui centered grid'>
      <h2>Blog</h2>
    </div>
    <div class='ui container'>
      <div v-for='post in posts'>
        <span class='ui violet label date'>{{ post.created | date }}</span>
        <router-link :to='{ path: `/blog/${post._id}` }'>Post</router-link>
        <h3>{{ post.title }}</h3>
        <p>{{ post.content | limit(500) }}</p>
        <div class='ui divider'></div>
      </div>
    </div>
  </div>
</template>

<script>
  import { Collection } from '../../bower_components/sugar-data/lib/collection.js';

  export default {
    data: function() {
      return {
        posts: [ ],
        errors: [ ]
      };
    },
    created: async function() {
      let collection = new Collection({
        host: 'http://localhost:8080',
        uri: 'v1',
        type: 'posts',
      });

      await collection.find({ sort: [ '-created' ] });

      if(collection.attributes.errors.length) {
        this.posts = [ ];
        this.errors = collection.attributes.errors;
      } else {
        this.posts = collection.attributes.items;
        this.errors = [ ];
      }
    },
    filters: {
      limit: function(value, limit) {
        if(value.length <= limit) {
          return value;
        }
        return value.substring(0, limit) + '...';
      },
      date: function(value) {
        let date = new Date(value);
        return date.toDateString();
      }
    }
  }
</script>

<style lang='sass' scoped>
  .date
    float: right
</style>
