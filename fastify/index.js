const fastify = require("fastify")({ logger: false });

fastify.get("/plaintext", async () => "Hello, World!");
fastify.get("/json", async () => ({ message: "Hello, World!" }));

fastify.listen({ port: 6000, host: "0.0.0.0" });
