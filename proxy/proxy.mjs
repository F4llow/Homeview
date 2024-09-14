import { initializeAuthProxy } from '@propelauth/auth-proxy'

// Replace with your configuration
await initializeAuthProxy({
    // authUrl: "https://7133856604.propelauthtest.com/",
    authUrl: "https://auth.homeview.studio/",
    integrationApiKey: "ad6d9ee78842e20a08652805026306f464f9927ff32867c2170ba66c567de74c607106643686f0713f89e5d14ce5aa1c",
    proxyPort: 8000,
    urlWhereYourProxyIsRunning: 'https://homeview.studio',
    target: {
        host: 'localhost',
        port: 8501,
        protocol: 'http:'
    },
})
