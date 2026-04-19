package main

import (
	"encoding/json"
	"net/http"
)

func main() {
	http.HandleFunc("/plaintext", func(w http.ResponseWriter, r *http.Request) {
		w.Write([]byte("Hello, World!"))
	})
	http.HandleFunc("/json", func(w http.ResponseWriter, r *http.Request) {
		w.Header().Set("Content-Type", "application/json")
		json.NewEncoder(w).Encode(map[string]string{"message": "Hello, World!"})
	})
	http.ListenAndServe(":4000", nil)
}
