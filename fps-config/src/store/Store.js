import { createStore } from "vuex";

const state = {
  motherboard: null,
  videocard: true,
  cpu: true,
  data_drive: true,
  completed: false,
};
const getters = {
  currentMotherboard: (state) => {
    return state.motherboard;
  },
  currentVideocard: (state) => {
    return state.videocard;
  },
  currentCPU: (state) => {
    return state.cpu;
  },
  currentDataDrive: (state) => {
    return state.data_drive;
  },
  status: (state) => {
    return state.completed;
  },
};
const mutations = {
  setCurrentMotherboard: (state, payload) => {
    state.motherboard = payload;
  },
  setCurrentVideocard: (state, payload) => {
    state.videocard = payload;
  },
  setCurrentCPU: (state, payload) => {
    state.cpu = payload;
  },
  setCurrentDataDrive: (state, payload) => {
    state.data_drive = payload;
  },
  toggleCompleted: (state) => {
    state.completed = !state.completed;
  },
};
const actions = {
  //context == state, payload - полученное значение
  async setCurrentMotherboard(context, payload) {
    await context.commit("setCurrentMotherboard", payload);
    await context.dispatch("checkCompletion");
  },
  async setCurrentVideocard(context, payload) {
    await context.commit("setCurrentVideocard", payload);
    await context.dispatch("checkCompletion");
  },
  async setCurrentCPU(context, payload) {
    await context.commit("setCurrentCPU", payload);
    await context.dispatch("checkCompletion");
  },
  async setCurrentDataDrive(context, payload) {
    await context.commit("setCurrentDataDrive", payload);
    await context.dispatch("checkCompletion");
  },
  async checkCompletion(context) {
    if (
      context.getters.currentMotherboard &&
      context.getters.currentCPU &&
      context.getters.currentDataDrive &&
      context.getters.currentVideocard
    ) {
      if (!context.getters.status) {
        await context.commit("toggleCompleted");
      }
    } else {
      if (context.getters.status) {
        await context.commit("toggleCompleted");
      }
    }
  },
};
export default createStore({
  state,
  mutations,
  actions,
  getters,
});
