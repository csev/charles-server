let DEVELOPMENT = true;

export let HOST;

if(DEVELOPMENT) {
  HOST = 'http://localhost:8000';
} else {
  HOST = 'http://production.host';
}
