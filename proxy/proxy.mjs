import { initializeAuthProxy } from '@propelauth/auth-proxy'

// Replace with your configuration
await initializeAuthProxy({
    // authUrl: "https://7133856604.propelauthtest.com/",
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
