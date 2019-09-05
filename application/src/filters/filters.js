import Vue from "vue";

Vue.filter("limit", function(value, limit) {
  if(value.length <= limit) {
    return value;
  }
  return value.substring(0, limit) + "...";
});

Vue.filter("date", function(value) {
  let date = new Date(value);
  return date.toDateString();
});
