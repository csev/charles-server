<template>
  <h3 contenteditable='true' @input='update'></h3>
</template>

<script>
  export default {
    props: {
      value: {
        type: String,
        required: true
      }
    },
    watch: {
      value: function(value) {
        this.$el.innerText = value;
      }
    },
    mounted: function() {
      this.$el.innerText = this.value;
    },
    methods: {
      update: function() {
        this.$emit('input', this.$el.innerText)
      }
    }
  }
</script>
