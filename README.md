## Manning Live Proejct: Create a Data Platform for Real-time Anomaly Detection

### Review

It's a quick project creating an api reponding to prediction requests with a pretrined anomaly deteciton model. The project focuses on (relatively) realistic composition of model serving, metrics collection, and performance monitoring. These are done through fastapi, prometheus, and grafana respectively. The missing part compared to a real system is proper productionization since the components in this projects are all local.

### Demo

In the `monitoring` directory, do `ADMIN_USER=admin ADMIN_PASSWORD=admin docker-compose up -d`, and in the project folder launch the `tester.py` for sending requests. Observe metrics collected through the Grafana dashboard.

- Prometheus: http://localhost:9090/graph
- Prometheus metrics: ttp://localhost:8889/metrics/
- Fastapi: http://localhost:8889/docs
- Grafana: http://127.0.0.1:3000
