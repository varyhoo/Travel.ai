import type { Config } from 'tailwindcss'

const config: Config = {
  content: [
    './src/pages/**/*.{js,ts,jsx,tsx,mdx}',
    './src/components/**/*.{js,ts,jsx,tsx,mdx}',
    './src/app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend:{
      colors: {
        hotpink: '#fff1da',
        green: '#5dae1d',
        orange: '#e79310',
        blue: '#181e4b',
        litepurple: '#5e6282',
        litegrey: '#686d77',
        grey: '#DFD7F9',
        litedark: '#212832',
        offwhite: '#F5F5F5',
		customPurple: '#6B21A8',
        customPink: '#EC4899',
        customLightPink: '#F9A8D4',
        customOrange: '#F97316',
        customBrown: '#78350F'
       }
    },
  },
  plugins: [],
}
export default config
