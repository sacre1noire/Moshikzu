import { Link, Outlet } from 'react-router-dom'
import { Container, Group, Paper, Anchor } from '@mantine/core'
import ThemeToggle from './ThemeToggle'

function Layout() {
    return (
        <>
            <Paper shadow="sm" withBorder>
                <Container size="xl">
                    <Group justify="space-between" py="sm">
                        <Group>
                            <Anchor component={Link} to="/">
                                Главная
                            </Anchor>

                            <Anchor component={Link} to="/connection">
                                Подключение
                            </Anchor>

                            <Anchor component={Link} to="/schema-graph">
                                Граф схемы
                            </Anchor>

                            <Anchor component={Link} to="/findings">
                                Находки
                            </Anchor>

                            <Anchor component={Link} to="/table-details">
                                Детали таблицы
                            </Anchor>

                            <Anchor component={Link} to="/query-log">
                                Журнал запросов
                            </Anchor>
                        </Group>

                        <ThemeToggle />
                    </Group>
                </Container>
            </Paper>

            <Outlet />
        </>
    )
}

export default Layout