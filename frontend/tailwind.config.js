module.exports = {
  darkMode: 'class',
  presets: [require('frappe-ui/src/utils/tailwind.config')],
  content: [
    './index.html',
    './src/**/*.{vue,js,ts,jsx,tsx}',
    './node_modules/frappe-ui/src/components/**/*.{vue,js,ts,jsx,tsx}',
  ],
  theme: {
    extend: {
      colors: {
        light: {
          background: '#FFFFFF',
          text: '#000000',
          navBackground: '#FFFFFF',
          navText: '#000000',
          link: '#000000',
          buttonBackground: '#000000',
          buttonText: '#FFFFFF',
          cardBackground: '#EEEEEE',
          hoverButtonBackground:"#DDE6ED",
          hoverButtonText:"#0B0F1F"
        },
        dark: {
          background: '#000000',
          text: '#FFFFFF',
          navBackground: '#111111',
          navText: '#FFFFFF',
          link: '#FFFFFF',
          buttonBackground: '#FFFFFF',
          buttonText: '#000000',
          cardBackground: '#222222',
          hoverButtonBackground:"#080707",
          hoverButtonText:"#f7f7f7"
        },
      },
    },
  },
  plugins: [],
}