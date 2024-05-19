package main

import (
	"fmt"
	"os"
	"os/signal"
	"time"
)

func clock(arg ...string) chan string {
	ch := make(chan string)
	start := time.Now()

	go func() {
		for {
			z := time.Unix(0, 0).UTC()
			ch <- z.Add(time.Since(start)).Format("15:03:05")
			time.Sleep(1 * time.Second)
		}
	}()

	return ch
}

func main() {
	clockChan := clock()

	signalChan := make(chan os.Signal, 1)
	signal.Notify(signalChan, os.Interrupt)

	go func() {
		for currentTime := range clockChan {
			fmt.Println(currentTime)
		}
	}()

	<-signalChan
	fmt.Println("\nZamykanie programu...")
	close(clockChan)
}
