import { Card, List, Stack, Table, Title } from '@mantine/core'

interface ColumnInfo {
    name: string
    type: string
    nullable: boolean
    isPrimaryKey: boolean
}

interface TableInfo {
    name: string
    columns: ColumnInfo[]
    indexes: string[]
    foreignKeys: {
        column: string
        referencesTable: string
    }[]
}

const table: TableInfo = {
    name: 'orders',

    columns: [
        {
            name: 'id',
            type: 'integer',
            nullable: false,
            isPrimaryKey: true,
        },
        {
            name: 'user_id',
            type: 'integer',
            nullable: false,
            isPrimaryKey: false,
        },
        {
            name: 'status',
            type: 'varchar',
            nullable: false,
            isPrimaryKey: false,
        },
        {
            name: 'total_amount',
            type: 'numeric',
            nullable: false,
            isPrimaryKey: false,
        },
        {
            name: 'created_at',
            type: 'timestamp',
            nullable: false,
            isPrimaryKey: false,
        },
    ],

    indexes: [
        'orders_pkey',
        'idx_orders_user_id',
        'idx_orders_created_at',
    ],

    foreignKeys: [
        {
            column: 'user_id',
            referencesTable: 'users',
        },
    ],
}

function TableDetails() {
    return (
        <Stack maw={1000} mx="auto" mt="xl">
            <Title order={2}>
                Таблица: {table.name}
            </Title>

            <Card withBorder>
                <Table>
                    <Table.Thead>
                        <Table.Tr>
                            <Table.Th>Название</Table.Th>
                            <Table.Th>Тип</Table.Th>
                            <Table.Th>Nullable</Table.Th>
                            <Table.Th>Первичный ключ</Table.Th>
                        </Table.Tr>
                    </Table.Thead>

                    <Table.Tbody>
                        {table.columns.map((column) => (
                            <Table.Tr key={column.name}>
                                <Table.Td>{column.name}</Table.Td>
                                <Table.Td>{column.type}</Table.Td>
                                <Table.Td>
                                    {column.nullable ? 'Да' : 'Нет'}
                                </Table.Td>
                                <Table.Td>
                                    {column.isPrimaryKey ? 'Да' : 'Нет'}
                                </Table.Td>
                            </Table.Tr>
                        ))}
                    </Table.Tbody>
                </Table>
            </Card>

            <Card withBorder>
                <Title order={4}>
                    Индексы
                </Title>

                <List>
                    {table.indexes.map((index) => (
                        <List.Item key={index}>
                            {index}
                        </List.Item>
                    ))}
                </List>
            </Card>

            <Card withBorder>
                <Title order={4}>
                    Внешние ключи
                </Title>

                <List>
                    {table.foreignKeys.map((foreignKey) => (
                        <List.Item key={foreignKey.column}>
                            {foreignKey.column} → {foreignKey.referencesTable}
                        </List.Item>
                    ))}
                </List>
            </Card>
        </Stack>
    )
}

export default TableDetails