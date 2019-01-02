package main

import (
	"C"
	"errors"
	"fmt"
	"math"
)
import "encoding/json"

// ErrInvalidPerson - Invalid PersonTestStruct constructor arguments
var ErrInvalidPerson = errors.New("invalid arguments to construct PersonTestStruct")

// PersonTestStruct - A struct for testing purposes
type PersonTestStruct struct {
	Name   string  `json:"name"`
	Height float64 `json:"height"`
	Age    int     `json:"age"`
}

//export NewPersonTestStructAsJSON
func NewPersonTestStructAsJSON(name string, height float64, age int) (string, error) {
	if name == "" || height < 1 || age < 1 {
		return "", ErrInvalidPerson
	}
	person := PersonTestStruct{
		Name:   name,
		Height: height,
		Age:    age,
	}
	personJSON, err := json.MarshalIndent(&person, "", "  ")
	if err != nil {
		return "", err
	}
	return string(personJSON), nil
}

//export SumFloat
func SumFloat(x, y float64) float64 {
	return x + y
}

//export Hello
func Hello() {
	fmt.Printf("Hello! The square root of 4 is: %g\n", math.Sqrt(4))
}

func main() {
	Hello()

	fmt.Println(NewPersonTestStructAsJSON(
		"bob",
		100.5,
		100,
	))

	fmt.Println(SumFloat(10.01, 10.01))
}
