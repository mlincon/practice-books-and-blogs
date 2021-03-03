package main

import "testing"

// declare a test function with starts with the keyword Test
// the argument "hooks" into the testing framework via *testing.T
func TestHelloSimple(t *testing.T) {
	// decleare got and want variables
	got := Hello("Chris", "")
	want := "Hello, Chris"

	if got != want {
		// fmt %q wraps values in double quotes
		t.Errorf("got %q want %q", got, want)
	}
}

func TestHello(t *testing.T) {

	// we define an assert function to avoid repeated boiler-plate code
	// we use the testing.TB interface that allows to use helper functions for both testing and benchmarking
	// the assertion function gets a special t.Helper() method, so that the compiler knows that this
	// is a helper function
	assertTest := func(t testing.TB, got, want string) {
		t.Helper()
		if got != want {
			t.Errorf("got %q want %q", got, want)
		}
	}

	// scenario 1
	t.Run("saying hello to people", func(t *testing.T) {
		got := Hello("Chris", "")
		want := "Hello, Chris"
		assertTest(t, got, want)
	})

	// scenario 2
	t.Run("pass an empty string to Hello function", func(t *testing.T) {
		got := Hello("", "")
		want := "Hello, world!"
		assertTest(t, got, want)
	})

	// scenario 3
	t.Run("greetings in spanish", func(t *testing.T) {
		got := Hello("Elodie", "Spanish")
		want := "Hola, Elodie"
		assertTest(t, got, want)
	})

	// scenario 4
	t.Run("greetings in french", func(t *testing.T) {
		got := Hello("Laura", "french")
		want := "Bonjour, Laura"
		assertTest(t, got, want)
	})

}
