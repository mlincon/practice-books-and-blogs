package integers

import (
	"fmt"
	"testing"
)

// test functions
func TestAdder(t *testing.T) {
	sum := Add(2, 2)
	expected := 4

	// %d instead of %q format to print integers
	if sum != expected {
		t.Errorf("expected '%d' but got '%d'", expected, sum)
	}
}

// examples
// show how to use functions
// this are executed just like test and reside in the _test.go files
func ExampleAdd() {
	sum := Add(1, 5)
	fmt.Println(sum)
	// Output: 6
}
