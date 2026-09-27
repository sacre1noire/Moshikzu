import { Badge, Code, Stack, Table, Text, Title, } from '@mantine/core'
interface QueryLogEntry {
    id: string
    query: string
    executedAt: string
    isAnomaly: boolean
}

const queryLog: QueryLogEntry[] = [
    {
        id: '1',
        query: 'SELECT * FROM orders WHERE user_id = 42',
        executedAt: 'Сегодня, 18:42',
        isAnomaly: false,
    },
    {
        id: '2',
        query: 'SELECT id, status FROM orders WHERE status = \'completed\'',
        executedAt: 'Сегодня, 18:39',
        isAnomaly: false,
    },
    {
        id: '3',
        query: 'SELECT * FROM users WHERE id = 15',
        executedAt: 'Сегодня, 18:35',
        isAnomaly: false,
    },
    {
        id: '4',
        query: 'SELECT * FROM orders',
        executedAt: 'Сегодня, 18:31',
        isAnomaly: true,
    },
    {
        id: '5',
        query: 'SELECT * FROM orders CROSS JOIN users',
        executedAt: 'Сегодня, 18:27',
        isAnomaly: true,
    },
]

function QueryLog() {
    return (
        <Stack maw={1200} mx="auto" mt="xl">
            <Title order={2}>
                Журнал запросов
            </Title>

            <Text c="dimmed">
                История выполненных SQL-запросов
            </Text>
            <Table>
                <Table.Thead>
                    <Table.Tr>
                        <Table.Th>Запрос</Table.Th>
                        <Table.Th>Время выполнения</Table.Th>
                        <Table.Th>Статус</Table.Th>
                    </Table.Tr>
                </Table.Thead>

                <Table.Tbody>
                    {queryLog.map((entry) => (
                        <Table.Tr key={entry.id}>
                            <Table.Td>
                                <Code>
                                    {entry.query}
                                </Code>
                            </Table.Td>

                            <Table.Td>
                                {entry.executedAt}
                            </Table.Td>

                            <Table.Td>
                                <Badge
                                    color={entry.isAnomaly ? 'red' : 'gray'}
                                    variant="light"
                                >
                                    {entry.isAnomaly ? 'Аномалия' : 'Норма'}
                                </Badge>
                            </Table.Td>
                        </Table.Tr>
                    ))}
                </Table.Tbody>
            </Table>
        </Stack>
    )
}
export default QueryLog