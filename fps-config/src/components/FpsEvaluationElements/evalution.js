export default {
  evaluate: function(CPU, Videocard, Memory, DataDrive, gameTitle) {
    let CPU_perf =
      0.2 * (CPU.NumberOfCores / 8) + 2 * (CPU.MaximumFrequency / 5000);
    let Videocard_perf =
      3 * (Videocard.ChipFrequency / 1755) +
      3 * (Videocard.TheNumberOfUniversalProcessors / 4352) +
      3.5 * (Videocard.NumberOfTextureUnits / 272) +
      3 * (Videocard.TheNumberOfROPUnits / 88) +
      Videocard.MemoryFrequency / 14000;

    if (Videocard.MemoryType === "GDDR6X") {
      Videocard_perf += 1.2;
    } else {
      Videocard_perf += 1;
    }
    let Memory_perf = Memory.Frequency / 3000 + Memory.Timings / 15;
    if (Memory.Type === "DDR4") {
      Memory_perf += 1.2;
    }
    CPU_perf /= 2;
    Videocard_perf /= 6;
    Memory_perf /= 3;
    let result = CPU_perf + Videocard_perf + Memory_perf;
    if (DataDrive.Type === "SSD" || DataDrive.Type === "M.2") {
      result = (result / 100) * 105;
    }
    result * game_coefficients[gameTitle];
    return Math.ceil(result);
  },
};
var game_coefficients = {
  "AC Odyssey": 21.6,
};
