import { initializeAuthProxy } from '@propelauth/auth-proxy'

// Replace with your configuration
await initializeAuthProxy({
    authUrl: "https://7133856604.propelauthtest.com/",
    integrationApiKey: "2b9c67e49f090cf533942dde2bff4a2123d7bca6569bb9c2d91df23f34f7683c2e3fec5fc3e7a9b87b5db69a39c5f171",
    proxyPort: 8000,
    urlWhereYourProxyIsRunning: 'http://localhost:8000',
    target: {
        host: 'localhost',
        port: 8501,
        protocol: 'http:'
    },
})
