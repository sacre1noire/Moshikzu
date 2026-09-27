import { Badge, Card, Group, Stack, Text, Title } from '@mantine/core'

interface Finding {
    id: string
    table: string
    title: string
    severity: 'low' | 'medium' | 'high'
    description: string
}

const findings: Finding[] = [
    {
        id: '1',
        table: 'users',
        title: 'Слабая политика паролей',
        severity: 'high',
        description:
            'Политика паролей допускает использование слишком простых паролей, что снижает уровень безопасности системы.',
    },
    {
        id: '2',
        table: 'orders',
        title: 'Отсутствует внешний ключ',
        severity: 'medium',
        description:
            'В таблице orders отсутствует ограничение внешнего ключа для столбца user_id, что может привести к нарушению целостности данных.',
    },
]

const severityColors = {
    high: 'red',
    medium: 'yellow',
    low: 'green',
}

const severityLabels = {
    high: 'Высокая',
    medium: 'Средняя',
    low: 'Низкая',
}

function Findings() {
    return (
        <Stack maw={800} mx="auto" mt="xl">
            <Title order={2}>Находки</Title>

            <Text c="dimmed">
                Обнаруженные проблемы в структуре базы данных
            </Text>

            {findings.map((finding) => (
                <Card
                    key={finding.id}
                    shadow="sm"
                    padding="lg"
                    radius="md"
                    withBorder
                >
                    <Group justify="space-between" mb="xs">
                        <Text fw={500}>
                            {finding.title}
                        </Text>

                        <Badge
                            color={severityColors[finding.severity]}
                            variant="light"
                        >
                            {severityLabels[finding.severity]}
                        </Badge>
                    </Group>

                    <Text size="sm" c="dimmed" mb="xs">
                        Таблица: {finding.table}
                    </Text>

                    <Text>
                        {finding.description}
                    </Text>
                </Card>
            ))}
        </Stack>
    )
}

export default Findings