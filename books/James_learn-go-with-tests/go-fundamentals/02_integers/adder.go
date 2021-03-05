package integers

// Add takes two integers and returns the sum of them.

// since both x and y are integers, we can shorten the argument specification
// in the function definition from (x int, y int) to (x, y int)
func Add(x, y int) int {
	return x + y
}
