<template>
  <div>
    <div class='ui centered grid'>
      <h2 class='row'>New Post</h2>
    </div>
    <div class='ui container'>
      <title-editable v-model='title'></title-editable>
      <div class='ui divider'></div>
      <paragraph-editable v-model='content'></paragraph-editable>
    </div>
    <div class='ui centered grid'>
      <div v-if='errors.length' class='row'>
        <div class='ui negative message'>
          <div class='header'>Post Failure</div>
          <p>{{ errors.length ? errors[0].detail : '' }}</p>
        </div>
      </div>
      <div class='row'>
        <div v-on:click='submit' class='ui violet button'>Submit</div>
      </div>
    </div>
  </div>
</template>

<script>
  import TitleEditable from '../components/TitleEditable.vue';
  import ParagraphEditable from '../components/ParagraphEditable.vue';

  import WebToken from '../../bower_components/sugar-data/lib/webtoken.js';
  import { Model } from '../../bower_components/sugar-data/lib/model.js';

  export default {
    components: {
      TitleEditable,
      ParagraphEditable
    },
    data: function() {
      return {
        title: '',
        content: '',
        errors: [ ]
      }
    },
    methods: {
      submit: async function() {
        if(!WebToken.authentication.token) {
          this.errors = [ { detail: 'Not logged in.' } ];
          return null;
        }
        let token = jwt_decode(WebToken.data.token);
        let post = new Model({
          host: 'http://localhost:8080',
          uri: 'v1',
          type: 'posts',
          attributes: {
            owner: token.data.id,
            title: this.title,
            content: this.content,
            created: Date.now()
          }
        });
        await post.save();
        console.log(post);
      }
    }
  }
</script>
