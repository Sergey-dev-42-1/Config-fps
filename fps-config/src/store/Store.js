import { createStore } from "vuex";

const state = {
  motherboard: {
    name: "Asrock B460",
    socket: "LGA 1200",
    maximumMemoryFrequency: "2933",
    TypeOfSupportedMemory: "DDR4",
    AvailabilityOfM2: true,
  },
};
const getters = {
  currentMotherboard: (state) => {
    return state.motherboard;
  },
};
const mutations = {
  setCurrentMotherboard: (state, payload) => {
    state.motherboard = payload;
  },
};
const actions = {
  //context == state, payload - полученное значение
  setCurrentMotherboard(context, payload) {
    context.commit("setCurrentMotherboard", payload);
  },
};
export default createStore({
  state,
  mutations,
  actions,
  getters,
});
