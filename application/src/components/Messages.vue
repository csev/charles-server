<template>
  <div>
    <div class="close-all"
      v-if="$store.state.messages.length"
      v-on:click="closeAll()">
      Close All <i class="fas fa-window-close"></i>
    </div>
    <div class="message"
      v-bind:class="message.class"
      v-for="message in $store.state.messages">
      {{ message.content }}
      <i class="close fas fa-window-close"
        v-on:click="close(message)">
      </i>
    </div>
    <div v-on:click="addMessage()">Add Message</div>
  </div>
</template>

<script>
  let interval = null;

  export default {
    methods: {
      addMessage() {
        this.$store.commit('addMessage', {
          class: "info centered",
          content: "This is a message.",
          timeout: 5
        })
      },
      closeAll() {
        for(let message of this.$store.state.messages) {
          this.$store.commit('removeMessage', message);
        }
      },
      close(message) {
        this.$store.commit('removeMessage', message);
      }
    },
    mounted() {
      interval = setInterval(() => {
        this.$store.commit('removeExpiredMessages');
      }, 1000)
    },
    destroyed() {
      clearInterval(interval);
    }
  }
</script>

<style lang="sass" scoped>
  @import "../../assets/color.sass"

  div.close-all
    color: gray
    text-align: right
    margin: 0rem 1rem 1rem 1rem

  div.close-all:hover
    cursor: pointer

  div.message
    margin: 0rem 1rem 1rem 1rem
    padding: 0.5rem
    border: 1px solid $purple
    background: $light-purple
    color: white

    &.centered
      text-align: center

    &.success
      background-color: $light-green
      border-color: $green

    &.error
      background-color: $light-red
      border-color: $red

    i
      float: right
      font-weight: 400

    i:hover
      cursor: pointer
</style>
