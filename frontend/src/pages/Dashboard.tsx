import { Card, SimpleGrid, Stack, Text, Title } from '@mantine/core'

interface DashboardStats {
    totalTables: number
    findingsBySeverity: {
        high: number
        medium: number
        low: number
    }
    lastAnalyzedAt: string
}

const stats: DashboardStats = {
    totalTables: 12,

    findingsBySeverity: {
        high: 2,
        medium: 4,
        low: 3,
    },

    lastAnalyzedAt: 'Сегодня, 18:30',
}

function Dashboard() {
    return (
        <Stack>
            <Title order={2}>
                Главная
            </Title>

            <Text c="dimmed">
                Сводка по состоянию базы данных
            </Text>

            <SimpleGrid cols={{ base: 1, sm: 3 }}>
                <Card withBorder>
                    <Text size="xl" fw={700}>
                        {stats.totalTables}
                    </Text>

                    <Text size="sm" c="dimmed">
                        Всего таблиц
                    </Text>
                </Card>

                <Card withBorder>
                    <Text size="xl" fw={700}>
                        {
                            stats.findingsBySeverity.high +
                            stats.findingsBySeverity.medium +
                            stats.findingsBySeverity.low
                        }
                    </Text>

                    <Text size="sm" c="dimmed">
                        Найдено проблем
                    </Text>
                </Card>

                <Card withBorder>
                    <Text size="xl" fw={700}>
                        {stats.lastAnalyzedAt}
                    </Text>

                    <Text size="sm" c="dimmed">
                        Последний анализ
                    </Text>
                </Card>
            </SimpleGrid>
        </Stack>
    )
}

export default Dashboard