FROM golang:1.20-alpine AS builder
WORKDIR /app
COPY . .
RUN go build -o division-api main.go

FROM alpine:latest
COPY --from=builder /app/division-api /division-api
EXPOSE 8080
ENTRYPOINT ["/division-api"]
 