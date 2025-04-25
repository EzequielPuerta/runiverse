/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
        "./src/**/*.{html,js,svelte,ts}"
    ],
    safelist: [{ pattern: /.*/ }],
    theme: {
        extend: {},
    },
    plugins: [require("daisyui")],
    daisyui: {
        themes: ["garden", "forest"],
        darkTheme: "forest",
    }
}
