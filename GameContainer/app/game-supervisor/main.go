package main

import (
	"game-supervisor/input"
	"time"
)

func main() {
	time.Sleep(3 * time.Second)
	input.KeyDown("A")
	time.Sleep(10 * time.Millisecond)
	input.KeyUp("A")
}
