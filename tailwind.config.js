/** @type {import('tailwindcss').Config} */
module.exports = {
  daisyui: {
    themes: [
      {
        LIGHT: {
          primary: "#22d3ee",
          "base-100": "#ffffff",
          success: "#4ade80",
          warning: "#facc15",
          error: "#dc2626",
        },
        DARK: {
          primary: "#22d3ee",
          "base-100": "#2B3441",
          success: "#4ade80",
          warning: "#facc15",
          error: "#dc2626",
        },
      },
    ],
  },
  content: ["./src/**/*.html"],
  theme: {
    extend: {},
  },
  plugins: [require("daisyui")],
};
