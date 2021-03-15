package main

// not that since the size of array is fixed, if we try to say pass an [4]int,
// it will not compile
// in comparison slices do not encode the size of the collection
func SumFixedSizeArrays(numbers [5]int) int {
	sum := 0

	// the following loop is similar to
	/*
		for i := 0; i < 5; i ++ {
			sum += numbers[i]
		}
	*/
	// range lets you to iterate over an array
	// every time range is called, it returns the current index and value
	for _, number := range numbers {
		sum += number
	}

	return sum
}

// use slices
// Slices hold references to an underlying array,
// if you assign one slice to another, both refer to the same array
func SumSlices(numbers []int) int {
	sum := 0
	for _, number := range numbers {
		sum += number
	}
	return sum
}

// passed on multiple integer slices of variable length, return a slice
// containig the sum of each individual slice
func SumAll(numbersToSum ...[]int) (sums []int) {

	// use length to get len of slices
	numberOfSlices := len(numbersToSum)

	// we create a slice using the make function
	// this allows to create a slice with a starting capacity of the len of the
	// numbersToSum input argument
	sums = make([]int, numberOfSlices)

	for i, numbers := range numbersToSum {
		// index slice to assign it a new value
		sums[i] = SumSlices(numbers)
	}
	return
}

func SumAllViaAppend(numbersToSum ...[]int) []int {
	// initate a sums slice
	// in the previous function, we initiated a slice with a capacity via the make function

	// NOTE: the length of a slice is the number of elements it contains while
	// he capacity of a slice is the number of elements in the underlying array,
	// counting from the first element in the slice

	// if we try to get or assign value to value larger than the capacity,
	// we will get a runtime error

	// alternatively, we can use the append function
	// this takes a slice, adds a new value and returns a new slice with larger capacity
	var sums []int

	for _, numbers := range numbersToSum {
		sums = append(sums, SumSlices(numbers))
	}
	return sums
}

func SumAllTails(numbersToSum ...[]int) []int {
	var sums []int
	for _, numbers := range numbersToSum {
		if len(numbers) == 0 {
			sums = append(sums, 0)
		} else {
			// get the tail, here all the elements except the first (head)
			// syntax: slice[low:hight]
			tail := numbers[1:]
			sums = append(sums, SumSlices(tail))
		}
	}
	return sums
}
