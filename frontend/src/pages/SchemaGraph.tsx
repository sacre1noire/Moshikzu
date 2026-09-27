import {
    Background,
    Controls,
    MiniMap,
    ReactFlow,
    type Node,
    type Edge,
} from '@xyflow/react'

import '@xyflow/react/dist/style.css'

import { Box, Stack, Text, Title } from '@mantine/core'

const nodes: Node[] = [
    {
        id: 'users',
        position: { x: 100, y: 100 },
        data: { label: 'users' },
    },
    {
        id: 'orders',
        position: { x: 400, y: 250 },
        data: { label: 'orders' },
    },
    {
        id: 'sessions',
        position: { x: 400, y: 0 },
        data: { label: 'sessions' },
    },
    {
        id: 'payments',
        position: { x: 700, y: 250 },
        data: { label: 'payments' },
    },
]

const edges: Edge[] = [
    {
        id: 'orders-users',
        source: 'orders',
        target: 'users',
        label: 'user_id',
    },
    {
        id: 'sessions-users',
        source: 'sessions',
        target: 'users',
        label: 'user_id',
    },
    {
        id: 'payments-orders',
        source: 'payments',
        target: 'orders',
        label: 'order_id',
    },
]

function SchemaGraph() {
    return (
        <Stack px="xl" mt="xl">
            <Title order={2}>
                Граф схемы
            </Title>

            <Text c="dimmed">
                Связи между таблицами базы данных
            </Text>

            <Box h={600}>
                <ReactFlow
                    nodes={nodes}
                    edges={edges}
                    fitView
                    fitViewOptions={{ padding: 0.3, maxZoom: 2 }}
                >
                    <Background />
                    <Controls />
                    <MiniMap />
                </ReactFlow>
            </Box>
        </Stack >
    )
}

export default SchemaGraph
