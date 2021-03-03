package main

import (
	"fmt"
	"strings"
)

// define constants
const spanish = "spanish"
const french = "french"

const englishHelloPrefix = "Hello, "
const spanishHelloPrefix = "Hola, "
const frenchHelloPrefix = "Bonjour, "

// even though this is a simple hello-world exercise, we separate here the "domain"
// from "side-effects" (i.e. printing to stdout)
// the printing to stdout happens in the main() function
// since the function starts with a uppercase letter, this will be public!
func Hello(name string, language string) string {
	if name == "" {
		name = "world!"
	}

	return greetingPrefix(strings.ToLower(language)) + name
}

// separate the greetings prefix in a different function
// since the function starts with a lowercase letter, it will be private!
func greetingPrefix(language string) (prefix string) {
	// use switch case
	switch language {
	case french:
		prefix = frenchHelloPrefix
	case spanish:
		prefix = spanishHelloPrefix
	default:
		prefix = englishHelloPrefix
	}

	// a named return (prefix string), i.e. the varibale prefix, which is
	// initiated with a value of ""
	// the name of the variable that will be returned is already specified
	// in the function definition header
	return
}

func main() {
	fmt.Println(Hello("world!", ""))
}
