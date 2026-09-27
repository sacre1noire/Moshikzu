import { Button, Card, NumberInput, PasswordInput, Stack, TextInput, Title } from '@mantine/core'
import { useForm } from '@mantine/form'

function ConnectionForm() {
    const form = useForm({
        initialValues: {
            host: '',
            port: 5432,
            database: '',
            user: '',
            password: '',
        },

        validate: {
            host: (value) => (value.trim() ? null : 'Введите хост'),
            port: (value) => (value > 0 && value <= 65535 ? null : 'Некорректный порт'),
            database: (value) => (value.trim() ? null : 'Введите название базы'),
            user: (value) => (value.trim() ? null : 'Введите пользователя'),
            password: (value) => (value ? null : 'Введите пароль'),
        },
    })

    const handleSubmit = (values: typeof form.values) => {
        console.log(values) //Заглушка для API fetch/axios к FastAPI эндпоинту, который будет проверять подключение к PostgreSQL
    }

    return (
        <Card
            shadow="sm"
            padding="xl"
            radius="md"
            withBorder
            maw={600}
            mx="auto"
            mt="xl"
        >
            <form onSubmit={form.onSubmit(handleSubmit)}>
                <Stack>
                    <Title order={2}>Подключение к PostgreSQL</Title>

                    <TextInput
                        label="Хост"
                        placeholder="localhost"
                        {...form.getInputProps('host')}
                    />

                    <NumberInput
                        label="Порт"
                        placeholder="5432"
                        {...form.getInputProps('port')}
                    />

                    <TextInput
                        label="База данных"
                        placeholder="my_database"
                        {...form.getInputProps('database')}
                    />

                    <TextInput
                        label="Пользователь"
                        placeholder="postgres"
                        {...form.getInputProps('user')}
                    />

                    <PasswordInput
                        label="Пароль"
                        placeholder="Введите пароль"
                        {...form.getInputProps('password')}
                    />

                    <Button type="submit">
                        Подключиться
                    </Button>
                </Stack>
            </form>
        </Card>
    )
}

export default ConnectionForm