package main

import "bufio"
import "fmt"
import "os"

func main() {
    args := os.Args[1:]

    data, _ := os.Open("day1/input")

    result := 0

    scanner := bufio.NewScanner(data)
    for scanner.Scan() {
        firstNumber := -1
        lastNumber := -1

        text := scanner.Text()
        for pos, character := range text {
            number := -1
            if character >= '0' && character <= '9' {
                number = (int) (character - '0')
            }

            if args[0] == "b" {
                if pos + 3 <= len(text) && text[pos:pos + 3] == "one" {
                    number = 1
                } else if pos + 3 <= len(text) && text[pos:pos + 3] == "two" {
                    number = 2
                } else if pos + 5 <= len(text) && text[pos:pos + 5] == "three" {
                    number = 3
                } else if pos + 4 <= len(text) && text[pos:pos + 4] == "four" {
                    number = 4
                } else if pos + 4 <= len(text) && text[pos:pos + 4] == "five" {
                    number = 5
                } else if pos + 3 <= len(text) && text[pos:pos + 3] == "six" {
                    number = 6
                } else if pos + 5 <= len(text) && text[pos:pos + 5] == "seven" {
                    number = 7
                } else if pos + 5 <= len(text) && text[pos:pos + 5] == "eight" {
                    number = 8
                } else if pos + 4 <= len(text) && text[pos:pos + 4] == "nine" {
                    number = 9
                }
            }
            
            if number != -1 {
                if firstNumber == -1 {
                    firstNumber = number
                }
                lastNumber = number 
            }
        }

        result += firstNumber * 10 + lastNumber;
    }

    fmt.Println(result)
}
