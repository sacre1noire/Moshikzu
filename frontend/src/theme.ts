import { createTheme } from '@mantine/core'

const theme = createTheme({
    colors: {
        brand: [
            '#f3f8eb',
            '#e7ece0',
            '#cfd7c3',
            '#b5c0a4',
            '#9fac89',
            '#91a078',
            '#87986a',
            '#77865c',
            '#68784f',
            '#586840',
        ],
    },

    primaryColor: 'brand',

    defaultRadius: 'md',

    fontFamily: 'Nunito, sans-serif',
})

export default theme