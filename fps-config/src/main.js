import store from "./store/Store";
import { createApp } from "vue";
import App from "./App.vue";
const app = createApp(App);
app.use(store);
app.mount("#app");
