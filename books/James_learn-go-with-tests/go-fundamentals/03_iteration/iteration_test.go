package iteration

import (
	"fmt"
	"testing"
)

// tests
func TestRepeatCharacter(t *testing.T) {
	repeated := RepeatCharacter("a", 5)
	expected := "aaaaa"

	if repeated != expected {
		t.Errorf("expected %q but got %q", expected, repeated)
	}
}

// example
func ExampleRepeatCharacter() {
	repeated := RepeatCharacter("a", 5)
	fmt.Println(repeated)
	// Ouptut: aaaaa
}

// benchmarks
// benchmarks start with the keyword Benchmark similarly like Test & Example
// when the following code is executed it runs b.N times and the time taken is measured
func BenchmarkRepeatCharacter(b *testing.B) {
	for i := 0; i < b.N; i++ {
		RepeatCharacter("a", 5)
	}
}
