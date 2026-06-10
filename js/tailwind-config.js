tailwind.config = {
  theme: {
    extend: {
      colors: {
        ocean: {
          50:  '#eef2ff',
          100: '#e0e7ff',
          200: '#c7d2fe',
          300: '#a5b4fc',
          400: '#818cf8',
          500: '#6366f1',
          600: '#4f46e5',
          700: '#4338ca',
          800: '#3730a3',
          900: '#312e81',
        },
        terracotta: {
          400: '#fb923c',
          500: '#f97316',
          600: '#ea580c',
        },
        sand: {
          50:  '#faf8f5',
          100: '#f5f0e8',
          200: '#ebe3d5',
        },
        gt: {
          50:  '#ecfdf5',
          100: '#d1fae5',
          200: '#a7f3d0',
          300: '#6ee7b7',
          400: '#34d399',
          500: '#10b981',
          600: '#059669',
          700: '#047857',
          800: '#065f46',
          900: '#064e3b',
        }
      },
      fontFamily: {
        display: ['Outfit', 'system-ui', 'sans-serif'],
        body:    ['Source Sans 3', 'system-ui', 'sans-serif'],
      },
    }
  }
};
