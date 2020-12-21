import { createStore } from "vuex";

const state = {
  motherboard: {
    name: "Asrock B490",
    socket: "LGA 1233",
    maximumMemoryFrequency: "4933",
    TypeOfSupportedMemory: "DDR8",
    AvailabilityOfM2: true,
  },
  videocard: {
    name: "Asrock B490",
    socket: "LGA 1233",
    maximumMemoryFrequency: "4933",
    TypeOfSupportedMemory: "DDR8",
    AvailabilityOfM2: true,
  },
  cpu: {
    name: "Asrock B490",
    socket: "LGA 1233",
    maximumMemoryFrequency: "4933",
    TypeOfSupportedMemory: "DDR8",
    AvailabilityOfM2: true,
  },
  memory: null,
  data_drive: {
    name: "Asrock B490",
    socket: "LGA 1233",
    maximumMemoryFrequency: "4933",
    TypeOfSupportedMemory: "DDR8",
    AvailabilityOfM2: true,
  },
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
  currentMemory: (state) => {
    return state.memory;
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
  setCurrentMemory: (state, payload) => {
    state.memory = payload;
  },
  setCurrentDataDrive: (state, payload) => {
    state.data_drive = payload;
  },
  dropCurrentMotherboard: (state) => {
    console.log("dropped motherboard");
    state.motherboard = null;
  },
  dropCurrentVideocard: (state) => {
    state.videocard = null;
  },
  dropCurrentCPU: (state) => {
    state.cpu = null;
  },
  dropCurrentMemory: (state) => {
    state.memory = null;
  },
  dropCurrentDataDrive: (state) => {
    state.data_drive = null;
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
  async setCurrentMemory(context, payload) {
    await context.commit("setCurrentMemory", payload);
    await context.dispatch("checkCompletion");
  },
  async setCurrentDataDrive(context, payload) {
    await context.commit("setCurrentDataDrive", payload);
    await context.dispatch("checkCompletion");
  },
  async dropCurrentMotherboard(context) {
    console.log("committing drop");
    await context.commit("dropCurrentMotherboard");
    await context.dispatch("checkCompletion");
  },
  async dropCurrentCPU(context) {
    await context.commit("dropCurrentCPU");
    await context.dispatch("checkCompletion");
  },
  async dropCurrentVideocard(context) {
    await context.commit("dropCurrentVideocard");
    await context.dispatch("checkCompletion");
  },
  async dropCurrentMemory(context) {
    await context.commit("dropCurrentMemory");
    await context.dispatch("checkCompletion");
  },
  async dropCurrentDataDrive(context) {
    await context.commit("dropCurrentDataDrive");
    await context.dispatch("checkCompletion");
  },
  async checkCompletion(context) {
    if (
      context.getters.currentMotherboard &&
      context.getters.currentCPU &&
      context.getters.currentMemory &&
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
