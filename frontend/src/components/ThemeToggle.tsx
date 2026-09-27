import { ActionIcon } from '@mantine/core'
import { useMantineColorScheme } from '@mantine/core'
import { IconMoon, IconSun } from '@tabler/icons-react'

function ThemeToggle() {
    const { colorScheme, toggleColorScheme } = useMantineColorScheme()

    return (
        <ActionIcon
            variant="default"
            size="lg"
            onClick={() => toggleColorScheme()}
            aria-label="Переключить тему"
        >
            {colorScheme === 'dark' ? <IconSun size={18} /> : <IconMoon size={18} />}
        </ActionIcon>
    )
}

export default ThemeToggle