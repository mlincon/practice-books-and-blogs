package iteration

// there is no while, do and until. Only for loop
func RepeatCharacter(char string, times int) string {
	// declare a variable of type string
	// := is a shorthand for declaring a variable and assigning a value to it
	var repeated string
	for i := 0; i < times; i++ {
		repeated += char
	}
	return repeated
}
