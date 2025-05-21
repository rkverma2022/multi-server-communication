package main

import (
    "encoding/json"
    "log"
    "net/http"
    "strconv"
)

type Response struct {
    Result  float64 `json:"result,omitempty"`
    Message string  `json:"message,omitempty"`
}
 
func divisionHandler(w http.ResponseWriter, r *http.Request) {
    // Parse query parameters "a" and "b"
    aStr := r.URL.Query().Get("a")
    bStr := r.URL.Query().Get("b")

    // Convert strings to float64
    a, err := strconv.ParseFloat(aStr, 64)
    if err != nil {
        w.WriteHeader(http.StatusBadRequest)
        json.NewEncoder(w).Encode(Response{Message: "Invalid parameter 'a'"})
        return
    }

    b, err := strconv.ParseFloat(bStr, 64)
    if err != nil {
        w.WriteHeader(http.StatusBadRequest)
        json.NewEncoder(w).Encode(Response{Message: "Invalid parameter 'b'"})
        return
    }

    // Check division by zero
    if b == 0 {
        w.WriteHeader(http.StatusBadRequest)
        json.NewEncoder(w).Encode(Response{Message: "Division by zero is not allowed"})
        return
    }

    result := a / b

    w.Header().Set("Content-Type", "application/json")
    json.NewEncoder(w).Encode(Response{Result: result})
}

func main() {
    http.HandleFunc("/divide", divisionHandler)

    log.Println("Starting server on :8080...")
    if err := http.ListenAndServe(":8080", nil); err != nil {
        log.Fatalf("Server failed to start: %v", err)
    }
}
