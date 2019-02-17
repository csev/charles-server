<template>
  <div>
    <div class='ui container'>
      <title-editable v-model='title'></title-editable>
      <div class='ui divider'></div>
      <paragraph-editable v-model='content'></paragraph-editable>
    </div>
    <div class='ui centered grid'>
      <div v-if='errors.length' class='row'>
        <div class='ui negative message'>
          <div class='header'>Post Failure</div>
          <p v-for='error in errors'>{{ error.detail }}</p>
        </div>
      </div>
      <div class='row'>
        <div v-on:click='submit' class='ui violet button'>Post</div>
      </div>
    </div>
  </div>
</template>

<script>
  import WebToken from '../../../bower_components/sugar-data/lib/webtoken.js';
  import { Model } from '../../../bower_components/sugar-data/lib/model.js';

  import TitleEditable from '../../components/TitleEditable.vue';
  import ParagraphEditable from '../../components/ParagraphEditable.vue';

  export default {
    components: {
      TitleEditable,
      ParagraphEditable
    },
    data: function() {
      return {
        title: 'Title',
        content: 'Content',
        errors: [ ]
      };
    },
    methods: {
      submit: async function() {
        if(!WebToken.authentication.token) {
          this.errors = [ { detail: 'Not logged in.' } ];
          return null;
        }

        let payload = WebToken.authentication.payload;

        let post = new Model({
          host: 'http://localhost:8080',
          uri: 'v1',
          type: 'posts',
          attributes: {
            owner: payload.data.id,
            title: this.title,
            content: this.content,
            created: Date.now()
          }
        });

        await post.save();

        console.log(post.attributes.errors);

      }
    }
  }
</script>
