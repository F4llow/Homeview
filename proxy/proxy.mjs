import { initializeAuthProxy } from '@propelauth/auth-proxy'

// Replace with your configuration
await initializeAuthProxy({
    authUrl: "",
    integrationApiKey: "",
    proxyPort: 8000,
    urlWhereYourProxyIsRunning: 'https://homeview.studio',
    target: {
        host: 'localhost',
        port: 8501,
        protocol: 'http:'
    },
})
