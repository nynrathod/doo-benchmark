# Benchmark Project

Performance benchmark comparison across multiple frameworks.

## Start Server

```bash
# Doo
cd doo && doo build && ./output

# Go
cd go && go build -o server . && ./server

# Python (FastAPI)
cd fastapi && python main.py

# Node.js (Fastify)
cd fastify && NODE_ENV=production node index.js
```

## Benchmark

```bash
# Plaintext
wrk -t10 -c900 -d30s http://localhost:3000/plaintext

# JSON
wrk -t10 -c900 -d30s http://localhost:3000/json
```

*Note: Port may vary based on framework configuration. Keep server running in separate terminal.*


## Benchmark Configuration

- **Threads (-t)**: 10
- **Connections (-c)**: 900
- **Duration (-d)**: 30 seconds


## Notes

> **Local Machine Benchmark**
> These results were measured on a local development machine using a release build compiled with LLVM optimizations.
> Results will vary based on CPU, memory, OS, and available system resources.
> Linux is recommended for best performance. Windows results may differ due to syscall overhead.